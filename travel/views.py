from django.shortcuts import render
from .models import Dest
import random


def index(request):

	
	dests=Dest.objects.all()
	L=[]
	length=len(dests)
	for dest in dests:
		i=random.randint(0,1)
		if i==1:
			L.append(dest)
    
	

	






	return render(request,'index.html',{'dests':L})

# Create your views here.
