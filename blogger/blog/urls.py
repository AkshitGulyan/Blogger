from django.urls import path
# from . import views
from .views import HomeView, postdetailsview

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>', postdetailsview.as_view(), name='postdetails'),
]