from django.shortcuts import render

# menu = [
#     {"title": "Home", "url_name": "home"},
#     {"title": "About", "url_name": "about"},
#     {"title": "Add", "url_name": "add"}
# ],


def home(request):
    menu = [{'title': 'Home'},
            {'title': 'About'},
            {'title': 'Contact'},
            {'title': 'Login'},
            {'title': 'Register'}
            ]
    context = {
        'menu': menu,
    }
    return render(request, 'home.html', context)


def custom_handler404(request, exception):
    return render(request, "unihub/404.html", {"title": "Not Found"})  # not found


def custom_handler500(request):
    return render(request, "unihub/500.html", {"title": "Server Error"})  # internal server error


def custom_handler403(request, exception):
    return render(request, "unihub/403.html", {"title": "Forbidden"})  # forbidden


def custom_handler400(request, exception):
    return render(request, "unihub/400.html", {"title": "Bad Request", "menu": menu})  # bad request
