from django.urls import path
from first_app import views

app_name = 'first_app'

urlpatterns = [
    path('', views.index, name='first_app'),
    #path('formpage/', views.from_name_view, name='form_name'),
    path('formpage/', views.users, name='form_name'),
]