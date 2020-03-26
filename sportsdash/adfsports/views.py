from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
import json
from .models import TeamScore
from django.views.decorators.csrf import csrf_exempt
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

@csrf_exempt
def teamsscoreapi(request):
    
    body = json.loads(request.body.decode("utf-8"))
    TeamMatch = body.get("TeamMatch", "")
    Sports = body.get("Sports", "")
    Point = body.get("Point", "")
    Wonby = body.get("Wonby", "")
    Lossby = body.get("Lossby", "")
    print(body)
    # import pdb;pdb.set_trace()
    if TeamMatch == "" or Sports == "" or Point == "" or Wonby == "" or Lossby == "" :
        result = {"success": False, "message": "Please Fill All The Fields"}
        return JsonResponse(result)
    else:
        try:    	
            TeamScore.objects.create(TeamMatch=TeamMatch,Sports=Sports,Point=Point,Wonby=Wonby,Lossby=Lossby,)
            result = {"success": True, "message": "Successfully Done "}
            return JsonResponse(result)
        except:
            result = {"success": True, "message": "Sql Error Check your Input "}
            return JsonResponse(result)
def teamsscore(request):
	return render(request,'teamsscore.html',{})	