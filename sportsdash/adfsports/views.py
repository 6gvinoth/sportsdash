from django.shortcuts import render

# Create your views here.
def adfsports(request):
    return render(request, 'adfsports.html', {})

def teams(request):
	return render(request,'teams.html',{})

def pointsystems(request):
	return render(request,'pointsystems.html',{})

def schedule(request):
	return render(request,'schedule.html',{})

def cricketrules(request):
	return render(request,'cricket_ruless.html',{})

def counterstrike(request):
	return render(request,'counterstrike.html',{})

def football(request):
	return render(request,'football.html',{})	

def carrom(request):
	return render(request,'carrom.html',{})	

def bvscm2(request):
	return render(request,'bvscm2.html',{})	

def avsbm1(request):
	return render(request,'avsbm1.html',{})	

def cricketdash(request):
	return render(request,'cricketdash.html',{})	
