import django.db.models


class MyChoices(django.db.models.IntegerChoices):
    A = 1, "A"
    B = 2, "B"


set(MyChoices)
