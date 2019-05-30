"""
Views
"""

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import markdown
import json
from _Models.Post import Post
from .models import Account


def create_dum(request):
    """
    asas
    """
    name = "admin"
    password = "admin"
    email = "admin"
    priviliges = {"admin": True}

    account = Account(
        username=name,
        name=name,
        password=password,
        email=email
    )

    account.save()

    account.set_privileges(priviliges)


def admin(request):

    """
    Loads Admin Page
    """
    # request.session["username"] = request.session["password"] = None
    if(request.session.get('username') and request.session.get('password')):
        return render(request, 'admin/admin.html')
    return HttpResponseRedirect('login')


@csrf_exempt
def login(request):

    """
    Login
    """

    if request.method == "POST":

        if(request.POST.get('username') and request.POST.get('password')):

            account = Account.objects(username=request.POST.get('username'))
            print(account)

            if account:

                request.session['username'] = request.POST['username']
                request.session['password'] = request.POST['password']
                request.session['priviliges'] = {
                    "admin": True,
                    "creator": True,
                    "content_manager": True
                }
                print("Account exists")

                return HttpResponseRedirect('/admin')

            return HttpResponse("User Not Found!")

        return HttpResponse("_|_")

    return render(request, "admin/login.html")


@csrf_exempt
def create_post(request):
    """
    Logic for post creation
    """

    if request.session["priviliges"]["creator"]:
        if request.method == 'POST':
            if(request.POST.get('title') and request.POST.get('content')):

                title = request.POST.get('title')
                content_raw = request.POST.get('content')
                banner = request.POST.get('banner')
                category = request.POST.get('category')
                color = request.POST.get('color')
                content_html = markdown.markdown(content_raw)

                post = Post(
                    title=title,
                    content_markup=content_raw,
                    content_html=content_html,
                    banner=banner,
                    category=category,
                    color=color,
                    views=1
                )

                post.save()

                return HttpResponse("Success! News posted.")

        return render(request, "admin/editor.html")

    return HttpResponse("You are not authorised to perform this action")


def manage_account(request, action=''):
    """
    Logic for loading manage accounts page
    """

    if request.session["priviliges"]["admin"]:

        if action == 'create':
            if request.method == "POST":

                if(request.POST.get('email') and
                   request.POST.get('name') and
                   request.POST.get('password')):

                    name = request.POST.get('name')
                    password = request.POST.get('password')
                    email = request.POST.get('email')
                    priviliges = request.POST.get('priviliges')

                    account = Account(
                        name=name,
                        password=password,
                        email=email
                    )

                    account.save()

                    account.set_privileges(priviliges)

                return HttpResponse("Success! Account created.")

            return HttpResponse("Invalid Request. Please use 'POST' request type.")

        if action == 'delete':
            pass

        if action == 'priviliges':
            pass

        return render(request, "admin/manage_account.html")

    return HttpResponseRedirect("Unauthorised.")


@csrf_exempt
def manage_post(request, action=''):
    """
    Logic for loading manage accounts page
    """

    if request.session["priviliges"]["admin"]:

        if action == 'delete':
            if request.method == "POST":

                if request.POST.get('post_id'):

                    post_id = request.POST.get('post_id')

                    post = Post.objects(id=post_id).delete()

                    return HttpResponse("Successfully Deleted Post!"+post_id)

                return HttpResponse("Invalid")

            return HttpResponse("Invalid Request. Please use 'POST' request type.")

        if action == 'priviliges':
            pass

        if request.method == 'GET':

            # Pagination
            items_per_page = 10
            page = int(request.GET.get("page", 1)) - 1
            offset = page * items_per_page
            posts = [
                {
                    "title": post.title,
                    "content": post.content_html,
                    "id": str(post.id)
                } for post in Post.objects.skip(offset).limit(items_per_page)]

            ctx = {
                'posts': posts
            }
            print(ctx)
            return render(request, 'admin/manage_post.html', context=ctx)

        return HttpResponseRedirect('/admin/manage_post/')

    return HttpResponse("You don't have the authorisation.")
