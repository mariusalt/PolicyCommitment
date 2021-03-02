from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
	Currency as c, currency_range
)
import random
from random import randint
import time


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
	name_in_url = 'Introduction01'
	players_per_group = None
	num_rounds = 1


class Subsession(BaseSubsession):
	pass


class Group(BaseGroup):
	pass


class Player(BasePlayer):
	dec11 = models.IntegerField()
	dec12 = models.IntegerField()
	dec21 = models.IntegerField()
	dec22 = models.IntegerField()
	dec31 = models.IntegerField()
	dec32 = models.IntegerField()
	dec41 = models.IntegerField()
	dec42 = models.IntegerField()
	dec51 = models.IntegerField()
	dec52 = models.IntegerField()
	ass11 = models.IntegerField()
	ass12 = models.IntegerField()
	ass21 = models.IntegerField()
	ass22 = models.IntegerField()
	ass31 = models.IntegerField()
	ass32 = models.IntegerField()
	ass41 = models.IntegerField()
	ass42 = models.IntegerField()
	ass51 = models.IntegerField()
	ass52 = models.IntegerField()
	tel = models.StringField(blank=True)
	email = models.StringField(blank=True)


