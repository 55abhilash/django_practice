from django.shortcuts import render
from django.http import HttpResponse
from p1.models import posts
#from p1.models import insert
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

def login(request):
    if(request.method=='POST'):
        if(request.POST.get('user') == "abhi"):
            if(request.POST.get('pwd') == "abhi"):
                return HttpResponse("LOGIN SUCCESSFUL")
            else :
                return HttpResponse("WRONG PASSWORD")
        else :
            return HttpResponse("USER NOT FOUND")
    return render(request, 'login.html')
