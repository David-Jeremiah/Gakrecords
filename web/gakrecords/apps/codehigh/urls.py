from django.urls import path
from .views import index,about,courses,contact,research,events,notice,teacher,scholarship

app_name = 'codehigh'


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('courses/', courses, name='courses'),
    path('contact/', contact, name='contact'),
    path('research/', research, name='research'),
    path('events/', events, name='events'),
    path('notice/', notice, name='notice'),
    path('teacher/', teacher, name='teacher'),
    path('scholarship/', scholarship, name='scholarship'),
]
