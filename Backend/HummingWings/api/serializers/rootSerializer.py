from rest_framework import serializers
from ..models.root import Root

class RootSerializer(serializers.ModelSerializer):
    class Meta:
        model = Root
        exclude = ('password',)
