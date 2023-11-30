from django.db import models
from django.core.validators import RegexValidator

validate_alphanumeric = RegexValidator(
    r'^[a-zA-Z0-9]*$', 
    'Only alphanumeric characters are allowed.'
)
class Roles(models.TextChoices):
    STUDENT='STUDENT','Student'
    TUTOR='TUTOR','Tutor'
    ADMINISTRATOR='ADMIN','Administrator'


class User(models.Model):
    userId = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100,validators=[validate_alphanumeric], default='')
    email = models.EmailField(unique=True)
    dateJoined = models.DateField(auto_now_add=True)
    role = models.CharField(max_length=20, choices=Roles.choices)

    class Meta:
        db_table = 'User'

class Course(models.Model):
    courseId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    enrollmentCapacity = models.IntegerField()
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Course'

class Enrollment(models.Model):
    enrollmentId = models.AutoField(primary_key=True)
    enrollmentDate = models.DateField()
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Enrollment'

class Material(models.Model):
    materialId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    uploadDate = models.DateField(auto_now_add=True)
    documentType = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Material'

class Assignment(models.Model):
    assignmentId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    dueDate = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Assignment'

class Submission(models.Model):
    submissionId = models.AutoField(primary_key=True)
    submissionContent = models.TextField()
    submissionDate = models.DateField(auto_now_add=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Submission'

class Grade(models.Model):
    gradeId = models.AutoField(primary_key=True)
    grade = models.CharField(max_length=10)
    feedback = models.TextField()
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Grade'

class InteractionHistory(models.Model):
    interactionId = models.AutoField(primary_key=True)
    interactionType = models.CharField(max_length=50)
    interactionDate = models.DateField()
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)

    class Meta:
        db_table = 'InteractionHistory'

class ReadingState(models.Model):
    readingStateId = models.AutoField(primary_key=True)
    readState = models.IntegerField()
    lastReadDate = models.DateField()
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)

    class Meta:
        db_table = 'ReadingState'
