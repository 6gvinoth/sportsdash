from django.urls import path
from adfsports import views
from django.views.generic import TemplateView
from django.conf.urls import url


urlpatterns = [
    # path('', views.adfsports, name='adfsports'),
    path('', TemplateView.as_view(template_name='base.html')),
    path('teams/', TemplateView.as_view(template_name='teams.html')),
    path('pointsystems/', TemplateView.as_view(template_name='pointsystems.html')),
    path('schedule/', TemplateView.as_view(template_name='schedule.html')),
    path('cricketrules/', TemplateView.as_view(template_name='cricket_rules.html')),
    path('counterstrike/', TemplateView.as_view(template_name='counterstrike.html')),
    path('football/', TemplateView.as_view(template_name='football.html')),
    path('carrom/', TemplateView.as_view(template_name='carrom.html')),
    path('bvscm2/', TemplateView.as_view(template_name='bvscm2.html')),
    path('avscm3/', TemplateView.as_view(template_name='avscm3.html')),
    path('avsbm1/', TemplateView.as_view(template_name='avsbm1.html')),
path('cricketdash/', TemplateView.as_view(template_name='cricketdash.html')),
url("teamsscoreapi/", views.teamsscoreapi, name="teamsscore"),
path('teamsscore/', TemplateView.as_view(template_name='teamsscore.html')),
]
