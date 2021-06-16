import json
import logging
import time
import uuid
from datetime import datetime

from django.contrib.auth import login as auth, logout as logoutdj
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.urls import reverse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .forms import KiposUserCreationForm
from .models import KiposUser, Module

logger=logging.getLogger(__name__)
@csrf_exempt
def check_connection(request):
    if request.method=='POST':
        data=json.loads(request.body)
        if 'uuid' in data and data['uuid']!=-1:
            #logger.log(logging.DEBUG,data['uuid'])
            return HttpResponse(not Module.objects.get(uuid=data['uuid']).forced_local_mode)
    return HttpResponse(False)

@csrf_exempt
def update(request):
    if request.method=='POST':
        data=json.loads(request.body)
        if 'uuid' in data and data['uuid']!=-1:
            changed=False
            module=Module.objects.get(uuid=data['uuid'])
            #logger.log(logging.DEBUG, data)
            if 'telemetry' in data:
                changed=True
                module.telemetry=data['telemetry']

            if 'settings' in data:
                if 'last_update_time' in data['settings']:
                    if data['settings']['last_update_time']==-1:
                        module.settings=data['settings']
                        module.settings['last_update_time']=int(time.time())
                        changed=True
                    if module.settings['last_update_time']<data['settings']['last_update_time']:
                        module.settings=data['settings']
                        changed=True

            if 'forced_local_mode' in data:
                module.forced_local_mode=data['forced_local_mode']
                changed=True

            if changed:
                module.save()
            data=json.dumps(module.settings)
            return HttpResponse(content = bytes(data,'ASCII'))
        return HttpResponse('No uuid in content')
    return HttpResponse('Wrong method')

def deletemodule(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            try:
                Module.objects.get(uuid=request.POST['uuid']).delete()
            except:
                return HttpResponse('failed to delete module')
            return HttpResponse('deleted')
    return HttpResponse()

def addmodule(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            try:
                name=request.POST['name']
                telemetry=request.POST['telemetry']
                settings=request.POST['settings']
                last_update=time.time()
            except:
                return HttpResponse('404')
            id=uuid.uuid4()
            Module.objects.create(user=request.user,last_update=last_update,uuid=id,name=name,telemetry=telemetry,settings=settings)
            return HttpResponse('200',content = f'{{uuid:{id}}}' )
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
