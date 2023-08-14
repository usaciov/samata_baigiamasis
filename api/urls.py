from django.urls import path
from . import views


urlpatterns = [
    path('items/', views.getData),
    path('items/add', views.postData),
    path('items/delete/<str:item_id>', views.deleteData),
    path('items/estimate', views.getDataSum),
    path('items/update/<str:item_id>', views.updateData),]
