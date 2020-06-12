from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ChildrenSerializer
from rest_framework import status
from.models import Children

class ChildrenView(APIView):
    def post(self, request):
        children_serializer = ChildrenSerializer(data=request.data)  # Request의 data를 UserSerializer로 변환

        if children_serializer.is_valid():
            children_serializer.save()  # UserSerializer의 유효성 검사를 한 뒤 DB에 저장
            return Response(children_serializer.data, status=status.HTTP_201_CREATED)  # client에게 JSON response 전달
        else:
            return Response(children_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, **kwargs):
        if kwargs.get('appuserId') is None:
            children_queryset = Children.objects.all()  # 모든 User의 정보를 불러온다.
            children_queryset_serializer = ChildrenSerializer(children_queryset, many=True)
            return Response(children_queryset_serializer.data, status=status.HTTP_200_OK)
        else:
            user_id = kwargs.get('appuserId')
            children_serializer = ChildrenSerializer(Children.objects.filter(uid=user_id), many=True)
            return Response(children_serializer.data, status=status.HTTP_200_OK)
    def delete(self, request, **kwargs):
        if kwargs.get('c_id') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            c_id = kwargs.get('c_id')
            children_obj = Children.objects.get(pk=c_id)
            children_obj.delete()
            return Response("Success delete!", status=status.HTTP_201_CREATED)