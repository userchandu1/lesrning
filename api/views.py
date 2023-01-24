from .models import Comment
from .serializers import CommentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse


def comment_view(request, pk):
    raw_data = Comment.objects.get(id=pk)
    serializer = CommentSerializer(raw_data)
    # json_data = JSONRenderer().render(data=serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)


def comment_list_view(request):
    raw_data = Comment.objects.all()
    serializer = CommentSerializer(raw_data, many=True)
    # json_data = JSONRenderer().render(data=serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data, safe=False)
