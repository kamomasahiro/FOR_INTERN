from django.shortcuts import render
from django.http import HttpResponse
from .models import Member, Message
from .forms import MemberForm, MessageForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def index(request):
    params = {
        'title': 'Welcome to Folia',
        'msg': 'index',
        'schedule': 'schedule',
        'map': 'map',
        'message': 'message',
        'trainer': 'trainer',
    }
    return render(request, 'hello/index.html', params)

def schedule(request):
    params = {
        'title': 'Wagou Store Schedule',
        'msg': 'スケジュール',
        'index': 'index',
    }
    return render(request, 'hello/schedule.html', params)

def map(request):
    params = {
        'title': 'Folia Store Map',
        'msg': '地図',
        'index': 'index',
    }
    return render(request, 'hello/map.html', params)

def message(request, page=1):
    if (request.method == 'POST'):
        obj = Message()
        form = MessageForm(request.POST, instance=obj)
        form.save()
    data = Message.objects.all().reverse()
    paginator = Paginator(data, 7)
    params = {
        'title': 'Message',
        'form': MessageForm(),
        'data': paginator.get_page(page),
    }
    return render(request, 'hello/message.html', params)

@login_required(login_url='/admin/login/')
def trainer(request):
    params = {
        'title': 'For Trainer',
        'msg': '指導薬剤師用',
        'index': 'index',
    }
    return render(request, 'hello/trainer.html', params)



