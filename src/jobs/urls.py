from django.urls import path

from jobs.views import IndexJobsListView, JobDetailView

urlpatterns = [
    path("", IndexJobsListView.as_view(), name="jobs"),
    path("<int:pk>/", JobDetailView.as_view(), name="job"),
]
