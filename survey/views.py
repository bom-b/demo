from django.db import connection
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from survey.models import Survey, Answer


# Create your views here.

def serveyList(request):
    """

    SELECT *
    FROM survey_survey
    WHERE status = 'y'
    ORDER BY survey_idx DESC
    LIMIT 1;

    """
    # where = filter를 사용해서 조건의 값을 설정
    survey = Survey.objects.filter(status='y').order_by("-survey_idx")[0]
    print('survey.question => ', survey.question)
    return render(request, "survey/list.html", {'survey':survey})


def show_result(request):
    """"
    SELECT survey_idx, num, sum_num, ROUND((sum_num * 1.0 / total_sum)* 100, 2) AS rate
    FROM (
    SELECT survey_idx, num, COUNT(*) AS sum_num,(SELECT COUNT(*) FROM survey_answer WHERE survey_idx = 1) AS total_sum
    FROM survey_answer
    WHERE survey_idx = 1
    GROUP BY num
    );
    """
    idx = request.GET['survey_idx']
    ans = Survey.objects.get(survey_idx=idx)
    answer = [ans.ans1, ans.ans2, ans.ans3, ans.ans4]

    surveyList = Survey.objects.raw("""
    select survey_idx,num,count(num) sum_num,
    round((select count(*) from survey_answer
    where survey_idx = a.survey_idx and num = a.num)*100.0/(select count(*) from survey_answer where survey_idx = a.survey_idx),2)
    rate
    from survey_answer a where survey_idx = %s
    group by survey_idx, num
    order by num
    """, idx)

    surveyList = list(zip(surveyList, answer))
    for e,ans in surveyList:
        print(f"{ans} -> {e.rate}")

    return render(request, "survey/result.html", {'surveyList': surveyList})

@csrf_exempt
def save_survey(request):
    survey_idxv = request.POST['survey_idx']
    numv = request.POST['num']
    print("넘어오나~",survey_idxv, numv)
    survey = Survey.objects.get(survey_idx=survey_idxv)
    dto = Answer(num=numv,survey_idx=survey)
    dto.save()
    return render(request,"survey/success.html",{'survey_idx':survey_idxv})


