from django.urls import path
from .views import JobCreateAPIView,JobListAPIView,UserTestAPIView

urlpatterns = [
    path('jobs/', JobListAPIView.as_view(),name='job-list'),
    path('jobs/create/',JobCreateAPIView.as_view(),name='job-create'),
    path("test/", UserTestAPIView.as_view(), name="user-test"),
]
