from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('form/',views.form_view)
]
