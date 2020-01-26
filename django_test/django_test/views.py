from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.response import Response
from django_test.serializers import (
    UserSerializer,
    GroupSerializer,
    SchoolSerializer,
    StudentSerializer,
    DisplayStudentSerializer,
)
from django_test.models import School, Student


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class MultiSerializerViewSetMixin(viewsets.ModelViewSet):
    def get_serializer_class(self):
        """
        Look for serializer class in self.serializer_action_classes, which
        should be a dict mapping action name (key) to serializer class (value),
        i.e.:

        class MyViewSet(MultiSerializerViewSetMixin, ViewSet):
            serializer_class = MyDefaultSerializer
            serializer_action_classes = {
               'list': MyListSerializer,
               'my_action': MyActionSerializer,
            }

            @action
            def my_action:
                ...

        If there's no entry for that action then just fallback to the regular
        get_serializer_class lookup: self.serializer_class, DefaultSerializer.

        """
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super(MultiSerializerViewSetMixin, self).get_serializer_class()


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class StudentViewSet(MultiSerializerViewSetMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    serializer_action_classes = {
        "list": DisplayStudentSerializer,
        "retrieve": DisplayStudentSerializer,
        "create": StudentSerializer,
    }

    def get_queryset(self):
        school_id = self.kwargs.get("school_pk")

        return (
            Student.objects.filter(school=school_id)
            if school_id is not None
            else self.queryset
        )

    # def list(self, request, school_pk=None, *args, **kwargs):
    #     # students = self.queryset.filter(school_id=school_pk)
    #     # return Response(students)

    #     return super(StudentViewSet, self).list(self, request, *args, **kwargs)
