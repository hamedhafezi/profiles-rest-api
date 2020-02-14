from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    '''Serializers a name field for testing our APIView'''
    name = serializers.CharField(max_length=10)
    email = serializers.EmailField(max_length=250)
