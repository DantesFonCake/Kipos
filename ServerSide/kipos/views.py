from django.contrib.auth import login as auth, logout as logoutdj
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from django.template import RequestContext
from django.urls import reverse
from django.views import View

from .forms import KiposUserCreationForm
from .models import KiposUser, Module


def addmodule(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            try:
                name=request.POST['name']
                telemetry=request.POST['telemetry']
                settings=request.POST['settings']
            except:
                return HttpResponse('404')
            Module.objects.create(user=request.user,name=name,telemetry=telemetry,settings=settings)
            return HttpResponse('200')
    return render(request,'kipos/moduleaddform.html')



def allmodules(request):
    if request.user.is_authenticated:
        return render(request,'kipos/modulelist.html',context = {'module_list':Module.objects.filter(user=request.user),
                                                                 'authed':'yes'})
    else:
        url = reverse('kipos:main')
        return HttpResponseRedirect(url)

def logout(request):
    logoutdj(request)
    return render(request, 'kipos/index.html')


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            form.clean()
            auth(request, form.user_cache, backend = 'django.contrib.auth.backends.ModelBackend')
            url = reverse('kipos:main')
            return HttpResponseRedirect(url)
        else:
            return render(request, 'kipos/login.html', context = {'form': form})
    return render(request, 'kipos/login.html', context = {'form': AuthenticationForm()})


def register(request):
    if request.method == 'POST':
        form = KiposUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            if len(KiposUser.objects.filter(username = username)) > 0:
                return render(request, 'kipos/register.html',
                              context = {'error': 'User with this username already exist'})
            email = form.cleaned_data.get('email')
            if len(KiposUser.objects.filter(email = email)) > 0:
                return render(request, 'kipos/register.html', context = {'error': 'User with this email already exist'})
            raw_pass1 = form.cleaned_data.get('password1')
            user = KiposUser.objects.create_user(username, email, raw_pass1)
            auth(request, user, backend = 'django.contrib.auth.backends.ModelBackend')
            url = reverse('kipos:main')
            return HttpResponseRedirect(url)
        else:
            return render(request, 'kipos/register.html', context = {'form': form})
    return render(request, 'kipos/register.html', context = {'form': KiposUserCreationForm()})


class MainView(View):
    def get(self, request):
        return render(request, 'kipos/index.html')
