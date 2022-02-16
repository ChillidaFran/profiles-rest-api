from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Resturn a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditionmal Django View',
            'Gives you the most control over you applicartion logic',
            'Is mapoped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview':an_apiview})
