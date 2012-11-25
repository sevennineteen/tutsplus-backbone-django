from django.forms import widgets
from rest_framework import serializers
from bbtuts.contacts.models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'first_name', 'last_name', 'email_address', 'description')