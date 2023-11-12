from django.urls import path
from . import views

app_name='storeapp'
urlpatterns = [
    # path('',views.index,name='index')
    path('',views.allProdCat,name='allProdCat'),
    path('home/<slug:c_slug>/',views.allProdCat,name='product_by_cat'),
    path('<slug:c_slug>/<slug:product_slug>/',views.Prodetail,name='ProCatdetail'),
]
