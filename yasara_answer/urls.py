from django.contrib import admin
from django.urls import path, include
from . import views
from .router import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('scoreboard/', views.scoreboard, name='index'),
    path('team/', views.team, name='team'),
    path('player/', views.player, name='player'),
    path('coach/', views.coach, name='coach'),
    path('api/', include(router.urls))
]
