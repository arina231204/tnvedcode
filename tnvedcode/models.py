
from django.db import models

class TnvedCode(models.Model):
    code = models.IntegerField(unique=True, verbose_name='Код товара')

    def __str__(self):
        return str(self.code)

class Organization(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название организации')

    def __str__(self):
        return self.name


class Permission(models.Model):
    IMPORT_STATUS_CHOICES = [
        ('+', 'Разрешен'),
        ('-', 'Без лицензии'),
        ('x', 'Запрещен'),
    ]



    code = models.ForeignKey(TnvedCode, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    import_status_legal = models.CharField(max_length=1, choices=IMPORT_STATUS_CHOICES, default='-', verbose_name='Статус ввоза для юридических лиц')
    import_status_individual = models.CharField(max_length=1, choices=IMPORT_STATUS_CHOICES, default='-', verbose_name='Статус ввоза для физических лиц')


