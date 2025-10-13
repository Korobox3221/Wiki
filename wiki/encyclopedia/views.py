from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from markdown2 import Markdown
import random
from django.contrib import admin

from . import util
markdowner = Markdown()

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })
def wiki(request, title):
    if util.get_entry(title) == None:
        message = 'Page not found'
        return HttpResponseRedirect(f'/error_page/{message}')
    content = markdowner.convert(util.get_entry(title))
    return render(request, "wiki/title.html",{
        'content': content,
        'title':title
    })
def search(request):
    if request.method == "POST":
        query = request.POST.get("q", "").strip()
        if query:
            if util.get_entry(query):
                return HttpResponseRedirect(f'/wiki/{query}')

            all_entries = util.list_entries()
            matches = [entry for entry in all_entries if query.lower() in entry.lower()]

            return render(request, "encyclopedia/index.html", {
                "entries": matches,
                "search_mode": True,
                "query": query
            })

    return HttpResponseRedirect("/")

def new_page(request):
    if  request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        entries = util.list_entries()
        if title in entries:
            message = 'Page already exist!'
            return HttpResponseRedirect(f'/error_page/{message}')
        util.save_entry(title,content)
        return HttpResponseRedirect(f'/wiki/{title}')
    return render(request, "new_page/new_page.html")
def edit_page(request,title):
    content = util.get_entry(title)
    if request.method == "POST":
        new_title = title
        new_content = request.POST.get("content")
        util.save_entry(new_title,new_content)
        return HttpResponseRedirect(f'/wiki/{title}')
    return render(request, "edit_page/edit_page.html",{
        'title':title,
        'content':content
    })
def random_page(request):
    entries = util.list_entries()
    if entries:
        title = random.choice(entries)
        return HttpResponseRedirect(f'/wiki/{title}')
    return render(request, "random_page/random_page.html")




def error(request, message):
    return render(request, "error_page/error.html"
                  ,{ 'message':message})
