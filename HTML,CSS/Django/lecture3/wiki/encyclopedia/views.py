from django.shortcuts import render
from markdown2 import Markdown

import util

def convert_md_to_html(title):
    content = util.get_entry(title)
    markdowner = Markdown.Markdown()
    if content == None:
        return None
    else:
        return markdownner.convert(content)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

