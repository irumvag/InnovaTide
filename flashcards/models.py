from django.db import models
from django.utils.translation import gettext_lazy as _

class FlashcardCategory(models.Model):
    name = models.CharField(_("Category Name"), max_length=100)
    description = models.TextField(_("Description"), blank=True)
    color = models.CharField(_("Color Code"), max_length=7, default="#28a745")

    class Meta:
        verbose_name = _("Flashcard Category")
        verbose_name_plural = _("Flashcard Categories")

    def __str__(self):
        return self.name

class Flashcard(models.Model):
    category = models.ForeignKey(FlashcardCategory, on_delete=models.CASCADE, verbose_name=_("Category"))
    term = models.CharField(_("Term"), max_length=200)
    definition = models.TextField(_("Definition"))
    image = models.ImageField(_("Image"), upload_to='flashcards/', blank=True, null=True)
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    class Meta:
        verbose_name = _("Flashcard")
        verbose_name_plural = _("Flashcards")
        ordering = ['category', 'term']

    def __str__(self):
        return f"{self.term} - {self.category.name}"