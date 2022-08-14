from rest_framework import serializers

from common. models import PersonAddress
from people.models import User


class PersonAddressSerializer(serializers.ModelSerializer):
    person = serializers.SerializerMethodField()

    class Meta:
        model = PersonAddress
        fields = '__all__'

    def get_person(self, address: PersonAddress):
        return address.person.id

    def get_is_default(self, address: PersonAddress):
        return address.is_dafault


class PersonAddressCreateSerializer(PersonAddressSerializer):
    class Meta:
        model = PersonAddress
        exclude = ['is_default']

    def create(self, validated_data):
        user_pk = self.context['request'].parser_context['kwargs']['user_pk']
        validated_data['person'] = User.objects.get(id=user_pk)
        validated_data['is_default'] = True
        user_addresses = PersonAddress.objects.filter(person=user_pk)
        for address in user_addresses:
            address.is_dafault = False
            address.save()
        return super(PersonAddressSerializer, self).create(validated_data)


class PersonAddressUpdateSerializer(PersonAddressSerializer):
    class Meta:
        model = PersonAddress
        fields = "__all__"

    def validate_is_default(self, is_default):
        if is_default == False:
            raise serializers.ValidationError(detail='Field must be set to true on selected address', code=400)
        return is_default


    def update(self, instance:PersonAddress , validated_data):
        if validated_data['is_default']:
            user_addresses = PersonAddress.objects.filter(person=instance.person.id)
            for address in user_addresses:
                if address.id == instance.id:
                    continue
                address.is_dafault = False
                address.save()
        return super(PersonAddressSerializer, self).update(instance, validated_data)