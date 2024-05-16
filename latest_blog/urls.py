from django.urls import path
from latest_blog import views

urlpatterns = [
    path('', views.home,)
]
