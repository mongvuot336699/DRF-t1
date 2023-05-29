from rest_framework import generics
from blog.models import Post
# from .serializers import PostSerializer

# Create your views here.
class PostList(generics.ListCreateAPIView):
    pass

class PostDetail(generics.RetrieveDestroyAPIView):
    pass