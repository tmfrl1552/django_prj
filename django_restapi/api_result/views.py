from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ResultSerializer
from rest_framework import status
from.models import Result


class ResultView(APIView):
    def post(self, request):
        result_serializer = ResultSerializer(data=request.data)  # Request의 data를 UserSerializer로 변환

        if result_serializer.is_valid():
            result_serializer.save()  # UserSerializer의 유효성 검사를 한 뒤 DB에 저장
            return Response(result_serializer.data, status=status.HTTP_201_CREATED)  # client에게 JSON response 전달
        else:
            return Response(result_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, **kwargs):
        if kwargs.get('appuserId') is None:
            if kwargs.get('childrenName') is None:
                result_queryset = Result.objects.all()  # 모든 User의 정보를 불러온다.
                result_queryset_serializer = ResultSerializer(result_queryset, many=True)
                return Response(result_queryset_serializer.data, status=status.HTTP_200_OK)
        else:
            user_id = kwargs.get('appuserId')
            c_name = kwargs.get('childrenName')
            r_queryset1 = Result.objects.filter(uid=user_id)
            r_queryset2 = r_queryset1.get(name=c_name)
            result_serializer = ResultSerializer(r_queryset2)
            #result_serializer = ResultSerializer(Result.objects.filter(uid=user_id, name=c_name))
            return Response(result_serializer.data, status=status.HTTP_200_OK)