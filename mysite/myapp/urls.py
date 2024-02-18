from django.urls import path
from .views import indexItem
from .views import index

app_name = 'myapp'

urlpatterns = [
    path('', index),
    path('<int:my_id>/', indexItem, name='detail'),
]