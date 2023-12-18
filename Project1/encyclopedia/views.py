import markdown
from django.shortcuts import render, reverse, HttpResponseRedirect
from django import forms

from . import util

class NewWikiForm(forms.Form):
    article = forms.CharField(label="New Article")


def index(request):
    if "articles" not in request.session:
        request.session["articles"] = []
    
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def new_page(request):
    if request.method == "POST":
        form = NewWikiForm(request.POST)
        if form.is_valid():
            article = form.cleaned_data["article"]            
            return HttpResponseRedirect(reverse("wiki:index"))
        else:
            return render(request, "wiki/create.html", {
                "form": form
            })

    return render(request, "encyclopedia/create.html", {
        "form": NewWikiForm()
    })

def rand(request):
    
    with open("Git.md", "r") as file:
        text = file.read()
        html = markdown.markdown(text)
    return render(request, "encyclopedia/rand.html", {
        
    })

#def display(request, entry):
#    return HttpResponse("You're looking at page %s." % entry)

def display(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)