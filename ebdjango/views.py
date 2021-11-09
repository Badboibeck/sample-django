from django.shortcuts import render


def home(request):
    return render(
        request,
        'index.html',
        {
            'title': 'Home',
            'name': 'Chandler G. Beck',
        }
    )

def about(request):
    return render(
        request,
        'about.html',
        {
            'title': 'About Me',
            'name': 'Chandler G. Beck',
        }
    )

def resume(request):
    return render(
        request,
        'resume.html',
        {
            'title': 'Resume',
            'name': 'Chandler G. Beck',
        }
    )