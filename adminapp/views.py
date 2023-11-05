from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Admin,Organisation,Donor



def adminhome(request):
    aname=request.session['aname']
    return render(request,'adminhome.html',{'aname':aname})
def ahome(request):
    return redirect('adminhome')
def logout(request):
    return redirect('login')
def adminviewdonors(request):
    aname=request.session['aname']
    donor=Donor.objects.all()
    return render(request,'adminviewdonors.html',{'aname':aname,'donor':donor})
def adminvieworg(request):
    aname=request.session['aname']
    org=Organisation.objects.all()
    return render(request,'adminvieworg.html',{'aname':aname,'organisation':org})
def adminchangepwd(request):
    aname=request.session['aname']
    return render(request,'adminchangepwd.html',{'aname':aname})
def adminpwdupdated(request):
    aname=request.session['aname']
    opwd=request.POST['opwd']
    npwd=request.POST['npwd']
    flag=Admin.objects.filter(password=opwd,username=aname)
    if flag:
        Admin.objects.filter(username=aname,password=opwd).update(password=npwd)
        message='password updated successfully'
        return render(request,'adminchangepwd.html',{'aname':aname,'msg':message})
    else:
        message = 'Enter valid old password'
        return render(request, 'adminchangepwd.html', {'aname': aname, 'msg': message})
def aupdatedonor(request,did):
    aname=request.session['aname']
    return render(request,'aupdatedonor.html',{'aname':aname,'did':did})
def adonorupdation(request):
    aname=request.session['aname']
    did=request.POST['id']
    name=request.POST['name']
    email=request.POST['email']
    address=request.POST['address']
    Donor.objects.filter(Q(id=did)).update(name=name,email=email,address=address)
    message="details updated successfully"
    return render(request,'aupdatedonor.html',{'aname':aname,'msg':message})

def aupdateorg(request):
    return render(request,'aupdateorg.html')
def adeletedonor(request):
    return render(request,'adeletedonor.html')
def adeleteorg(request):
    return render(request,'adeleteorg.html')

