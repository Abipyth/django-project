from django.shortcuts import render
from .forms import MyFileForm
from .models import MyFileUpload
from django.contrib import messages
from django.shortcuts import redirect
import os
from django.urls import path
from django.contrib.auth.models import User,auth
from django.http import HttpResponse, Http404
# Create your views here.
def staffuploadfiles(request):
    mydata=MyFileUpload.objects.all()
    myform = MyFileForm()
    context={'form':myform}
    #return render(request,'index.html',context)
    if mydata!='':
        context={'form':myform,'mydata':mydata}
        return render(request,'index.html',context)
    else:
        context={'form':myform}
        return render(request,'index.html',context)

def uploadfile(request):    
    if request.method == "POST":
        myform=MyFileForm(request.POST,request.FILES)
        if myform.is_valid():
            MySubjectName = request.POST.get('subject_name')
            MyFile=request.FILES.get('file')

            exists=MyFileUpload.objects.filter(subject_Name=MySubjectName,my_file=MyFile).exists()

            if exists:
                messages.error(request,"The file already exists...!!")
            else:
                MyFileUpload.objects.create(subject_Name=MySubjectName,my_file=MyFile).save()
                messages.success(request,"File Uploaded Successfully.")
        return redirect ("staffuploadfiles")
    
# students download portal
from .models import MyFileUpload

def downloadfiles(request):
    mydata=MyFileUpload.objects.all()
    myform = MyFileForm()
    context={'mydata':mydata}
    
    return render(request,'download.html',context)
def getuploadfile(request):    
    if request.method == "POST": 
        mydata=MyFileUpload.objects.all()    
    return redirect ("downloadfiles")

    
def deletefile (request,id):
    mydata=MyFileUpload.objects.get(id=id)
    mydata.delete()
    os.remove(mydata.my_file.path)
    messages.success(request,"File Deleted Successfully.")
    return redirect('staffuploadfiles')
def sturegister (request):
    if request.method == "POST":
        name = request.POST['name']
        school_name = request.POST["school_name"]
        username = request.POST["rollno"]
        email=request.POST["email"]
        password=request.POST["password"]
        confirm_password=request.POST["confirm_password"]
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info (request,'Rollno is already exists')
                return redirect ('stureg')
            else:
                user=User.objects.create_user(username=username, password=password,email=email)
                user.save()
                messages.success(request,"Your account has been created successfully")
                return redirect('stu_login')


        else:
            messages.info(request,"Passwords doesn't match")
            return redirect ('stureg')
    return render(request,'stu_reg.html')
    

def stulogin (request):
    if request.method =="POST":
        username=request.POST['rollno']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect ('downloadfiles')
        else:
            messages.info(request,"Invalid Rollno or Password")
            return redirect('stu_login')
        
    else:
        return render(request,'stu_login.html')


def staffregister (request):
    if request.method == "POST":
        name = request.POST['name']
        school_name = request.POST["school_name"]
        username = request.POST["id"]
        email=request.POST["email"]
        password=request.POST["password"]
        confirm_password=request.POST["confirm_password"]
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info (request,'Staff Id is already exists')
                return redirect ('staffreg')
            else:
                user=User.objects.create_user(username=username, password=password,email=email)
                user.save()
                messages.success(request,"Your account has been created successfully")
                return redirect('stafflogin')


        else:
            messages.info(request,"Passwords doesn't match")
            return redirect ('staffreg')
    
    return render (request,'staff_reg.html')

def stafflogin (request):
    if request.method =="POST":
        username=request.POST['id']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect ('staffuploadfiles')
        else:
            messages.info(request,"Invalid Staff Id or Password")
            return redirect('stafflogin')
        
    else:
        return render (request,'staff_login.html')