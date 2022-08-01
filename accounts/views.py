from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import CustomUserSerializer


# @login_required
# @authentication_classes(
#     JWTAuthentication,
# )
# @permission_classes((IsAuthenticated,))
@api_view(["GET"])
def getUserProfile(request):
    print(request.user)
    f = request.user.is_authenticated
    print(request.META["HTTP_AUTHORIZATION"])  # printing the token
    if f:
        print("Yes")
    user = request.user
    serializer = CustomUserSerializer(user, many=False)
    return Response(serializer.data)


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        print(request.user)
        print(request.META["HTTP_AUTHORIZATION"])
        content = {"message": "Hello, GeeksforGeeks"}
        return Response(content)
