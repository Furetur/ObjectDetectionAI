from django.urls import path

from ObjectDetection.views import index

urlpatterns = [path("", index, name="index")]
