from django.shortcuts import render

# Create your views here.
def greeting(request):
    content = {
        'name': 'Phillip',
    }
    return render(request, 'hello_world/index.html', content)