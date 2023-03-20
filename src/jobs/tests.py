from django.test import TestCase

from jobs.models import Job


class JobsTestCase(TestCase):
    """
    Тестирование функций выполненных работ.
    """

    def setUp(self) -> None:
        """
        Настройка перед тестированием.

        :return:
        """

        Job.objects.create(
            image="Job image",
            description="Job description",
            detailed_description="Detailed description" * 100,
        )

    def test_job_messages_creation(self) -> None:
        """
        Тестирование модели для выполненных работ.

        :return:
        """

        job = Job.objects.get(image="Job image")
        self.assertEqual(job.summary(), ("Detailed description" * 100)[:50] + "...")
        self.assertEqual(str(job), f'Объект "Выполненная работа" (id={job.pk})')
