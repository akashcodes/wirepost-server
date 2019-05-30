"""
"""
from django.http import HttpResponse, JsonResponse
from _Models.Post import Post


def articles(request, year=None, month=None, date=None, aid=None):
    """
        Method to fetch all articles
    """
    default_items = 20
    items_per_page = int(request.GET.get("limit", default_items))

    page = int(request.GET.get("page", 1))
    offset = int(request.GET.get("offset", (page-1) * items_per_page))
    print(offset)

    if not page:
        page = 1

    if year and month and date and aid:
        return HttpResponse("Get that exact article")

    if year and month and date:
        return HttpResponse("Show articles from "+str(year)+"/"+str(month)+"/"+str(date))

    if year and month:
        return HttpResponse("Show artciles from "+str(year)+"/"+str(month))

    if year:
        return HttpResponse("Show articles from year "+str(year))
    
    posts = [
        {
            "title": post.title,
            "content": post.content_html,
            "banner": post.banner,
            "content": post.content_markup,
            "category": post.category,
            "color": post.color,
            "id": str(post.id),
            "creation_date": post.creation_date
        } for post in Post.objects.skip(offset).limit(items_per_page)]

    return JsonResponse(posts, safe=False)


def article(request, postid=None):
    """
        Method to fetch article by id
    """

    #postid = request.GET.get("id", None)

    if not postid:
        return JsonResponse({}, safe=False)
    
    posts = [
        {
            "title": post.title,
            "content": post.content_html,
            "banner": post.banner,
            "category": post.category,
            "color": post.color,
            "id": str(post.id),
            "creation_date": post.creation_date
        } for post in Post.objects(id=postid)]
    
    return JsonResponse(posts, safe=False)


def category_articles(request, category):
    """
        Method to fetch all articles by category
    """

    default_items = 20
    items_per_page = int(request.GET.get("limit", default_items))+1

    page = int(request.GET.get("page", 1))
    offset = int(request.GET.get("offset", page * items_per_page))

    if not page:
        page = 1
    
    posts = [
        {
            "title": post.title,
            "content": post.content_html,
            "banner": post.banner,
            "content": post.content_markup,
            "category": post.category,
            "color": post.color,
            "id": str(post.id),
            "creation_date": post.creation_date
        } for post in Post.objects(category=category).skip(offset).limit(items_per_page)]

    return JsonResponse(posts, safe=False)
