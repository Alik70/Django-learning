from django.urls import path
from .views import SignupPageView

urlpatterns = [
    path('singup/', SignupPageView.as_view(), name='signup'),

]
