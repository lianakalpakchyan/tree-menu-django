from django.db import models
from autoslug import AutoSlugField


class Menu(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='url', unique=True, null=False, editable=False)
    url = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField()

    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = "menus"
        ordering = ['order']

    def __str__(self):
        full_path = [self.name]
        parent = self.parent
        while parent is not None:
            full_path.append(parent.name)
            parent = parent.parent
        return ' ➡ '.join(full_path[::-1])

    def has_children(self):
        return Menu.objects.filter(parent=self).exists()

    def get_absolute_url(self):
        url = [self.slug]
        parent = self.parent
        while parent is not None:
            url.append(parent.slug)
            parent = parent.parent
        return f"/{'/'.join(url[::-1])}"
