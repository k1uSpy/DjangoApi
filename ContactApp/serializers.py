from rest_framework import serializers
from ContactApp.models import Contacts

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contacts
        fields=('ContactId', 'ContactName', 'ContactPhone', 'ContactAddress')