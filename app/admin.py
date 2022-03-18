from django.contrib import admin
from .models import Workerdetail,Companies,Products,HeadQ,Area,Shop,Product,SuperheadQ
# Register your models here.
admin.site.site_header="ADMIN PANEL"
admin.site.site_title="ADMIN PANEL"



admin.site.register(Workerdetail)
admin.site.register(Companies)
admin.site.register(Products)
admin.site.register(HeadQ)
admin.site.register(Area)
admin.site.register(Shop)
admin.site.register(SuperheadQ)
admin.site.register(Product)