from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def new_page(request):
    return render(request, "encyclopedia/create.html", {
        # "title, contents":util.save_entry()
    })

def random(request, title):
    return render(request, "encyclopedia/random.html", {
        "title":util.get_entry()
    })

def display(request, title):
    return render(request, "encyclopedia/random.html", {
        "title":util.get_entry(title)
    })
