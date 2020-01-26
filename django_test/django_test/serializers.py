from django.contrib.auth.models import User, Group
from django_test.models import School, Student
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ["name", "max_students"]


class StudentSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        school_chosen = validated_data["school"]
        number_of_student = Student.objects.filter(school_id=school_chosen.id).count()

        if number_of_student >= school_chosen.max_students:
            raise Exception("Already too many students in this school")

        return super(StudentSerializer, self).create(validated_data)

    class Meta:
        model = Student
        fields = ["id", "first_name", "last_name", "school"]


class DisplayStudentSerializer(StudentSerializer):
    class Meta:
        model = Student
        fields = StudentSerializer.Meta.fields + ["identification"]
