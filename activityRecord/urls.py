
from django.urls import path
from .views import UsersList

urlpatterns = [
    path('members/',UsersList.as_view()),
]
