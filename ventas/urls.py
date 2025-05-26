from django.urls import path
from .views import prediccion_view

urlpatterns = [
    path('', prediccion_view, name='prediccion'),
]
