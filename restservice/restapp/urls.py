from django.conf.urls.static import static
from django.urls import path

from restservice import settings
from .views import ObjectAPIView, ObjectAPIDetail

urlpatterns = [
    path('', ObjectAPIView.as_view()),
    path('<str:pk>/', ObjectAPIDetail.as_view()),

]
