from django.urls import path

from .views import getUserProfile, HelloView

urlpatterns = [
    path("profile/", getUserProfile, name="user-profile"),
    path("hello/", HelloView.as_view(), name="hello"),
]
