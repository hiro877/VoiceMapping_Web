from django.urls import path
from . import views

app_name='vmap'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('voice_mapping/', views.VoiceMappingView.as_view(), name="voice_mapping"),
    # path('plot/', views.PlotView.as_view(), name="plot"),
    # path('voice_mapping/plot', views.img_plot, name="img_plot"),
]
