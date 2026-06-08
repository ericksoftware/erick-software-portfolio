from django.db import models


class TimeStampedModel(models.Model):
    """
    Agrega automáticamente las fechas de creación y actualización.
    """

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="fecha de creación",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="última actualización",
    )

    class Meta:
        abstract = True


class OrderedVisibleModel(TimeStampedModel):
    """
    Base para elementos que pueden ordenarse y ocultarse.
    """

    order = models.PositiveIntegerField(
        default=0,
        db_index=True,
        verbose_name="orden",
    )
    is_visible = models.BooleanField(
        default=True,
        verbose_name="visible",
    )

    class Meta:
        abstract = True
        ordering = ("order", "id")