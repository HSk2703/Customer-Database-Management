# customer360/urls.py

from django.contrib import admin
from django.urls import path
from . import views  # Import views from the same app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),  # Root URL
    path('create/', views.create_customer, name='create_customer'),  # URL for creating customers
    path('interact/<int:cid>', views.interact, name='interact'),  # URL for interacting with a customer
    path('summary/', views.summary, name='summary'),  # URL for viewing interaction summary
]
