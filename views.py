from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Student, Subject
from .serializers import StudentSerializer, SubjectSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    print()
    serializer_class = StudentSerializer

def create(self, request, *args, **kwargs):
    subject_id = request.data.get('subject')
    print("fgdhfhgj")
    
    try:
        # Check if the subject exists
        subject = Subject.objects.get(id=subject_id)
        print("Subject ID:", subject_id)
    except Subject.DoesNotExist:
        return Response(
            {'error': 'Subject matching query does not exist.'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Prepare the student data
    student_data = {
        'student_name': request.data.get('student_name'),
        'grade': request.data.get('grade'),
        'remarks': request.data.get('remarks'),
        'subject': subject.id  # Pass the subject instance or ID
    }
    
    # Use the serializer to validate and save the student data
    serializer = StudentSerializer(data=student_data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def destroy(self, request, *args, **kwargs):
    # Retrieve the student instance by the provided ID
    try:
        student = self.get_object()
        student.delete()
        return Response({"message": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except Student.DoesNotExist:
        return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
    def update(self, request, *args, **kwargs):
        # Custom logic (if any) for PUT (update)
        return super().update(request, *args, **kwargs)

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    def create(self, request, *args, **kwargs):
        # Custom logic (if any) for POST (create)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        # Custom logic (if any) for PUT (update)
        return super().update(request, *args, **kwargs)


