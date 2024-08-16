from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def index(request):
    data=category.objects.all().order_by('-id')[0:20]
    sliderdata=slider.objects.all().order_by('-id')[0:3]
    edata=medicine.objects.all().order_by('-id')[0:100]
    #print(data)
    md={"cdata":data,"sdata":sliderdata,"edata":edata}
    return render(request,'user/index.html',md)
def about(request):
    return render(request,'user/aboutus.html')
def contact(request):
    if request.method=="POST":
        a1=request.POST.get('name')
        a2=request.POST.get('email')
        a3=request.POST.get('mobile')
        a4=request.POST.get('message')
        #print(a1,a2,a3,a4)
        x=contactus(Name=a1,Email=a2,Mobile=a3,Message=a4).save()
        return HttpResponse("<script>alert('Thank you for contacting with us');location.href='/user/contact/' </script>")


    return render(request,'user/contactus.html')
def signin(request):
    if request.method=="POST":
        email=request.POST.get('email')#Ram@gmail.com
        passwd=request.POST.get('passwd')#12345
        x=register.objects.filter(email=email,passwd=passwd).count()
        if x==1:
            a=register.objects.filter(email=email,passwd=passwd)
            request.session['username']=str(a[0].uname)
            request.session['userpic']=str(a[0].upic)
            request.session['user']=email
            return HttpResponse("<script>alert('You are signed In ');location.href='/user/signin/'</script>")
        else:
            return HttpResponse("<script>alert('Your userid or password is incorrect...');location.href='/user/signin/'</script>")
    return render(request,'user/signin.html')
def signup(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')#xyz@gmail.com
        passwd=request.POST.get('passwd')
        address=request.POST.get('address')
        picture=request.FILES['fu']
        a=register.objects.filter(email=email).count()
        if a==0:
            register(email=email,uname=name,passwd=passwd,address=address,upic=picture).save()
            return HttpResponse("<script>alert('You are registered successfully...');location.href='/user/signup/'</script>")

        else:
            return HttpResponse("<script>alert('You are already registered..');location.href='/user/signup/'</script>")
    return render(request,'user/signup.html')
def mymedicine(request):
    cid=request.GET.get('msg')
    if cid is not None:
        edata=medicine.objects.filter(medicine_category=cid)
    else:
        edata=medicine.objects.all().order_by('-id')
    md={"edata":edata}
    return render(request,'user/medicine.html',md)

def igallery(request):
    cid=request.GET.get('cid')
    if cid is not None:
        idata=imagegallery.objects.filter(category=cid)
    else:
        idata=imagegallery.objects.all().order_by('-id')
    cdata=category.objects.all().order_by('-id')
    mydict={"idata":idata,"cdata":cdata}
    return render(request,'user/igallery.html',mydict)

def vgallery(request):
    cid=request.GET.get('x')
    cdata=category.objects.all().order_by('-id')
    if cid is not None:
        vdata=videogallery.objects.filter(category=cid)
    else:
        vdata=videogallery.objects.all().order_by('-id')
    mydict={
        "cdata":cdata,
        "vdata":vdata,
    }
    return render(request,'user/vgallery.html',mydict)

def viewdetails(request):
    eid=request.GET.get('msg')
    edata=medicine.objects.filter(id=eid)
    md={"edata":edata}
    return render(request,'user/viewdetails.html',md)

def logout(request):
    user=request.session.get('user')
    if user:
        del request.session['user']
        del request.session['username']
        del request.session['userpic']
        return HttpResponse("<script>alert('You are logout successfully..');location.href='/user/index/'</script>")


    return render(request,'user/logout.html')



def payment(request):
    return render(request,'user/payment.html')