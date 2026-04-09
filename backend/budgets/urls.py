from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BudgetViewSet, GoalViewSet

router = DefaultRouter()
router.register(r'', BudgetViewSet, basename='budget')
router.register(r'goals', GoalViewSet, basename='goal')

urlpatterns = [
    path('', include(router.urls)),
]