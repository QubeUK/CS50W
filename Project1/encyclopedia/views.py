import markdown
from random import choice
from django.shortcuts import render, reverse, HttpResponseRedirect
from django import forms

from . import util

class NewWikiForm(forms.Form):
    article = forms.CharField(label="New Article")


def index(request):
    if "articles" not in request.session:
        request.session["articles"] = []    
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})

def new_page(request):
    if request.method == "POST":
        form = NewWikiForm(request.POST)
        if form.is_valid():
            article = form.cleaned_data["article"]            
            return HttpResponseRedirect(reverse("wiki:index"))
        else:
            return render(request, "wiki/create.html", {"form": form})

    return render(request, "encyclopedia/create.html", {"form": NewWikiForm()})

def rand(request):    
    article = choice(util.list_entries())    
    html = markdown.markdown(util.get_entry(article))
    title = html.split()[0].replace("<h1>","").replace("</h1>","")        
    return render(request, "encyclopedia/rand.html", {"html":html, "title":title})


def display(request, article):             
    html = markdown.markdown(util.get_entry(article))
    title = html.split()[0].replace("<h1>","").replace("</h1>","")        
    return render(request, "encyclopedia/rand.html", {"html":html, "title":title})
    
    
def search(request):
    query = request.GET["query"]
    if query in util.list_entries():
        html = markdown.markdown(util.get_entry(query))
        title = html.split()[0].replace("<h1>","").replace("</h1>","")       
        return render(request, "encyclopedia/rand.html", {"html":html, "title":title})
                
    return render(request, "encyclopedia/search.html", {"title":"Search Results"})
    