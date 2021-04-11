from django.shortcuts import render
from django.http import HttpResponse
from .models import Player

def index(request):
	playerdata = Player.objects.all()
	posfilter = request.GET.get('pos-filter')
	q1 = Player.objects.filter(main_position=posfilter)
	print(q1)
	return render(request,'index.html',locals())