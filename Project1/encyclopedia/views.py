from random import choice
import markdown
from django.shortcuts import render, reverse, HttpResponseRedirect
from django import forms

from . import util

class NewWikiForm(forms.Form):
    """Django form class"""
    title = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Enter Title'}))
    content = forms.CharField(label="",widget=forms.Textarea(attrs={'placeholder':'Enter Markdown Here'}))


def index(request):
    """Creates list of entires for index.html"""
    if "articles" not in request.session:
        request.session["articles"] = []
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})

def new_page(request):
    """Displays form and gets data for new wiki entry"""
    if request.method == "POST":
        form = NewWikiForm(request.POST)
        if form.is_valid():
            #article = form.cleaned_data["article"]         
            return HttpResponseRedirect(reverse("wiki:index"))
        else:
            return render(request, "wiki/create.html", {"form": form})

    return render(request, "encyclopedia/create.html", {"form": NewWikiForm()})

def rand(request):
    """Displays a random article"""
    article = choice(util.list_entries())
    html = markdown.markdown(util.get_entry(article))
    title = html.split()[0].replace("<h1>","").replace("</h1>","")
    return render(request, "encyclopedia/rand.html", {"html":html, "title":title})


def display(request, article):
    """Displays a requested article"""
    html = markdown.markdown(util.get_entry(article))
    title = html.split()[0].replace("<h1>","").replace("</h1>","")
    return render(request, "encyclopedia/rand.html", {"html":html, "title":title})


def search(request):
    """Displays a searched for article"""
    query = request.GET["query"]    
    if query.casefold() in map(str.casefold, util.list_entries()):
        html = markdown.markdown(util.get_entry(query))
        title = html.split()[0].replace("<h1>","").replace("</h1>","")
        return render(request, "encyclopedia/rand.html", {"html":html, "title":title})
    return render(request, "encyclopedia/search.html", {"title":"Search Results"})
