from django.shortcuts import render
from django.http import HttpResponse
from p1.models import posts
import salt.client
import json
# Create your views here.

def index(request):
    if(request.method=='POST'):
        if(request.POST['postid'] == '1'):
            local = salt.client.LocalClient()
            x = local.run_job('*', 'cmd.run', ['sleep 5 && echo output'])
            y = local.get_cli_returns(x['jid'], x['minions'])
        else if( request.POST['postid'] == '2'):

    return render(request, 'index.html')
