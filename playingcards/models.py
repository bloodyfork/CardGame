from django.db import models
from core.models import BaseModel
# Create your models here.


class Card(BaseModel):
    NUMBER_CHOICE = {

        '1': 'ace',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        '10': '10',
        '11': 'jack',
        '12': 'queen',
        '13': 'king',

         }

    number = models.CharField(choices=NUMBER_CHOICE)
    type_card = models.ForeignKey('TypeCard', on_delete=models.CASCADE)


class TypeCard(BaseModel):
    SYMBOL_CHOICE = {'spade': 'spade', 'club': 'club', 'diamond': 'diamond', 'heart': 'heart'}
    COLOR_CHOICE = {'black': 'black', 'red': 'red'}
    symbol = models.CharField(choices=SYMBOL_CHOICE)
    color = models.CharField(choices=COLOR_CHOICE)
