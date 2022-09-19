from django.shortcuts import redirect, render
from.models import Post
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def index(request):
    posts=Post.objects.all()
    return render(request,'index.html',{'posts':posts})

def post(request,pk):
    posts=Post.objects .get(id=pk)
    return render(request,'posts.html',{'posts':posts})
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['Password']
        password2=request.POST['Password2']

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Exists')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Password Not The Same')
            return redirect('register')
            
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password= request.POST['password']

        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('')
        else:
            messages.info(request,'Credentials Invalid')
            return redirect('Login')
    else:
        return render(request,'login.html')


    

        

            


    
    