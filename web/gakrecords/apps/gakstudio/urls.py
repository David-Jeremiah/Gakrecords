from django.urls import path
from .views import home,about,track,contact

app_name = 'gakstudio'


urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('track/', track, name='track'),
    path('contact/', contact, name='contact'),
]
