from django.urls import path
# from . import views
from .views import HomeView, postdetailsview,addpostview,form_submit

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', postdetailsview.as_view(), name='postdetails'),
    path('addpost/', addpostview.as_view(), name='addpost'),
    path('submit/', form_submit, name='form_submit'),
]