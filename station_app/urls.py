from django.urls import path
from . import views

urlpatterns = [
    path('<int:station_id>/media/', views.get_station_media, name='station_media'),
    path('<int:station_id>/slider/', views.station_media_slider, name='station_media_slider'),
    path('stream/video/<path:video_path>/', views.stream_video, name='stream_video'),
    path('stream/pdf/<path:pdf_path>/', views.stream_pdf, name='stream_pdf'),
    path('<int:station_id>/updates/', views.get_station_media_updates, name='station_updates'),


]