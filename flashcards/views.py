from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext as _
from .models import Flashcard, FlashcardCategory

def flashcard_list(request):
    categories = FlashcardCategory.objects.all()
    return render(request, 'flashcards/list.html', {'categories': categories})

def flashcard_category(request, category_id):
    category = get_object_or_404(FlashcardCategory, id=category_id)
    flashcards = Flashcard.objects.filter(category=category)
    return render(request, 'flashcards/category.html', {
        'category': category,
        'flashcards': flashcards
    })

def flashcard_view(request, flashcard_id):
    flashcard = get_object_or_404(Flashcard, id=flashcard_id)
    return render(request, 'flashcards/view.html', {'flashcard': flashcard})

# In your views.py
def random_flashcard(request):
    flashcards = Flashcard.objects.order_by('?')[:10]  # 10 random cards
    return render(request, 'flashcards/random.html', {
        'flashcards_json': serializers.serialize('json', flashcards)
    })