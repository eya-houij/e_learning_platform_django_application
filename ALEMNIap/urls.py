from rest_framework import routers
from django.urls import path, include
from .views import (
    UserViewSet,
    CourseViewSet,
    EnrollmentViewSet,
    MaterialViewSet,
    AssignmentViewSet,
    SubmissionViewSet,
    GradeViewSet,
    InteractionHistoryViewSet,
    ReadingStateViewSet,
)

# Get the reference to the default router defined in the rest_framework for ModelViewSets
router = routers.DefaultRouter()

# Register ViewSets with the router
router.register(r'users', UserViewSet, basename='users')
router.register(r'courses', CourseViewSet, basename='courses')
router.register(r'enrollments', EnrollmentViewSet, basename='enrollments')
router.register(r'materials', MaterialViewSet, basename='materials')
router.register(r'assignments', AssignmentViewSet, basename='assignments')
router.register(r'submissions', SubmissionViewSet, basename='submissions')
router.register(r'grades', GradeViewSet, basename='grades')
router.register(r'interactionhistory', InteractionHistoryViewSet, basename='interactionhistory')
router.register(r'readingstate', ReadingStateViewSet, basename='readingstate')

# Include the router URLs in the main urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]
