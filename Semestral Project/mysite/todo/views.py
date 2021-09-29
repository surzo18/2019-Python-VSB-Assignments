from django.http import Http404

from django.shortcuts import get_object_or_404,render,redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.db.models import Sum
from collections import OrderedDict
from .models import Film,Actor,Star
from django.views import View
from .forms import RegisterForm, LoginForm , StarForm

from django.contrib.auth import logout

import operator

def logout_view(request):
    logout(request)
    return redirect('todo:login')

class LoginFormView(View):
    form_class= LoginForm
    template_name = 'todo/login.html'

    def get(self, request):
        user=request.user
        if(user.is_authenticated):
            return redirect('todo:index')
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        print(form.errors)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request,username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('todo:index')
        error="Zadal si niečo zle"
        return render(request, self.template_name,{'form':form,'error':error})

class RegisterFormView(View):
    form_class= RegisterForm
    template_name = 'todo/register.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(request,username=username,password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('todo:index')
        return render(request, self.template_name,{'form':form})
# Create your views here. 6views 6 templates 3 forms 3 models
def index(request):
    film = Film.objects.all().order_by('?')[:3]
    actor = Actor.objects.all().order_by('?')[:3]
    context = {
        'film': film,
        'actor': actor
    }
    return render(request, 'todo/index.html',context)
"""
def film(request, film_id):
    form_class=StarForm
    form=form_class(None)
    film = get_object_or_404(Film, pk=film_id)
    return render(request, 'todo/film.html', {'film': film,'form': form})
"""
class FilmView(View):
    form_class=StarForm
    template_name = 'todo/film.html'

    def get(self, request,film_id):
        form = self.form_class(None)
        film = get_object_or_404(Film, pk=film_id)
        return render(request, self.template_name, {'film':film,'form':form})

    
    def post(self, request,film_id):
        user=request.user
        if(not user.is_authenticated):  
            return HttpResponse("Pre hlasovanie sa prihlas")
        form = self.form_class(request.POST)
        film = get_object_or_404(Film, pk=film_id)
        if form.is_valid():
            formular=form.save(commit=False)
            value = form.cleaned_data['star']
            num_results = Star.objects.filter(film_name = film, user=user.username).count()
            if(num_results > 0):
               return HttpResponse("Uz si hlasoval za tento film")
            formular = Star.objects.create(film_name=film,user=user.username,value=value)
            formular.save()
            return render(request, self.template_name, {'film':film,'form':form})
        else:
            return HttpResponse("Nic")

def actor(request, actor_id):
    actor = get_object_or_404(Actor, pk=actor_id)
    films = Film.objects.filter(actors__id=actor_id)
    return render(request, 'todo/actor.html', {'actor': actor, 'films': films})

def about(request):
    return render(request, 'todo/about.html')

def log(request):
        return render(request, 'todo/login.html')

def register(request):
    actor = Actor.objects.all()
    context = {
        'actor': actor
    }
    return render(request, 'todo/register.html',context)

def films(request):
    film = Film.objects.all()
    context = {
        'film': film
    }
    return render(request, 'todo/films.html',context)

def actors(request):
    actor = Actor.objects.all()
    context = {
        'actor': actor
    }
    return render(request, 'todo/actors.html',context)

    
def chart(request):
    #Star.objects.values("film").annotate(Sum("value")) by to zgrouplo podle filmu (snad)
    #Movie.objects.annotate(num_ratings=Count('star')).order_by('-num_ratings')
    #Star.objects.aggregate(Sum('value'))
    films = Star.objects.all()
    dictionary = {}

    for film in films:
        name =film.film_name
        print(film.film_name, " toto je meno")
        if film.film_name not in dictionary:
            dictionary[name] = film.value
            print(film.value)
        else:
            dictionary[name] += film.value
    #Sdictionary = sorted(dictionary, key = lambda x: (-dictionary[x], x))
    context = {
        'film': dictionary
    }
    return render(request, 'todo/chart.html', context)


def addStar(request):
    return render(request, 'todo/login.html')
    
