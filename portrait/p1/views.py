from django.shortcuts import render
from django.http import HttpResponse
from p1.models import posts
from p1.models import insert
import salt.client
import json
# Create your views here.

def index(request):
    if(request.method=='POST'):
        preq = request.POST.get('postid', False)
        if(preq == '1'):
            local = salt.client.LocalClient()
            x = local.run_job('*', 'cmd.run', ['ls'])
            y = local.get_cli_returns(x['jid'], x['minions'])
            return response(request, 'index.html', json.dumps(y))
        elif(preq == '2'):
            insert()
            return response(request, 'index.html', "INSERTED")
    return render(request, 'index.html')
