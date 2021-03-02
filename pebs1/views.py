from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import time
import random


class A_Start(Page):
	def is_displayed(self):
		return self.round_number == 1

	def before_next_page(self):
		self.player.partvars()

class B_Effort(Page):
	form_model=models.Player
	form_fields=["answer"]


	def answer_error_message(self,value):
		if not (value==self.subsession.solution):
			return 'Die Antwort ist nicht korrekt. Bitte korrigieren Sie die Eingabe und versuchen Sie es erneut.'

	def vars_for_template(self):
		question = self.player.vars_for_template()
		return question
		
	def is_displayed(self):
		return self.round_number <= self.subsession.in_round(1).rand_max_round

	def before_next_page(self):
		self.player.roundnumber()
		self.player.tim21()
		self.player.calc_tree()


class Results(Page):
	def is_displayed(self):
		return self.round_number == self.subsession.in_round(1).rand_max_round
		

	def vars_for_template(self):
		question = self.player.vars_for_template()
		return question

	def before_next_page(self):
		self.player.roundnumber()
		self.player.tim22()


page_sequence = [
    B_Effort,
]
