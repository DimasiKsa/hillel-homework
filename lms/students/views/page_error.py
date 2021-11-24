from django.shortcuts import render


def view_404(request, exception):
    return render(request, "404.html")
