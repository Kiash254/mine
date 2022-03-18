from secrets import choice
from tabnanny import check
from tkinter import CASCADE
from tkinter.tix import Tree
from turtle import ondrag, position
from django.db import models
from numpy import True_, product

# Create your models here.
class Shop(models.Model):
    kiashShop=models.CharField(max_length=200,null=True)
    nomsShop=models.CharField(max_length=255,null=True,blank=True)
    Snaveshop=models.CharField(max_length=200,blank=True,null=True)
    mirriam=models.CharField(max_length=45,null=True,blank=True)
    maathais=models.CharField(max_length=30,null=True)
    def __str__ (self):
        return f'kiashShop{self.kiashShop}'


class SuperheadQ(models.Model):
    all=models.ForeignKey(Shop,on_delete=True)
    maathais=models.CharField(max_length=200,null=True,blank=True)
    Magunas=models.CharField(max_length=200,null=True)
    Tuskeys=models.CharField(max_length=40,null=True,blank=True)
    Leestar=models.CharField(max_length=200,null=True)
    def __str__(self):
        return f'all{self.all}'



class Product(models.Model):
    name=models.CharField(max_length=255,null=True)
    item=models.CharField(max_length=20,null=True,blank=True)
    price=models.CharField(max_length=30,null=True,blank=True)
    vat=models.IntegerField()
    offer=models.IntegerField()
    deliverly=models.CharField(max_length=200,blank=True,null=True)

    def __str__ (self):
        return f'name{self.name}'




class Area(models.Model):
    nairobi=models.CharField(max_length=30,null=True)
    places=models.ForeignKey(Shop,on_delete=CASCADE)
    thika=models.CharField(max_length=200,null=True)
    kisumu=models.CharField(max_length=30,null=True,blank=True)
    mombasa=models.CharField(max_length=30,null=True,blank=True)
    nyeri=models.CharField(max_length=200,null=True,blank=True)
    def __str__ (self):
        return f'places{self.places}'
class HeadQ(models.Model):
    kenya=models.ForeignKey(Shop,on_delete=CASCADE,null=True)
    Usa=models.CharField(max_length=200,null=True)
    ameriaca=models.ForeignKey(Area,on_delete=True)
    time=models.DateTimeField(auto_now_add=True)
    travel_cost=models.IntegerField()

    def __str__ (self):
        return f'kenya{self.kenya}'



class Products(models.Model):
    product=models.ForeignKey(Shop,on_delete=True)
    milk=models.CharField(max_length=200,null=True,blank=True)
    cake=models.CharField(max_length=300,null=True)
    credit=models.IntegerField()
    tissue=models.CharField(max_length=200,null=True,blank=True)
    pen=models.CharField(max_length=20,null=True,blank=True)
    books=models.CharField(max_length=100,null=True)
    gas=models.CharField(max_length=200,null=True,blank=True)
    bulb=models.CharField(max_length=20)
    def __str__ (self):
        return f'product{self.product}'

class Companies(models.Model):
    products=models.ForeignKey(Products,on_delete=True)
    brookside=models.BooleanField(True)
    broadways=models.BooleanField(True)
    safaricom=models.BooleanField(True)
    toilex=models.BooleanField(True)
    bic=models.BooleanField(True)
    nuru_gas=models.BooleanField(True)
    ludan=models.BooleanField(check)

    def __str__ (self):
        return f'products{self.products}'

class Workerdetail(models.Model):
    companies=models.ForeignKey(Companies,on_delete=True)
    firstname=models.CharField(max_length=300,null=True)
    middlename=models.CharField(max_length=200,null=True)
    lastname=models.CharField(max_length=30,null=True)
    phone_number=models.CharField(max_length=30,null=True,blank=True)
    age=models.IntegerField()
    gender=models.CharField(max_length=200,null=True,blank=True)
    position=models.CharField(max_length=30,null=True,blank=True)
    home_place=models.CharField(max_length=200,null=True)
    medical_effects=models.CharField(max_length=200,null=30,blank=True)

    def __str__ (self):
        return f'companies{self.companies}'


