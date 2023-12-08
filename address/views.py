from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from address.models import Address


# Create your views here.

def writeForm(request):
    # address/templates/address/write.html
    # {"msg":"안녕~"} = 진자 문법?? 익스프레션 랭귀지로 사용할 수 있음
    return render(request, "address/write.html", {"msg": "안녕~ㅋㅋ"})


# @csrf_exempt # csrf 토큰 검증 그냥 생략하겠다는 뜻
def insert(request):
    namev = request.POST['name']
    telv = request.POST['tel']
    emailv = request.POST['email']
    addressv = request.POST['address']
    print(f"name = {namev}")
    addr = Address(name=namev, tel=telv, email=emailv, address=addressv)
    # res.save() => insert into address_address values(increment,val,val,val...)
    addr.save()
    return redirect("/address/list")


def addList(request):
    # entity 클래스를 생성한다.
    # Address.objects : select 객체가 리스트로 저장이 됨
    # .order_by('name') : 오름차순
    # .order_by('-name') : 내림차순
    items = Address.objects.order_by('idx')
    # <QuerySet [<Address: Address object (1)>, <Address: Address object (2)>, <Address: Address object (3)>, <Address: Address object (4)>, <Address: Address object (5)>]>
    print(items.all())
    print(type(items))
    # for i in items:
    #     print(f"idx -> {i.idx}, i.name -> {i.name}")
    # 카운트 뽑기
    address_count = Address.objects.all().count()
    return render(request, "address/list.html", {'items': items, 'address_count': address_count})


def detail(request):
    idv = request.GET['idx']
    print(f"{idv}")
    # view ->
    addr = Address.objects.get(idx=idv)
    print('type => ', type(addr))
    print('addr => ', addr)
    print('name => ', addr.name)
    return render(request, 'address/detail.html', {'addr': addr})


def update(request):
    idv = request.POST['idx']
    namev = request.POST['name']
    telv = request.POST['tel']
    emailv = request.POST['email']
    addressv = request.POST['address']
    # 기존에 idx값이 존재하면 수정. save()로 구분한다. update라는 메서드가 존재하지 않음.
    addr = Address(idx=idv, name=namev, tel=telv, email=emailv, address=addressv)
    addr.save()
    return redirect("/address/list")


def delete(request):
    id = request.POST['idx']
    Address.objects.get(idx=id).delete()
    return redirect("/address/list")
