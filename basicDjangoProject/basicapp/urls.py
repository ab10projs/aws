from django.urls import path
from . import views
from basicapp.dash_apps.finished_apps import sinpleexampe
urlpatterns = [
path('',views.basicapp, name= 'basicapp')
]