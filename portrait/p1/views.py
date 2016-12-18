from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from p1.models import posts
from p1.models import log
from django.contrib.auth import hashers
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
        all_entries = log.objects.all() 
# all_entries is a query set. We have to iterate over a query set in order
# to access each entry in the database table.
        t = log(user="abhi", pwd=hashers.make_password('abhi'))
        t.save()
        for entry in all_entries :
# entry.user -> access the value of column 'user' in the entry.
            if(request.POST.get('user') == entry.user):
                if(hashers.check_password(request.POST.get('pwd'), entry.pwd)):
                    return redirect('http://localhost/')
                else :
                    return HttpResponse("WRONG PASSWORD")
        return HttpResponse("USER NOT FOUND")
            
    else :
        return render(request, 'login.html')
