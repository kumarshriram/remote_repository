from django.shortcuts import render
from django.http.response import HttpResponse
from curdapp1.models import ProductData
def home(request):
    return  render(request,'curd_home.html')
def create_view(request):
    if request.method=="POST":
            product_id=request.POST.get('pid')
            product_name=request.POST.get('pname')
            product_cost=request.POST.get('pcost')
            product_class=request.POST.get('pclass')
            no_of_products=request.POST.get('npros')
            manufacture_date=request.POST.get('mdate')
            expiry_date=request.POST.get('edate')
            customer_name=request.POST.get('cname')
            mobile=request.POST.get('mobile')
            email=request.POST.get('email')
            data=ProductData(
                pid=product_id,
                pname=product_name,
                pcost=product_cost,
                pclass=product_class,
                npros=no_of_products,
                mdate=manufacture_date,
                edate=expiry_date,
                cname=customer_name,
                mobile=mobile,
                email=email,

            )
            data.save()

            return render(request,'curdfile.html')

    else:

        return  render(request,'curdfile.html')


def retrieve_view(request):
    data=ProductData.objects.all()
    return render(request,'retrieve.html',{'data':data})


def update_view(request):
    if request.method=='POST':
        product_id=request.POST.get('pid')
        product_cost=request.POST.get('pcost')
        pid=ProductData.objects.filter(pid=product_id)

        if not pid:
            return HttpResponse('not available')
        else:
            pid.update(pcost=product_cost)
            return  render(request,'update.html')
    else:
        return render(request,'update.html')


def delete_view(request):
    if request.method=='POST':
        product_id=request.POST.get('pid')
        pid=ProductData.objects.filter(pid=product_id)
        if not pid:
            return HttpResponse('not available')
        else:
            pid.delete()
            return render(request,'delete.html')
    else:
        return render(request,'delete.html')