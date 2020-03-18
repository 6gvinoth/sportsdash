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