from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST

from snippets.forms import SnippetForm, CommentForm
from snippets.models import Snippet, Comment


def top(request):
    context = {
        "snippets": Snippet.objects.all(),
        "num_snippets": Snippet.objects.all().count(),
        "num_users": get_user_model().objects.all().count(),
    }
    return render(request, "top.html", context)
