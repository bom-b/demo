from django.shortcuts import render, redirect

from login.models import LoginDao


# Create your views here.

# 로그인 화면으로 넘어가는 get과 로그인 정보를 넘기는 post 둘다 처리
def loginform(request):
    print(f"Method: {request.method}")
    # session이 존재한다면 메인으로 이동
    if 'user_id' in request.session:
        return redirect("/")
    if request.method == 'POST':
        user_id = request.POST['id']
        user_pwd = request.POST['pwd']
        #SQL id, pwd를 전송한 다음에 결과값을 반환 받아서 세션을 등록할지 말지를 결정하기!
        loginlist = (user_id,user_pwd)
        login_ref = LoginDao()
        login_res = login_ref.loginCheck(loginlist)
        print(f"login_res => {login_res}")
        if login_res is not None:
            print("로그인 성공")
            request.session['user_id'] = user_id
            request.session['user_name'] = login_res[0]
            return redirect('/')
        else:
            print("로그인 실패")
    return render(request, 'login/login.html')


def logout(request):
    del request.session['user_id']
    del request.session['user_name']
    return redirect("/")
