from django.shortcuts import render
from django.http import HttpResponse
from .models import Player

def index(request):
	playerdata = Player.objects.all()
	return render(request,'index.html',locals())