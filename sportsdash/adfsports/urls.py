from django.urls import path
from adfsports import views
from django.views.generic import TemplateView


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
]
