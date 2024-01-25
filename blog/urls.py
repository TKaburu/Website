from django.urls import path
from .views import HomeView, BlogView, PostDetail


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('blog/', BlogView.as_view(), name='blog'),
    path('<slug:slug>', PostDetail.as_view(), name='post-detail'),
]

