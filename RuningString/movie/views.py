import mimetypes

from django.http import HttpResponse
from django.shortcuts import render
from .video import create_video
from .forms import TextForm
from .models import *
from transliterate import translit

LIMIT_LAST_TEXT = 5


def home(request):

    if request.method == 'POST':
        form = TextForm(request.POST)

        if form.is_valid():
            form.save()
            create_video(request.POST['text'])
            text_file = translit(request.POST['text'], language_code='ru', reversed=True)
            return download_file(request, text_file)
    else:
        form = TextForm()

    return render(request, 'index.html', {'form': form})


def last_files(request):
    last_text = Text.objects.all()[:LIMIT_LAST_TEXT]
    return render(request, 'last_files.html',
                  {'last_text': last_text})


def download_file(request, filepath):
    filepath = translit(filepath, language_code='ru', reversed=True)
    fl_path = '../tempVideo/' + filepath + '.mp4'
    filename = filepath + '.mp4'
    fl = open(fl_path, 'rb')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
