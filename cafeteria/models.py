from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class cafes(models.Model):
     CATEGORY_CHOICES=[
        (1,"cafe"),
        (2,"club"),
        (3,"Restaurant")
    ]
     name=models.CharField(max_length=100)
     detail=models.CharField(max_length=400)
     address=models.CharField(max_length=100)
     place=models.CharField(max_length=100)
     category=models.IntegerField(choices=CATEGORY_CHOICES)
     rating=models.FloatField()
     contact=models.IntegerField()
     image=models.ImageField(upload_to='images')
     cusine=models.CharField(max_length=200)
     def __str__(self):
      return self.name    
     
class jain(models.Model):   
     CATEGORY_CHOICES=[
        (1,"cafe"),
        (2,"club"),
        (3,"Restaurant")
    ]
     name=models.CharField(max_length=100)
     detail=models.CharField(max_length=400)
     address=models.CharField(max_length=100)
     place=models.CharField(max_length=100)
     category=models.IntegerField(choices=CATEGORY_CHOICES)
     rating=models.FloatField()
     contact=models.IntegerField()
     image=models.ImageField(upload_to='images')
     cusine=models.CharField(max_length=200)
     def __str__(self):
      return self.name

class sweet(models.Model):
      CATEGORY_CHOICES=[
        (1,"cafe"),
        (2,"club"),
        (3,"Restaurant")
    ]
      name=models.CharField(max_length=100)
      detail=models.CharField(max_length=400)
      address=models.CharField(max_length=100)
      place=models.CharField(max_length=100)
      category=models.IntegerField(choices=CATEGORY_CHOICES)
      rating=models.FloatField()
      contact=models.IntegerField()
      image=models.ImageField(upload_to='images')
      def __str__(self):
       return self.name
      
class bar(models.Model):
   CATEGORY_CHOICES=[
        (1,"cafe"),
        (2,"club"),
        (3,"Restaurant")
    ]
   name=models.CharField(max_length=100)
   detail=models.CharField(max_length=400)
   address=models.CharField(max_length=100)
   place=models.CharField(max_length=100)
   category=models.IntegerField(choices=CATEGORY_CHOICES)
   rating=models.FloatField()
   contact=models.IntegerField()
   image=models.ImageField(upload_to='images')
   def __str__(self):
       return self.name
   
class place(models.Model):
   CATEGORY_CHOICES=[
        (1,"cafe"),
        (2,"club"),
        (3,"Restaurant")
    ]
   name=models.CharField(max_length=100)   
   detail=models.CharField(max_length=400)
   address=models.CharField(max_length=100)
   place=models.CharField(max_length=100)
   category=models.IntegerField(choices=CATEGORY_CHOICES)
   rating=models.FloatField()
   contact=models.IntegerField()
   image=models.ImageField(upload_to='images')
   def __str__(self):
       return self.name
   
class Wishlist(models.Model):
    uid=models.ForeignKey(User,on_delete = models.CASCADE,db_column="uid",default=1)
    cid=models.ForeignKey(cafes,on_delete =models.CASCADE,db_column="cid",default=1)
    jain = models.ForeignKey(jain, on_delete=models.CASCADE,db_column="jid",default=1)
    sweet = models.ForeignKey(sweet, on_delete=models.CASCADE,db_column="did",default=1 )
    bar = models.ForeignKey(bar, on_delete=models.CASCADE,db_column="rid" ,default=1)
    place = models.ForeignKey(place, on_delete=models.CASCADE,db_column="pid",default=1 )


class list(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE, db_column="uid")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"Wishlist Entry - {self.content_object}"    
   
class visitor(models.Model):
   name=models.CharField(max_length=100)
   contact=models.IntegerField()
   email=models.EmailField()
   visitors=models.IntegerField()   
   date=models.DateTimeField()
   def __str__(self):
      return self.name



         
   
         
   
