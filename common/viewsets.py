from rest_framework import viewsets, exceptions

from common.models import PersonAddress
from common.serializers import PersonAddressSerializer, PersonAddressCreateSerializer, PersonAddressUpdateSerializer
from people.models import User


class PersonAddressViewset(viewsets.ModelViewSet):

    def get_queryset(self):
        if getattr(self, "swagger_fake_view", False):
            return None # Return nothing on swagger generation request
        person = User.objects.filter(id=self.kwargs['user_pk'])
        if not person:
            raise exceptions.NotFound('Person nort found.')
        queryset = PersonAddress.objects.filter(person=self.kwargs['user_pk'])
        return queryset

    def get_serializer_class(self):
        if self.action == 'create':
            return PersonAddressCreateSerializer
        if self.action in ['update', 'partial_update']:
            return PersonAddressUpdateSerializer
        return PersonAddressSerializer