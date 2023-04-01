from django.shortcuts import get_object_or_404, redirect #render
from django.views import generic
from .models import Note
#from django.http import HttpResponseRedirect

class IndexView(generic.ListView):
    template_name = 'notes/index.html'
    context_object_name = 'note_list'

    def get_queryset(self):
        """Return all the latest notes."""
        return Note.objects.order_by('-created_at')

def add(request):
    title = request.POST['title']
    Note.objects.create(title=title)

    return redirect('notes:index')

def delete(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    note.delete()

    return redirect('notes:index')

def update(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    isCompleted = request.POST.get('isCompleted', False)
    if isCompleted == 'on':
        isCompleted = True
    
    note.isCompleted = isCompleted

    note.save()
    return redirect('notes:index')