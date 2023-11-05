from django.shortcuts import render
from adminapp.models import Admin,Donor,Organisation,Donororgmapping

def organisationhome(request):
    oname=request.session['oname']
    alldonors=Donororgmapping.objects.all()
    don=[]
    for i in alldonors:
        if i.organisation.name==oname:
            don.append(i)
    amount=0
    for i in don:
        amount=i.amount+amount
    organ=Organisation.objects.get(name=oname)
    return render(request,'organisationhome.html',{'oname':oname,"organ":organ,"amt":amount})
def orgchangepwd(request):
    oname=request.session['oname']
    return render(request,"orgchangepwd.html",{'oname':oname})
def orgpwdupdated(request):
    oname=request.session['oname']
    opwd=request.POST['opwd']
    npwd=request.POST['npwd']
    flag=Organisation.objects.filter(password=opwd,name=oname)
    if flag:
        Organisation.objects.filter(password=opwd,name=oname).update(password=npwd)
        message="password updated successfully"
        return render(request,"orgchangepwd.html",{'oname':oname,"msg":message})
    else:
        message="enter valid old password"
        return render(request,"orgchangepwd.html",{'oname':oname,'msg':message})

def orgdonors(request):
    oname=request.session['oname']
    orgdonors=Donororgmapping.objects.all()
    orgdon=[]
    for i in orgdonors:
        if i.organisation.name==oname:
            orgdon.append(i)
    return render(request,'orgdonors.html',{'oname':oname,"orgdon":orgdon})
