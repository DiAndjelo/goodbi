from django.db import models


class Passenger(models.Model):
    """ Titanic passenger model
    """
    survived = models.BooleanField(verbose_name='Survived', default=True)
    pclass = models.IntegerField(verbose_name='Passenger class', default=0)
    name = models.CharField(verbose_name='Name', max_length=128)
    sex = models.CharField(verbose_name='Sex', max_length=64)
    age = models.IntegerField(verbose_name='Age')
    sib_sp = models.IntegerField(verbose_name='SibSp', default=0)
    parch = models.CharField(verbose_name='Parch', max_length=128)
    ticket = models.CharField(verbose_name='Ticket', max_length=128)
    fare = models.CharField(verbose_name='Fare', max_length=128)
    cabin = models.CharField(verbose_name='Cabin', max_length=128)
    embarked = models.CharField(verbose_name='Embarked', max_length=128)

    def __str__(self):
        return self.name
