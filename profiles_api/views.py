from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    '''Test API View'''

    def get(self, request, format=None):
        '''Returns a list APIView featurs'''
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to traditional Django View',
            'Gives you the most control over your application  logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello', 'res': an_apiview})
