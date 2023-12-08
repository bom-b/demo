from django.http import JsonResponse
from django.shortcuts import render, redirect

from shop.models import Product

# Create your views here.
UPLOAD_DIR = '/home/ict01/PycharmProjects/demo/shop/static/images/'


def product_write(request):
    return render(request, "shop/upload.html")


def product_insert(request):
    ##### file upload process
    # file = request.FILES['file1']
    # print('type :', type(file))
    # print('dir :', dir(file))
    # print(file._name)  # sessionid2123123.png
    # print(file.size)
    if 'file1' in request.FILES:
        file = request.FILES['file1']
        file_name = file._name
        with open(f"{UPLOAD_DIR}{file_name}", 'wb') as f:
            # chunks() : 1byte단위로 읽어들이면 True
            for chunk in file.chunks():
                f.write(chunk)
    else:
        file_name = '-'
    dto = Product(
        product_name=request.POST['product_name'],
        price=request.POST['price'],
        description=request.POST['description'],
        picture_url=file_name)
    dto.save()
    return redirect('/shop/list')


def product_list(request):
    count = Product.objects.count()
    productList = Product.objects.order_by("-product_id")
    return render(request, 'shop/list.html', {'productList': productList, 'count': count})


def product_detail(request):
    num = request.GET['num']
    print(f"{num}")
    # view ->
    product = Product.objects.get(product_id=num)
    return render(request, 'shop/detail.html', {'product': product})


# 전체 업데이트
def product_update(request):
    product_id = request.POST['product_id']
    product_name = request.POST['product_name']
    price = request.POST['price']
    description = request.POST['description']
    if 'file1' in request.FILES:
        file = request.FILES['file1']
        file_name = file._name
        with open(f"{UPLOAD_DIR}{file_name}", 'wb') as f:
            # chunks() : 1byte단위로 읽어들이면 True
            for chunk in file.chunks():
                f.write(chunk)
    else:
        file_name = '-'
    # 기존에 idx값이 존재하면 수정. save()로 구분한다. update라는 메서드가 존재하지 않음.
    product = Product(product_id=product_id, product_name=product_name, price=price, description=description,
                      picture_url=file_name)
    product.save()
    return redirect('/shop/list')


# 이미지만 업데이트
def product_update_img(request):
    product_id = request.POST['product_id']
    # 먼저 넘겨받은 product_id에 해당하는 Product 객체를 가져온다.
    product = Product.objects.get(product_id=product_id)

    if 'file1' in request.FILES:
        file = request.FILES['file1']
        file_name = file._name
        with open(f"{UPLOAD_DIR}{file_name}", 'wb') as f:
            # chunks() : 1byte단위로 읽어들이면 True
            for chunk in file.chunks():
                f.write(chunk)
        status = '이미지 업데이트 성공'
    else:
        file_name = '-'
        status = '이미지 삭제 성공'

    # Product 객체의 picture_url 값만 새로운 file_name 으로 수정한다.
    product.picture_url = file_name
    product.save()

    # JsonResponse를 통해 새로 등록에 성공한 이미지 파일의 이름과, 업데이트/삭제 여부를 나타내는 status를 넘긴다.
    return JsonResponse({'status': status, 'file_name': file_name})


def product_delete(request):
    id = request.POST['product_id']
    Product.objects.get(product_id=id).delete()
    return redirect('/shop/list')
