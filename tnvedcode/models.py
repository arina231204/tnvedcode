from django.db import models
IMPORT_STATUS_CHOICES = [
        ('+', '+'),
        ('-', '-'),
        ('x', 'x'),
    ]


class TnvedCode(models.Model):
    IMPORT_STATUS_CHOICES = [
        ('+', '+'),
        ('-', '-'),
        ('x', 'x'),
    ]

    code = models.IntegerField(unique=True, verbose_name='Код товара')
    name = models.CharField(max_length=255, verbose_name='Наименование группы товара')
    import_status_legal_private = models.CharField(max_length=1, choices=IMPORT_STATUS_CHOICES, default='-',
                                                   verbose_name='Статус ввоза для юридических лиц частных компаний')

    import_status_individual_private = models.CharField(max_length=1, choices=IMPORT_STATUS_CHOICES, default='-',
                                                        verbose_name='Статус ввоза для физических лиц частных компаний')

    def __str__(self):
        return f'{self.code}'


class Organization(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название организации')

    def __str__(self):
        return self.name


class Permission(models.Model):



    code = models.ForeignKey(TnvedCode, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    import_status_legal = models.CharField(max_length=1, choices=IMPORT_STATUS_CHOICES, default='-', verbose_name='Статус ввоза для юридических лиц')
    import_status_individual = models.CharField(max_length=1, choices=IMPORT_STATUS_CHOICES, default='-', verbose_name='Статус ввоза для физических лиц')


    class Meta:

        unique_together = ['code', 'organization']

