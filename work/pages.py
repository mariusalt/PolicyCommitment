from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from . import models
from .models import Constants


class prep2(Page):
	pass

class Anleitung2(Page):
	def before_next_page(self):
		self.player.modi()

class choice2(Page):
	form_model=models.Player
	form_fields=["worktoday","workweek"]

	def error_message(self, values):
		if values['worktoday'] + values['workweek'] != 30:
			return 'Die Summe der Aufgaben an den beiden Tagen muss 30 ergeben.'


class choice2_1(Page):
	form_model=models.Player
	form_fields=["devup1","devup2","devup3","devup4","devup5","devup6","devup7","devup8","devup9","alter1","devdown1","devdown2","devdown3","devdown4","devdown5","devdown6","devdown7","devdown8","devdown9","alter1","alter2"]

	def vars_for_template(self):
		question = self.player.vars_for_template()
		return question
	def before_next_page(self):
		self.player.choice_dev()

class result(Page):


	def vars_for_template(self):
		question = self.player.vars_for_template()
		return question




page_sequence = [	
	prep2,
	Anleitung2,
	choice2,
	choice2_1,#
	result]
