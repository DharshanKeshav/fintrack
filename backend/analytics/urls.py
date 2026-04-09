from django.urls import path
from .views import SummaryView, CategoryBreakdownView

urlpatterns = [
    path('summary/', SummaryView.as_view(), name='summary'),
    path('by-category/', CategoryBreakdownView.as_view(), name='by-category'),
]
