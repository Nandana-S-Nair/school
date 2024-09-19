from rest_framework import serializers
from .models import Student, Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'subject_name']

class StudentSerializer(serializers.ModelSerializer):
    # subject = SubjectSerializer()  # Ensure subject is nested with details
    
    class Meta:
        model = Student
        fields = ['id', 'student_name', 'grade', 'remarks', 'subject']

    # def create(self, validated_data):
    #     subject_id = validated_data.pop('subject')
    #     print(subject_id)
    #     subject = Subject.objects.get(id=subject_id)  # Get the subject based on the ID
    #     student = Student.objects.create(subject=subject, **validated_data)
    #     return student

    def update(self, instance, validated_data):
        subject_id = validated_data.pop('subject', None)
        if subject_id is not None:
            subject = Subject.objects.get(id=subject_id)
            instance.subject = subject
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
