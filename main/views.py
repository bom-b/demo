import json
import os
import re

from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from resnet1.models import MyResNet50Model
import requests
from datetime import datetime
from googletrans import Translator

UPLOAD_DIR = 'main/static/images'
# Create your views here.
def mymain(request):
    return render(request, "main/main.html")


def error(request):
    return render(request, "main/error.html")

User = get_user_model()

def keyboard(request):
    return JsonResponse({"type": "text"})


@csrf_exempt
def keyboard2(request):
    return JsonResponse({
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "간단한 텍스트 요소입니다."
                    }
                }
            ]
        }
    })


@csrf_exempt
def picture_test(request):

    load_json = json.loads(request.body.decode('utf8'))
    # print(str(load_json))
    secureimage_str = load_json.get('action').get('params').get("secureimage", '{}')
    # print(secureimage_str)
    match = re.search(r'"secureUrls":"(List\(.+?\))"', secureimage_str)
    secure_urls_str = match.group(1)[5:-1]
    # print(secure_urls_str)

    now = datetime.now()
    # datetime 객체를 초로 변환합니다.
    timestamp = str(int(now.timestamp()))

    response = requests.get(secure_urls_str)
    myModel = MyResNet50Model()

    if response.status_code == 200:
        image_data = response.content

        save_path = os.path.join(UPLOAD_DIR, f"{timestamp}.jpg")

        with open(save_path, "wb") as f:
            f.write(image_data)

    else:
        print(f"Failed to download image. Status code: {response.status_code}")

    top = myModel.myImagePredict(UPLOAD_DIR + "/" + f"{timestamp}.jpg")

    res = top[0][1]
    resProba = float(f"{top[0][2]:.3f}") * 100
    f_resProba = f"{resProba:.1f}"

    # res2 = top[1][1]
    # resProba2 = float(f"{top[1][2]:.3f}") * 100
    # f_resProba2 = f"{resProba2:.1f}"
    #
    # res3 = top[2][1]
    # resProba3 = float(f"{top[2][2]:.3f}") * 100
    # f_resProba3 = f"{resProba3:.1f}"

    translator = Translator()
    ko_res = translator.translate(res, dest='ko').text
    # ko_res2 = translator.translate(res2, dest='ko').text
    # ko_res3 = translator.translate(res3, dest='ko').text

    return JsonResponse({
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "basicCard": {
                        "title": f"예측 결과 : {ko_res}",
                        "description": f"'{ko_res}'일 확률이 {f_resProba}%입니다.",
                        # "description": f"'{ko_res}'일 확률이 {f_resProba}%입니다. \n\n(후보)\n'{ko_res2}'일 확률이 {f_resProba2}%\n'{ko_res3}'일 확률이 {f_resProba3}%",
                        "thumbnail": {
                            "imageUrl": secure_urls_str
                        },
                        "buttons": [
                            {
                                "action": "webLink",
                                "label": "크게보기",
                                "webLinkUrl": secure_urls_str
                            }
                        ]
                    }
                }
            ]
        }
    })