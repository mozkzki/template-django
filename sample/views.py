from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, "sample/index.html", {})


def index_get(request):
    if request.method != "GET":
        return HttpResponseBadRequest()

    try:
        user_name = request.GET.get("user", "default")
        return HttpResponse("access done! by user=" + user_name)
    except Exception as e:
        print("error occured.")
        print(e)
        return HttpResponseBadRequest()


@csrf_exempt
def index_post(request):
    if request.method != "POST":
        return HttpResponseBadRequest()

    try:
        body_unicode = request.body.decode("utf-8")
        name = request.POST.get("name", "規定の名前")
        email = request.POST.get("email", "規定のEmail")

        dic = {"body_unicode": body_unicode, "name": name, "email": email}

        return render(request, "sample/post.html", dic)
    except Exception as e:
        print("error occured.")
        print(e)
        return HttpResponseBadRequest()
