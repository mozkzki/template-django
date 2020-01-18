from django.urls import path

from event import views

app_name = "event"
urlpatterns = [
    path('', views.index, name='index'),
    path('table/', views.table, name="table"),
]
