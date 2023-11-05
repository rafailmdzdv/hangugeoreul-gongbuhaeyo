"""URLs mappings for days application."""
from django.urls import path

from server.apps.days import views

app_name = 'days'

urlpatterns = (
    path('all/', views.StudyDayListView.as_view()),
)
