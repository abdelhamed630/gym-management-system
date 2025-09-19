from datetime import timezone
from django.shortcuts import render,redirect,get_object_or_404
from .forms import CreateUserForm,LoginForm,CreateRecord,UpdateRecordForm
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from .models import record
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import logging
from django.contrib import messages
from django.utils.timezone import now
from django.utils import timezone




def index(request):

    return render(request,'web/index.html')


def register(request):
    if request.POST:
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Registrations succssfully')
            return redirect('login')
    else:
        form=CreateUserForm()
    context={'form':form}
    return render(request,'web/register.html',context)


def login(request):
    form=LoginForm()
    if request.method == 'POST':
        form=LoginForm(request,data=request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            
            user=authenticate(request,username=username,password=password)
            if user is not None:
                auth_login(request,user)
                messages.success(request,'Login succssfully')
                return redirect('dashbord')
    else:
        form=LoginForm()
    context={'form':form}
    return render(request,'web/login.html',context)
        

   
def home(request):
    context={'record':record}
    return render(request,'web/index.html',context)


@login_required(login_url='login')
def dashbord(request):
    recor=record.objects.all()
    context={'record':recor}
    return render(request,'web/dashbord.html',context)




@login_required(login_url='login')
def creat_record(request):
    form=CreateRecord()
    if request.method== "POST":
       form= CreateRecord(request.POST)
       if form.is_valid():
           form.save()
           messages.success(request,'recorded succssfully')
           return redirect('dashbord')
    else:
        form=CreateRecord()
    context={'form':form}
    return render(request,'web/record.html',context)
    
    
    
@login_required(login_url='login') 
def view(request,record_id):
    all=get_object_or_404(record,id=record_id)
    context={"record":all}
    return render(request,'web/view.html',context)
    
    
    
@login_required(login_url='login')
def update_record(request,record_id):
    Record=get_object_or_404(record,id=record_id)
    form=UpdateRecordForm(instance=Record)
    if request.method=='POST':
        form=UpdateRecordForm(request.POST,instance=Record)
        if form.is_valid():
            form.save()
            messages.success(request,'Updated succssfully')
            return redirect('dashbord')
    context={'record':form}
    return render(request,'web/update.html',context)



@login_required(login_url='login')
def delete(request,record_id):
     Record=get_object_or_404(record,id=record_id)
     Record.delete()
     messages.success(request,'Deleted succssfully')
     return redirect('dashbord')



logger=logging.getLogger(__name__)
@login_required(login_url='login')
def search(request):
    quary=request.GET.get("q")
    results=[]
    try:
        if quary:
            results=record.objects.filter(Q(name__icontains=quary) | Q(id__icontains=quary))
    except Exception as e:
        logger.error('Erro during search: %s', e)
    context={'results':results,'quary':quary}
    return render(request,'web/search.html',context)
    

def logout(request):
    auth_logout(request)
    messages.success(request,'Logout succssfully')
    return redirect('login')



@login_required(login_url='login')
def renew_payment(request, record_id):
    member = get_object_or_404(record, id=record_id)
    member.last_payment = timezone.now().date()  # تحديث التاريخ
    member.save()
    messages.success(request, f"تم تجديد الاشتراك للعضو {member.name} بنجاح ✅")
    return redirect('dashbord')


def erro_page(request,exception):
    return render(request,'web/404.html',status=404)
    
