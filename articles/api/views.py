from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

@api_view(['GET', 'POST'])
def articles(request):
    if request.method == 'POST':
        return Response({
            "message": "POST - state publish, draft"
        })

    elif request.method == 'GET':
        params = request.query_params

        author_id = params.get('authorId', "me")
        page = int(params.get('page', 1))
        size = params.get('size', 10)
        state = params.get('state', 'published')
        sort_by = params.get('sortBy', 'createdAt')
        sort_order = params.get('sortOrder', 'desc')
        category = params.get('category', None)
        keyword = params.get('keyword', None)

        return Response({
            "message": "GET articles",
            "author_id": author_id,
            "page": page,
            "size": size,
            "state": state,
            "sort_by": sort_by,
            "sort_order": sort_order,
            "category": category,
            "keyword": keyword
        })
    else:
        return Response({
            "message": "articles error exception",
        })


@api_view(['GET', 'PATCH', 'DELETE'])
def article_detail(request, id):
    if request.method == "GET":
        return Response({
                "message": "article detail get page.",
                "id": id
        })
    elif request.method == "PATCH":
        return Response({
                "message": "article detail patch page.",
                "id": id
        })
    elif request.method == "DELETE":
        return Response({
                "message": "article detail del page.",
                "id": id
        })
    else:
        return Response({
            "message": "article detail error exception",
        })


@api_view(['PATCH'])
def publish_draft(request, id):

    if request.method == 'PATCH':
        return Response({
            "message": "publish draft page.",
            "id": id
        })
    else:
        return Response({
            "message": "publishing error exception",
        })