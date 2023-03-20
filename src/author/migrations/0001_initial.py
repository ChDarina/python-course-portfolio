from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies: list = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время создания записи"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Время обновления записи"
                    ),
                ),
                ("github", models.URLField(verbose_name="Ссылка на GitHub-репозиторий")),
                ("resume", models.URLField(verbose_name="Ссылка на резюме")),
                (
                    "email",
                    models.EmailField(max_length=254, verbose_name="Электронная почта"),
                ),
            ],
            options={
                "verbose_name": "Информация об авторе",
                "verbose_name_plural": "Информация об авторе",
            },
        ),
    ]
