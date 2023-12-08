from django.shortcuts import render
# json으로 가공할때씀
import json

# RestAPI로 json으로 응답할때
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from resapi.models import make_dfall


# Create your views here.
def loadJson(request):
    df = make_dfall()[['student','kor','eng','math']]
    # Dataframe을 split형식으로 json으로 변경하는 함수
    df.to_json('student1115.json', orient='split',force_ascii=False)
    f = open('student1115.json')
    resJson = json.load(f)
    # safe = False : JsonResponse가 기본적으로 딕셔너리만 취급하는데 False로 주면 모두 허용하겠다.
    return JsonResponse(resJson,json_dumps_params={'ensure_ascii':False},safe=False)

def chartJson(request):
    return render(request, "resapi/chartJson.html")


def loadJsonp(request):
    df = make_dfall()[['student', 'kor', 'eng', 'math']]
    # print(df)
    # DataFrame을 split형식으로 json으로 변경하는 함수, student1115.json 저장
    df.to_json('student1115.json', orient='split', force_ascii=False)
    f = open('student1115.json')
    resJson = json.load(f)
    # callback function 정의
    # get 방식으로 전달되어온 파라미터의 값
    json_callback = request.GET.get('callback')
    print(f'json_callback => {json_callback}')
    # Get param = > callback
    if json_callback:
        # callback(jsonData) : 응답객체를 callback()함수에 감싸서 전달
        response = HttpResponse("%s(%s);" %(json_callback,json.dumps(resJson,ensure_ascii=False)))
        response["Content-Type"] = "text/javascript; charset=utf-8"
        print("JsonP")
    else:
        return JsonResponse(resJson,json_dumps_params={'ensure_ascii':False},safe=False)
        print('Json')
    return  response


@csrf_exempt
def gojango(request):
    # ajax로 보낸 Formdata를 변수로 받기
    name = request.POST['file'] + "(django 서버에서 정제됨)"
    date = request.POST['date'] + "(django 서버에서 정제됨)"
    print(f"name => {name}, date => {date}")

    # 받은 데이터를 딕셔너리 형태로 변환
    image_data = {"file_name": name, "file_date": date}

    # 딕셔너리를 json형식으로 변환하고 저장
    with open('homework.json', 'w', encoding='utf-8') as file:
        json.dump(image_data, file, ensure_ascii=False, indent=4)

    # 저장된 json파일을 변수로 만들기
    f = open('homework.json')
    resJson = json.load(f)

    # JsonResponse()를 통해 json파일(resJson) 전송하기
    return JsonResponse(resJson, json_dumps_params={'ensure_ascii': False}, safe=False)



