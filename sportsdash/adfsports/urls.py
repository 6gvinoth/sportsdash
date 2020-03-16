from django.urls import path
from adfsports import views
from django.views.generic import TemplateView


urlpatterns = [
    # path('', views.adfsports, name='adfsports'),
    path('', TemplateView.as_view(template_name='base.html')),
    path('teams/', TemplateView.as_view(template_name='teams.html')),
]
