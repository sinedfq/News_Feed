from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import News 
from .forms import NewsForm


def news_list(request):
    per_page = request.GET.get("per_page", 10)
    try:
        per_page = int(per_page)
    except ValueError:
        per_page = 10

    news = News.objects.all()
    paginator = Paginator(news, per_page)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "news/news_list.html", {
        "page_obj": page_obj,
        "per_page": per_page,
    })

def add_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("news_list")
    else:
        form = NewsForm()
    return render(request, "news/add_news.html", {"form": form})