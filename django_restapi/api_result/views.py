from rest_framework.views import APIView
from rest_framework.response import Response


class ResultView(APIView):
    def get(self, request):
        return Response("ok", status=200)