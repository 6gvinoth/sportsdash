from django.shortcuts import render

# Create your views here.
def adfsports(request):
    return render(request, 'adfsports.html', {})

def teams(request):
	return render(request,'teams.html',{})