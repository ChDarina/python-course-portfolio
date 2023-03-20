from django.db import models

from base.models import TimeStampMixin


class Author(TimeStampMixin):
    """
    Модель для хранения данных об авторе сайта
    """

    github = models.URLField(verbose_name="Ссылка на GitHub репозиторий")
    resume = models.URLField(verbose_name="Ссылка на резюме")
    email = models.EmailField(verbose_name="Email-почта")

    class Meta:
        verbose_name = "Информация об авторе сайта"

    def __str__(self) -> str:
        return f'Объект "автор сайта" (id={self.pk})'
