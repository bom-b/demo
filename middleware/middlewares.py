# myapp/middleware.py
from django.shortcuts import redirect


class IPCheckMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # 클라이언트의 IP 주소를 얻습니다.
        client_ip = self.get_client_ip(request)

        # IP 주소를 출력하거나 원하는 다른 작업을 수행합니다.
        print(f"접속한 IP Address: {client_ip}")
        if client_ip != "192.168.0.17":
            request.session['waring'] = True
            request.session['waring_ip'] = f"{client_ip} 이거 누구냐"

            if client_ip == "192.168.0.30":
                request.session['waring_ip'] = "승현ㅎㅇ"

            if client_ip == "192.168.0.211":
                request.session['waring_ip'] = "민섭ㅎㅇ"

            if client_ip == "192.168.0.7":
                request.session['waring_ip'] = "민섭폰ㅎㅇ"

            if client_ip == "192.168.0.225":
                request.session['waring_ip'] = "진원ㅎㅇ"

            if client_ip == "192.168.0.180":
                request.session['waring_ip'] = "내폰ㅎㅇ"

        # 다음 미들웨어 또는 뷰로 요청을 전달합니다.
        response = self.get_response(request)

        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
