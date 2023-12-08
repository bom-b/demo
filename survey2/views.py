from django.core.serializers import serialize
from django.db import connection
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from survey2.models import PracticeSurvey, PracticeAnswer


# Create your views here.

def surveyList(request):
    """

    SELECT *
    FROM survey_survey
    WHERE status = 'y'
    ORDER BY survey_idx DESC
    LIMIT 1;

    """
    # where = filter를 사용해서 조건의 값을 설정
    survey = PracticeSurvey.objects.filter(status='y').order_by("-survey_idx")[0]
    print('survey.question => ', survey.question)
    return render(request, "survey2/list.html", {'survey': survey})


def show_result(request):
    print('결과확인 함수 호출')
    idx = request.GET['survey_idx']
    ans = PracticeSurvey.objects.get(survey_idx=idx)
    answer = [ans.ans1, ans.ans2, ans.ans3, ans.ans4]

    surveyList = PracticeSurvey.objects.raw("""
    select survey_idx,num,count(num) sum_num,
    round((select count(*) from survey2_Practiceanswer
    where survey_idx = a.survey_idx and num = a.num)*100.0/(select count(*) from survey2_Practiceanswer where survey_idx = a.survey_idx),2)
    rate
    from survey2_Practiceanswer a where survey_idx = %s
    group by survey_idx, num
    order by num
    """, idx)

    survey_list = [
        {
            'num': survey.num,
            'sum_num': survey.sum_num,
            'rate': survey.rate,
            'answer': answer[i]
        }
        for i, survey in enumerate(surveyList)
    ]

    return JsonResponse({'surveyList': survey_list})


@csrf_exempt
def save_survey(request):
    survey_idxv = request.POST['survey_idx']
    numv = request.POST['num']
    print("넘어오나~", survey_idxv, numv)
    survey = PracticeSurvey.objects.get(survey_idx=survey_idxv)
    dto = PracticeAnswer(num=numv, survey_idx=survey)
    dto.save()
    return redirect(f"/survey2/show_result2?survey_idx={survey_idxv}")
