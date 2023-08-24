from django.shortcuts import render,redirect,HttpResponse
from .forms import *
from django.contrib.auth import authenticate,login, logout
from .models import Turffdetails,Tbooking

# Create your views here.
def run(req):
    context={}
    context['data']=Turffdetails.objects.all()
    # return render(request,'turff_list.html',context=context)
    return render(req,'base.html',context=context)

def signup(req):
    if req.method=='GET':
        context={'form':UserForm()}
        return render(req,'signup.html',context=context)
    elif req.method=='POST':
        form=UserForm(req.POST,req.FILES)

        if form.is_valid():
            obj=form.save(commit=False)
            obj.set_password(form.cleaned_data['password'])
            # obj.is_staff = True
            obj.save()
            return redirect("run")
        else:
            return render(req,'signup.html',context={'form':UserForm()})
    

def action_login(request):
    if request.method=='GET':
        return render(request,'login.html')
    elif request.method=='POST':
        uname=request.POST['uname']
        password=request.POST['password']
        user=authenticate(request, username=uname, password=password)
        if user is not None:
            login(request,user)
            if user.is_superuser:
                return redirect('run')
            
            else:
                return redirect('run')
            return HttpResponse('success')
        else:
            return HttpResponse("Failed")
        
def action_logout(request):
    logout(request)
    return redirect('login')

def turff_list(request):
    context={}
    context['data']=Turffdetails.objects.all()
    return render(request,'turff_list.html',context=context)

def owner_turff_list(request):
    context={}
    context['data']=Turffdetails.objects.filter(turff_owner=request.user)
    return render(request,'ownerturfflist.html',context=context)
def turffdelete(req,id):
    turff=Turffdetails.objects.get(pk=id)
    turff.delete()
    return redirect('owner_turff_list')
def owner_signup(req):
    if req.method=='GET':
        context={'form1':UserForm(),'form2':OwnerForm()}
        return render(req,'owner_signup.html',context=context)
    elif req.method=='POST':
        form1=UserForm(req.POST)
        form2=OwnerForm(req.POST)
        if form1.is_valid() and form2.is_valid():
            obj=form1.save(commit=False)
            obj.set_password(form1.cleaned_data['password'])
            obj.is_staff = True
            obj1=form2.save(commit=False)
            obj1.user=obj
            obj.save()
            obj1.save()
            return redirect("run")
        else:
            return render(req,'signup.html',context={'form':UserForm()})
        
def turffdetails_form(req):
    if req.method=='GET':
        context={'form':TurffdetailsForm()}
        return render(req,'add_turff.html',context=context)
    elif req.method=='POST':
        form=TurffdetailsForm(req.POST,req.FILES)

        if form.is_valid():
            obj=form.save(commit=False)
            obj.turff_owner = req.user
            obj.save()
            return redirect('run')
            
        else:
            return render(req,'add_turff.html',context={'form':TurffdetailsForm()})
        
def turff_in_detail(req,id):
    data=Turffdetails.objects.get(pk=id)
    context={}
    context['turff']=data
    return render(req,'turff_detail_view.html',context=context)

def booking(req,id):
    turff=Turffdetails.objects.get(pk=id)
    context={'turff':turff}
    
    if req.method=='GET':
        return render(req, "tbooking.html",context=context)
    elif req.method=='POST':
        # c_name=req.POST['c_name']
        # detail=req.POST['turff_name']
        date=req.POST['date']
        s_time=req.POST['s_time']
        e_time=req.POST['e_time']
        duration=req.POST['duration']
        amount=req.POST['amount']
        obj = Tbooking.objects.create(c_name=req.user,detail=turff,date=date,s_time=s_time,e_time=e_time,duration=duration,amount=amount)
        
        return redirect('confirm', id=obj.id)

def confirm(req,id): 
    booking=Tbooking.objects.get(pk=id)
    context={'booking':booking}
    return redirect('success')

def booking_success(req):
    return render(req, 'note.html')
def about(req):
    return render(req,'about.html')
def mybook(req):
    context = {}
    context["bookings"] = Tbooking.objects.filter(c_name=req.user)
    return render(req,'mybook.html', context)
def tdelete(req,id):
    booking=Tbooking.objects.get(pk=id)
    booking.delete()
    return redirect('mybook')
def ownerbook(req):
    context = {}
    context["bookings"] = Tbooking.objects.filter(detail__turff_owner=req.user)
    return render(req,'ownerbook.html', context)