from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate
from . models import User
from . forms import Registration
# Create your views here.

def services(request):
    #context={'services':'active'}
    return render(request,'app/services.html')

def skill(request):
    #context={'skill':'active'}
    return render(request, 'app/skill.html')

def home(request):
    #posts=Post.objects.all()
    return render(request, 'app/home.html')

#def contact(request):
#    return render(request, 'app/contact.html')

def contact(request):
    
    if request.method=='POST':
        fm=Registration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            sb=fm.cleaned_data['subject']
            ms=fm.cleaned_data['message']
            reg=User(name=nm, email=em, subject=sb, message=ms)
            reg.save()
            messages.success(request, 'Your message has sent successfully.')
            fm=Registration()
            
    else:
        fm=Registration()
    stud=User.objects.all()
    return render(request, 'app/contact.html',{'form':fm, 'stu':stud})
