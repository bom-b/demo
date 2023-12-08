import json
import os

from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from resnet1.models import MyResNet50Model

# Create your views here.
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

UPLOAD_DIR = 'main/static/images'

def resnet1_writer(request):
    return render(request, "resnet1/resnetImgForm.html")

@csrf_exempt
def resnet1_insert(requset):
    file = requset.FILES['file1']
    # multipart/form-data => requset.FILES['']
    # file의 _name, file_size 함께 전송되어 온다.

    print('requset.FILES["file1"] => ', requset.FILES['file1'])
    print('file_name => ', file._name)
    print('file_size =>', file.size)

    product_name = requset.POST['category']
    print("product_name => ", product_name)

    if 'file1' in requset.FILES:
        file = requset.FILES['file1']
        file_name = file._name
        fp = open(UPLOAD_DIR+file_name,'wb')
        # 'wb' = write binary = 파일을 쓰겠다는거임 1바이트씩 받아서
        # chunk() : 1바이트 단위로 읽어들이는 함수
        for chunk in file.chunks():
            fp.write(chunk)
        fp.close()

        imagePath = UPLOAD_DIR + file_name
        myModel = MyResNet50Model()

        top = myModel.myImagePredict(imagePath)
        print(f"예측결과:{top[0][1]}일 확률이 {top[0][2]:2f}%")
        resProba = f"{top[0][2]:2f}"
        resJson = {"res":top[0][1],"probability":resProba}

    return JsonResponse(resJson, json_dumps_params={'ensure_ascii': False}, safe=False)
#
#
# User = get_user_model()
#
# @csrf_exempt
# def resnet1_insert(request):
#     if request.method == 'POST':
#         load_json = json.loads(request.body.decode('utf8'))
#     else:
#         load_json = {}
#     user_key = load_json.get('user_key')
#
#     if user_key:
#         try:
#             django_user = User.objects.get(username=user_key)
#         except User.DoesNotExist:
#             django_user = User.objects.create_user(username=user_key)
#
#     message_type = load_json['type']
#     content = load_json['content']
#
#     if message_type == 'text':
#         response_msg = {
#             "message": {
#                 "text": django_user.username + "님의 메시지 입니다.\n\n" + content
#             }
#         }
#     elif message_type == 'photo':
#         response_msg = {
#             "message": {
#                 "text": django_user.username + "님의 사진 입니다.\n\n",
#                 "photo": {
#                     "url": content,
#                     "width": 720,
#                     "height": 630
#                 }
#             }
#         }
#     else:
#         response_msg = {}
#
#     return JsonResponse(response_msg)
