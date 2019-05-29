from django.urls import path

from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('films/', views.films, name='films'),
    path('actors/', views.actors, name='actors'),
    path('chart/', views.chart, name='chart'),
    path('about/', views.about, name='about'),
    path('register/', views.RegisterFormView.as_view(), name='register'),
    path('logout/', views.logout_view, name='logout'),



    path('film/<int:film_id>/',views.FilmView.as_view(), name="film"),
    path('actor/<int:actor_id>/',views.actor, name="actor"),
    path('addstar/',views.addStar, name="addStar"),

]


