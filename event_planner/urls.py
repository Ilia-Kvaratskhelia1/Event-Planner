
from django.contrib import admin
from django.urls import path, reverse
from events import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index ),
    path('event/<str:title>/', views.events_detail, name='detail'),
]

