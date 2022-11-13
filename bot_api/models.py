import django.db.models as model
from django.db.models import Model


class Objects(Model):
    handle_num = model.SmallIntegerField(
        verbose_name="Номер хендла объекта",
        null=True,
        blank=True,
        default="Не определено",
    )
    obj_name = model.CharField(
        verbose_name="Имя объекта",
        max_length=999,
        null=True,
        blank=True,
        default="Не определено",
    )
    top_y = model.SmallIntegerField(
        verbose_name="Верхняя Y координата",
        null=True,
        blank=True,
        default=0,
    )
    bottom_y = model.SmallIntegerField(
        verbose_name="Нижняя Y координата",
        null=True,
        blank=True,
        default=0,
    )
    left_x = model.SmallIntegerField(
        verbose_name="Левая X координата",
        null=True,
        blank=True,
        default=0,
    )
    right_x = model.SmallIntegerField(
        verbose_name="Правая X координата",
        null=True,
        blank=True,
        default=0,
    )

    @staticmethod
    def clear_all():
        Objects.objects.all().delete()
