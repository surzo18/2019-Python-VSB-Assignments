import datetime
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

# Create your models here.
class Actor(models.Model):
    actor_name = models.CharField(max_length = 50,  null=False)
    age = models.IntegerField(default = 0) 
    description = models.TextField(max_length = 500, default = "Description is unknown")
    #films_names = models.ManyToManyField(Film, on_delete=models.CASCADE) #Co Default
    image_link = models.CharField(max_length= 500, default= "https://vignette.wikia.nocookie.net/kongregate/images/9/96/Unknown_flag.png/revision/latest?cb=20100825093317")
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.actor_name

class Genre(models.Model):
    genre_name= models.CharField(max_length = 20, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.genre_name

    

class Film(models.Model): # pridat k cudzim klucom on_delete=models.CASCADE
    film_name = models.CharField(max_length = 50, null=False )
    year_of_release= models.IntegerField(default = 0, validators=[MaxValueValidator(datetime.datetime.now().year + 5) , MinValueValidator(0)]) # MAX A MIN ??
    country=models.CharField(max_length = 20 , default = "Unknown") 
    genres = models.ManyToManyField(Genre)#, on_delete=models.CASCADE #Co Default
    actors = models.ManyToManyField(Actor)#, on_delete=models.CASCADE #Co Default 
    description = models.TextField(max_length = 500, default = "This description is not added yet")
    poster = models.CharField(max_length = 50, default = "images/unknown.png") # defaultna adresa na img  #spýtať sa
    #stars = models.ForeignKey(Star,on_delete=models.CASCADE,)  #co Default
    created_at = models.DateTimeField(auto_now_add=True)
    image_link1 = models.CharField(max_length = 500, default = "https://vignette.wikia.nocookie.net/kongregate/images/9/96/Unknown_flag.png/revision/latest?cb=20100825093317")
    image_link2 = models.CharField(max_length = 500, default = "https://vignette.wikia.nocookie.net/kongregate/images/9/96/Unknown_flag.png/revision/latest?cb=20100825093317")
    image_link3 = models.CharField(max_length = 500, default = "https://vignette.wikia.nocookie.net/kongregate/images/9/96/Unknown_flag.png/revision/latest?cb=20100825093317")

    
    def __str__(self):
        return self.film_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Comment(models.Model):
    Comment= models.TextField(max_length = 1000 , null = False)
    film_name= models.ForeignKey(Film, on_delete=models.CASCADE)   #, null = False
    user= models.CharField(max_length = 30, null = False) #Nastavit ako cudzi kluc z Users alebo zadať
    created_at = models.DateTimeField(auto_now_add=True)
    
class Star(models.Model):
    film_name= models.ForeignKey(Film,on_delete=models.CASCADE,  null = False) #,on_delete=models.CASCADE #co Default
    user = models.CharField(max_length = 30,  null = False)#Nastavit ako  cudzi kluc z users
    value = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)], null = False) #nastaviť max na 5 min na 0
    created_at = models.DateTimeField(auto_now_add=True)

    def filmName(self):
        return self.film_name

