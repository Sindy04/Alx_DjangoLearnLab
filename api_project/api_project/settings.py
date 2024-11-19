api, rest_framework
rest_framework.authtoken

rest_framework.authentication.TokenAuthentication
rest_framework.permissions.IsAuthenticated
rest_framework.views.APIView

class MyAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Only authenticated users can access this view
        return Response({'message': 'Hello, authenticated user!'})
