from django.db import models
from django.db.models.deletion import SET_NULL
from django.db.models.fields import TextField
from django.utils.translation import ugettext_lazy as _


class category(models.Model):
    title = models.CharField(_("Title"), max_length=32)
    slug = models.SlugField(_("Slug"))
    parent = models.ForeignKey(
        "self",
        verbose_name=_("Parent"),
        related_query_name="child",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    create_at = models.DateTimeField(_("Create at"))
    update_at = models.DateTimeField(_("Update at"))


class post(models.Model):
    title = models.CharField(_("Title"), max_length=512, db_index=True)
    slug = models.SlugField(_("Slug"), db_index=True, unique=True)
    content = models.TextField(_("Post Content"))
    category = models.ForeignKey(
        "category",
        related_name="posts",
        verbose_name=_("Category"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    create_at = models.DateTimeField(_("Publish at"))
    update_at = models.DateTimeField(_("Update at"))
