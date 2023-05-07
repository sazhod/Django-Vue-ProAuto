from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.html import mark_safe


class ServiceModel(models.Model):
    """
    Модель описывающая услуги сервиса.
    """
    class Meta:
        ordering = ['title']
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    title = models.CharField(max_length=255, verbose_name='Название')
    min_price = models.IntegerField(
        validators=[MinValueValidator(100), MaxValueValidator(999999)],
        verbose_name='Цена от'
    )
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title


class WorkExampleModel(models.Model):
    """
    Модель описывающая примеры работ по услугам.
    """
    service_id = models.ForeignKey(ServiceModel, on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Описание')
    start_date = models.DateTimeField(verbose_name='Дата начала работы')
    end_date = models.DateTimeField('Дата окончания работы')

    def __str__(self):
        return f'Для услуги "{self.service_id}"'

    class Meta:
        verbose_name = 'Пример работы'
        verbose_name_plural = 'Примеры работ'


class ImagesModel(models.Model):
    """
    Модель описывающая изображения ДО ПОСЛЕ для примеров работ.
    """
    class Meta:
        verbose_name = 'Изображения'
        verbose_name_plural = 'Изображения'

    title = models.CharField(max_length=255, verbose_name='Название')
    before_image = models.ImageField(upload_to='static/services/images/', verbose_name='Изображение до')
    after_image = models.ImageField(upload_to='static/services/images/', verbose_name='Изображение после')
    work_example_id = models.ForeignKey(WorkExampleModel, verbose_name='Фото работ', on_delete=models.CASCADE)

    def before_image_preview(self):
            return mark_safe(
                f'<img src = "{self.before_image.url}" width = "300"/>'
            )

    def after_image_preview(self):
        return mark_safe(
            f'<img src = "{self.after_image.url}" width = "300"/>'
        )

    def __str__(self):
        return self.title

