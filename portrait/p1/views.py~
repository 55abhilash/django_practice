from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from p1.models import posts
from p1.models import log
from django.contrib.auth import hashers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import datetime
import salt.client
import json
# Create your views here.

def index(request):
    if(request.method=='POST'):
        return HttpResponse("INSERTED")
        preq = request.POST.get('postid')
        if(preq == '1'): 
            local = salt.client.LocalClient()
            x = local.run_job('*', 'cmd.run', ['ls'])
            return HttpResponse(json.dumps(x))
        elif(preq == '2'):
            x = posts(author="abc", title="tit", bodytext="alsjkdfl", timestamp=datetime.date(1995, 2, 2))
            x.save()
            return HttpResponse("INSERTED")
    return render(request, 'index.html')

def login_1(request):
    if(request.method=='POST'):
        all_entries = log.objects.all() 
# all_entries is a query set. We have to iterate over a query set in order
# to access each entry in the database table.
        t = log(user="abhi", pwd=hashers.make_password('abhi'))
        t.save()
        for entry in all_entries :
# entry.user -> access the value of column 'user' in the entry.
            if(request.POST.get('user') == entry.user):
                if(hashers.check_password(request.POST.get('pwd'), entry.pwd)):
                    redirect('http://localhost/')
                else :
                    return HttpResponse("WRONG PASSWORD")
        return HttpResponse("USER NOT FOUND")
# not a post request, i.e. just the login.html url is typed         
    else :
        return render(request, 'login.html')

def login_portrait(request):
    if(request.method=='POST'):
        User.objects.create_user("abhi", "abhilashmhaisne@gmail.com", "abhi")
        user = authenticate(username=request.POST.get('user'), password=request.POST.get('pwd'))
        if(user is not None):
            login(request, user)
            resp = {'status' : '0', 'url' : 'http://localhost/'}
            return HttpResponse(json.dumps(resp), content_type = 'application/json')
        else :
            resp = {'status' : '1', 'message' : 'Invalid Credentials'}
            return HttpResponse(json.dumps(resp), content_type = 'application/json')
    else :
        return render(request, 'login.html')
