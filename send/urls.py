
from django.urls import path
from . import views


urlpatterns = [

    path('sendmail/', views.EmailSendView.as_view(), name='emailsend'),
]