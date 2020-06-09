from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CommentsSerializer
from rest_framework import status
from.models import Comments
from django.conf import settings




class CommentsView(APIView):
    def post(self, request):
        comments_serializer = CommentsSerializer(data=request.data)

        if comments_serializer.is_valid():
            comments_serializer.save()
            return Response(comments_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(comments_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, **kwargs):
        if kwargs.get('itype') is None:
            comments_queryset = Comments.objects.all()
            comments_queryset_serializer = CommentsSerializer(comments_queryset, many=True)
            return Response(comments_queryset_serializer.data, status=status.HTTP_200_OK)
        else:
            itype = kwargs.get('itype')
            comments_serializer = CommentsSerializer(Comments.objects.get(pk=itype))
            return Response(comments_serializer.data, status=status.HTTP_200_OK)  # 테스트용 response

    def put(self, request, **kwargs):
        if kwargs.get('itype') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            itype = kwargs.get('itype')
            comments_object = Comments.objects.get(pk=itype)

            update_comments_serializer = CommentsSerializer(comments_object, data=request.data)
            if update_comments_serializer.is_valid():
                update_comments_serializer.save()
                return Response(update_comments_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, **kwargs):
        if kwargs.get('itype') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)
        else:
            itype = kwargs.get('itype')
            comments_object = Comments.objects.get(pk=itype)
            comments_object.delete()
            return Response("ok", status=status.HTTP_201_CREATED)


class TreemodelView(APIView):
    def get(self, request, **kwargs):
        if kwargs.get('uimage') is None:
            return Response("invalid request", status=status.HTTP_400_BAD_REQUEST)

        else:
            uimage = settings.MEDIA_ROOT+'\\userimage\\'+kwargs.get('uimage')
            # model 호출하기
            #itype = Model(uimage)
            itype = 1
            comments_serializer = CommentsSerializer(Comments.objects.get(pk=itype))
            #return Response(uimage, status=status.HTTP_200_OK)
            return Response(comments_serializer.data, status=status.HTTP_200_OK)
