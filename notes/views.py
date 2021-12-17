import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Note


# Create your views here.
def index(req):
    note_list = Note.objects.all()
    context = {
        'note_list': note_list
    }

    return render(req, 'list.html', context)


def note(req):
    action = req.GET.get('action')
    note_id = 0

    note = Note()

    if action == 'view':
        note_id = req.GET.get('id')
        note = Note.objects.get(id=note_id)

    if action == 'new':
        note.title = ''
        note.content = ''
        note.pub_date = timezone.now()
        note.save()

        note_id = note.id

    context = {
        'id': note_id,
        'action': action,
        'note': note
    }

    return render(req, 'editor.html', context)


def save_note(req):
    res = {
        'success': True,
        'message': 'Note saved'
    }

    data = json.loads(req.body)

    note = Note.objects.get(id=data['id'])
    note.title = data['title']
    note.content = data['content']
    note.save()

    return JsonResponse(res)


def delete_note(req, id):
    note = Note.objects.get(id=id)
    note.delete()

    return redirect('/')


def setting(req):
    return render(req, 'setting.html')
