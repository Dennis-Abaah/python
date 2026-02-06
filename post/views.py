from django.shortcuts import render, redirect
from django.contrib.auth.models import User , auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from .forms import PostForm

# Create your views here.
def index(request):
    #Get all post from the database , newest first
    all_posts = Post.objects.all().order_by('-created_at')
    return  render(request , 'index.html', {'posts':all_posts })

def register(request):
   if request.method == 'POST' :
     username = request.POST['username']
     email = request.POST['email']
     password = request.POST['password']
     password2 = request.POST['password2']
     
     if password == password2 :
        if User.objects.filter( email=email).exists():
           messages.info(request, "Email Already exists")
           return redirect('register')
        elif User.objects.filter( username=username).exists():
            messages.info(request,"Username already exists")  
            return redirect('register')
        else :
            user = User.objects.create_user(username=username ,email=email , password=password)
            user.save();
            return redirect('login')
     else:
        messages.info(request, 'Password not the same')
        return redirect('register')
   else :
      return render(request , 'register.html')
   
def login(request):
   if request.method == 'POST' :
      username = request.POST['username']
      password = request.POST['password']
      user =auth.authenticate(username=username , password=password)

      if user is not None:
         auth.login(request, user)
         return redirect('index')
      else:
         messages.info(request , 'Invalid Credentials')
         return redirect('login')
   else:
     return render(request , 'login.html')


def logout(request):
   auth.logout(request)
   return redirect('index')

def create_post(request):
   if request.user.is_authenticated:
      if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user 
            post.save()
            return redirect('index')
      else:
         #If user just opened the page give them an empty form
         form = PostForm()
      return render( request , 'create_post.html', {'form':form})
   return render( request , 'create_post.html')

def user_posts(request):
   if request.user.is_authenticated:
        number = Post.objects.filter(author=request.user).count
        user_posts = Post.objects.filter( author=request.user ).order_by('-created_at')
        return render(request, 'user_posts.html', {'user_posts': user_posts ,'number':number})
   return render(request,'user_posts.html' )
