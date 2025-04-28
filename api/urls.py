from django.urls import path
from . import views

urlpatterns = [
    path('upload', views.ImgViewSet),
    path('audio-upload', views.AudioViewSet),
    path('', views.query),
    path('video', views.VideoViewSet),
    path('pdf', views.PdfViewSet),
    path('verify-trxn', views.VerifyTxn)
]