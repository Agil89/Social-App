from rest_framework import generics, status, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PostSerializer
from django.http import Http404
from .models import PostLike, Post



class PostCreateView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = PostSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({
                'message': 'Post created!'}, status=status.HTTP_201_CREATED)

        return Response({'Errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

class PostLikeView(APIView):
    def post(self, request, id):
        post = Post.objects.get(id=id)
        if not PostLike.objects.filter(user=request.user, post=post).first():
            PostLike.objects.create(user=request.user, post=post)
            return Response({'Success': 'Liked'}, status=status.HTTP_200_OK)
        else:
            return Response({'Errors': 'Like already exists'}, status=status.HTTP_400_BAD_REQUEST)

class PostUnLikeView(APIView):
    def post(self, request, id):
        post = Post.objects.get(id=id)
        if PostLike.objects.filter(user=request.user, post=post).first():
            PostLike.objects.filter(user=request.user, post=post).delete()
            return Response({'Success': 'Deleted!'}, status=status.HTTP_200_OK)
        else:
            return Response({'Errors': 'Like doesn"t exists'}, status=status.HTTP_400_BAD_REQUEST)

class GetAllPosts(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

class FilterLikesByDate(APIView):
    def get(self, request):
        data = {}
        date_from = self.request.query_params.get('date_from')
        date_to = self.request.query_params.get('date_to')
        likes = PostLike.filter_by_date(date_from, date_to)
        for like in likes:
            if not data.get(f'{like.created_date}'):
                data[f'{like.created_date}'] = {
                    'date': str(like.created_date),
                    'count':0
                }
            data[f'{like.created_date}']['count'] += 1
        return Response(data.values(), status=status.HTTP_200_OK)
    