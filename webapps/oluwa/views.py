from django.shortcuts import render

def index(request, pagename=None):
    context = {}
    if (pagename) and (pagename != 'index') and not (str(pagename).__contains__('.html')):

        return render(request, f'{pagename}.html', context=context)
    return render(request, 'index.html', context=context)