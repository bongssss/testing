from django.shortcuts import render, redirect
from django.shortcuts import  get_object_or_404, redirect
from django.http.response import HttpResponse
from django.template import loader
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as django_logout
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#from .forms import CustomLoginForm, CustomSignupForm  # Import custom forms if you have defined them


# Create your views here.
def index(request):   # Request handler
   context = {}   # Initialize context dictionary
   # Render index.html with context
   return render(request, 'biblesearch/index.html', context)

#class CustomLoginView(LoginView):
 #   template_name = 'biblesearch/login.html' 

def signup(request):   # Request handler
   context = {}   # Initialize context dictionary
   # Render index.html with context
   return render(request, 'biblesearch/signup.html', context)

def login(request):
   if request.method == 'POST':
       email = request.POST["inputEmail"]
       password = request.POST['inputPassword']
       user = authenticate(email, password)
       #print("client.id",client.pk)
       if user is not None:
          request.session['userId'] = user.pk
          return redirect('home')
       elif user is None:
          messages.error(request,"Invalid Email or Password")
       return render(request, 'biblesearch/login.html')
    
   else:
     #return render(request, 'biblesearch/login.html')
   
      return LoginView.as_view(template_name='biblesearch/login.html')(request)

def authenticate(email,password):
   try:
      user = Users.objects.get(email=email)
      if user.password == password:
         return user
   except Users.DoesNotExist:
      return None


def home(request):   # Request handler
   context = {}   # Initialize context dictionary
   # Render index.html with context
   return render(request, 'biblesearch/home.html', context)
