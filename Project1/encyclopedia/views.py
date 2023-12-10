from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def new_page(request):
    return render(request, "encyclopedia/new_page.html", {
        #"title, contents":util.save_entry()
    })

def random(request):
    return render(request, "encyclopedia/random.html", {
        #"title, contents":util.get_entry()
    })