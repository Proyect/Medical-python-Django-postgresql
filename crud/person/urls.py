from django.urls import path
from .views import PersonListCreateAPIView

urlpatterns = [ 
    path('persons/', PersonListCreateAPIView.as_view(), name='product-list-create'),
]