from django.urls import path

from app.models import Products
from .views import Workerdetail,Companies,Products,Product,HeadQ,Area,Shop,SuperheadQ
app_name="app"
urlpatterns = [
    path("",Workerdetail,name="work"),
    path("",Companies,name="companies"),
    path("",Products,name="products"),
    path("",Product,name="product"),
    path("",HeadQ,name="headq"),
    path("",Area,name="area"),
    path("",Shop,name="shop"),
    path("",SuperheadQ,name="super")
]
