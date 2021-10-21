from typing import Tuple
from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.fields import TextField
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify

# Category Section
class Category(models.Model):
    category_title = models.CharField(_("Title"), max_length=32, db_index=True)
    slug = models.SlugField(
        _("Slug"),
        blank=True,
        unique=True,
    )
    parent = models.ForeignKey(
        "self",
        verbose_name=_("Parent"),
        related_query_name="child",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default="self",
    )
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.category_title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category_title)
        super(Category, self).save(*args, **kwargs)


# Post Section
class Post(models.Model):
    title = models.CharField(_("Title"), max_length=512, db_index=True)
    slug = models.SlugField(
        _("Slug"),
        blank=True,
        unique=True,
    )
    content = models.TextField(_("Post Content"))
    category = models.ManyToManyField(
        "Category",
        related_name="posts",
        verbose_name=_("Category"),
        blank=True,
    )
    create_at = models.DateTimeField(_("Publish at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def display_category(self):
        """Create a string for the Category. This is required to display Category in Admin."""
        return ", ".join(
            category.category_title for category in self.category.all()[:3]
        )

    display_category.short_description = "Category"
