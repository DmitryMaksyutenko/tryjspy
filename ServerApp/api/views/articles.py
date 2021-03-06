from rest_framework.views import APIView
from rest_framework.response import Response

from blog.services.articles import ArticlesServices


class ArticlesView(APIView):
    def get(self, request, *args, **kwargs):
        service = ArticlesServices(request)
        data = service.get_all()
        return Response(data)


class ArticleView(APIView):
    def get(self, request, *args, **kwargs):
        service = ArticlesServices(request)
        data = service.get_one()
        return Response(data)
