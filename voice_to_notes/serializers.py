# myapp/serializers.py

from rest_framework import serializers
from .models import V2NModel

class Voice2NotesSerializer(serializers.ModelSerializer):

    def validate_notes_title(self, value):
        if '-' in value or '^' in value:
            raise serializers.ValidationError("Notes title cannot contain '-' or '^' characters.")
        return value

    class Meta:
        model = V2NModel
        fields = ['id', 'notes_title', 'notes_content']
