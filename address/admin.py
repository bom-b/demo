from django.contrib import admin

# admin.ModelAdmin을 상속 받아서 관리자 화면에서 설정 할 내용등을 등록까지 하는 기능
from address.models import Address

# Register your models here.
class AddressAdmin(admin.ModelAdmin):
    # admin 화면에 출력 될 필드 목록을 정의
    list_display = ('name','tel','email','address')

# admin site에 Model인 Address , AddressAdmin register함
# Address ALT + Enter
admin.site.register(Address,AddressAdmin)
