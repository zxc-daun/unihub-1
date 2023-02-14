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
            {'title': 'Register'},
            {'title': 'Add'}
            ]
    context = {
        'menu': menu,
    }
    return render(request, 'unihub/home.html', context)


def custom_handler404(request, exception):
    return render(request, "unihub/404.html", {"title": "Not Found"})  # not found


def custom_handler500(request):
    return render(request, "unihub/500.html", {"title": "Server Error"})  # internal server error


def custom_handler403(request, exception):
    return render(request, "unihub/403.html", {"title": "Forbidden"})  # forbidden


def custom_handler400(request, exception):
    return render(request, "unihub/400.html", {"title": "Bad Request"})  # bad request


def login(request):
    menu = [{'title': 'Home'},
            {'title': 'About'},
            {'title': 'Contact'},
            {'title': 'Login'},
            {'title': 'Register'},
            {'title': 'Add'},
            {'title': 'Logout'}
            ]
    context = {
        'menu': menu,
    }
    return render(request, 'unihub/login.html', context)


def register(request):
    menu = [{'title': 'Home'},
            {'title': 'About'},
            {'title': 'Contact'},
            {'title': 'Login'},
            {'title': 'Register'}
            ]
    context = {
        'menu': menu,
    }
    return render(request, 'unihub/register.html', context)

def logout(request):
    menu = [{'title': 'Home'},
            {'title': 'About'},
            {'title': 'Contact'},
            {'title': 'Login'},
            {'title': 'Register'},
            {'title': 'Add'}
            ]
    context = {
        'menu': menu,
    }
    return render(request, 'unihub/logout.html', context)

def add(request):
    menu = [{'title': 'Home'},
            {'title': 'About'},
            {'title': 'Contact'},
            {'title': 'Login'},
            {'title': 'Register'},
            {'title': 'Add'}
            ]
    context = {
        'menu': menu,
    }
    return render(request, 'unihub/add.html', context)
