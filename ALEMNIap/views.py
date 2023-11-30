import statistics
from rest_framework import viewsets, status
from rest_framework.response import Response
from ALEMNIap import serializers
from ALEMNIap import models

from .models import (
    User,
    Course,
    Enrollment,
    Material,
    Assignment,
    Submission,
    Grade,
    InteractionHistory,
    ReadingState,
)

from .serializers import (
    UserSerializer,
    CourseSerializer,
    EnrollmentSerializer,
    MaterialSerializer,
    AssignmentSerializer,
    SubmissionSerializer,
    GradeSerializer,
    InteractionHistorySerializer,
    ReadingStateSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    
class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    
class InteractionHistoryViewSet(viewsets.ModelViewSet):
    queryset = InteractionHistory.objects.all()
    serializer_class = InteractionHistorySerializer
    
class ReadingStateViewSet(viewsets.ModelViewSet):
    queryset = ReadingState.objects.all()
    serializer_class = ReadingStateSerializer
   