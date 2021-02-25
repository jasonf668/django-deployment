from django.urls import path
import main_app.views as views
from .views import *

urlpatterns = [
    path('ads.txt', AdsView.as_view()),
    path('random_porn', views.random_porn),
    path('random_star', views.random_star),
    path('from_category', views.from_category),
    path('fuq', views.fuq)

]
