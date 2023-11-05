
from django.http import HttpResponse
from django.shortcuts import render, redirect
from adminapp.models import Admin,Organisation,Donor,Donororgmapping

def index(request):
    return render(request,"index.html")
def login(request):
    return render(request,'login.html')
def checkadminlogin(request):
    uname=request.POST['uname']
    pwd=request.POST['pwd']
    f1=Admin.objects.filter(username=uname,password=pwd)
    f2=Organisation.objects.filter(name=uname,password=pwd)
    f3=Donor.objects.filter(name=uname,password=pwd)
    if f1:
        request.session['aname']=uname
        return render(request,'adminhome.html',{"aname":uname})
    elif f2:
        request.session['oname']=uname
        alldonors = Donororgmapping.objects.all()
        don = []
        for i in alldonors:
            if i.organisation.name == uname:
                don.append(i)
        amount = 0
        for i in don:
            amount = i.amount + amount
        organ = Organisation.objects.get(name=uname)
        return render(request,'organisationhome.html',{"oname":uname,"organ":organ,"amt":amount})
    elif f3:
        request.session['dname']=uname
        don = Donor.objects.get(name=uname)
        return render(request,'donorhome.html',{'dname':uname,"don":don})
    else:
        message='invalid credentials'
        return render(request,'login.html',{'msg':message})
def home(request):
    return redirect("index")
def about(request):
    return render(request,'about.html')

def orgsignup(request):
    return render(request,'orgsignup.html')
def orgsignedup(request):
    name = request.POST['orgname']
    email = request.POST['email']
    type = request.POST['type']
    address = request.POST['address']
    password = request.POST['pwd']
    if type is 'governmental' or 'non governmental':
         org = Organisation(name=name, email=email, type=type, address=address, password=password)
         Organisation.save(org)
         message='registered successfully'
         return render(request,'orgsignup.html',{'msg':message})
    else:
        message='registration unsuccessful'
        return render(request,'orgsignup.html',{'msg':message})

def donorsignup(request):
    return render(request,'donorsignup.html')
def donorsignedup(request):
    name=request.POST['name']
    email=request.POST['email']
    gender=request.POST['gender']
    age=request.POST['age']
    password=request.POST['pwd']
    address=request.POST['address']
    if gender is 'male' or 'female' or 'others' :
        donor=Donor(name=name,email=email,gender=gender,age=age,password=password,address=address)
        Donor.save(donor)
        message='registered successfully'
        return render(request,'donorsignup.html',{'msg':message})
    else:
        message = 'registration unsuccessful'
        return render(request, 'donorsignup.html', {'msg': message})

