from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import time
import random


class noi_Start(Page):
	def is_displayed(self):
		if self.participant.vars['tak']=='Aufgabenaufteilung':
			return self.round_number == 1 
		

	def before_next_page(self):
		self.player.calc_first_pay()

class noi_Effort(Page):
	form_model=models.Player
	form_fields=["answer"]


	timer_text = 'Time left to complete this task:'

	def answer_error_message(self,value):
		if not (value==self.subsession.solution):
			return 'Die Antwort ist nicht korrekt. Bitte korrigieren Sie die Eingabe und versuchen Sie es erneut.'

	def vars_for_template(self):
		question = self.player.vars_for_template()
		return question

	def is_displayed(self):
		if self.participant.vars["tak"]=="Aufgabenaufteilung":
			if self.participant.vars['wowe']>0:
				return self.round_number <= self.participant.vars['wowe']

		
	def before_next_page(self):
		self.player.calc_score()


class noi_Results(Page):
	def is_displayed(self):
		if self.participant.vars["tak"]=="Aufgabenaufteilung":
			return self.round_number==self.participant.vars['wowe']
		

	def vars_for_template(self):
		question = self.player.vars_for_template()
		return question

	def before_next_page(self):
		self.player.save_payoff()



class A_Start(Page):
	def is_displayed(self):
		if self.participant.vars['time']=='delay':
			if self.participant.vars['tak']=='Umweltaufgabe':
				return self.round_number == 1  

	def before_next_page(self):
		self.participant.vars['expiry'] = time.time()+300
		self.player.calc_first_pay()
		self.player.treaty()

#        self.subsession.start_rand()
 #       self.player.genriddle()

class B_Effort(Page):
	form_model=models.Player
	form_fields=["answer"]


	timer_text = 'Time left to complete this task:'


	def get_timeout_seconds(self):
		if self.participant.vars['version']=='Vorgabe':
			pass
		else:
			return self.participant.vars['expiry'] - time.time()

	def answer_error_message(self,value):
		if not (value==self.subsession.solution):
			return 'Die Antwort ist nicht korrekt. Bitte korrigieren Sie die Eingabe und versuchen Sie es erneut.'

	def vars_for_template(self):
		question = self.player.vars_for_template()
		if self.round_number>1:
			question.update({'pun_dis':self.player.in_round(self.round_number-1).pun,'wage_dis':self.player.in_round(self.round_number-1).wage, 'perf25':int(self.player.in_round(self.round_number-1).perf_others25), 'perf5':int(self.player.in_round(self.round_number-1).perf_others5), 'face':int(self.player.in_round(self.round_number-1).emo)})
		return question

	def is_displayed(self):
		if self.participant.vars['time']=='delay':
			if self.participant.vars['version']=='Vorgabe':
				if self.participant.vars['tak']=='Umweltaufgabe':
					return self.round_number <= self.subsession.in_round(1).rand_max_round
			elif self.participant.vars['version']!='Vorgabe':
				if self.participant.vars['tak']=='Umweltaufgabe':
					return self.participant.vars['expiry'] - time.time() >= 1 

		

	def before_next_page(self):
		if self.participant.vars['expiry'] - time.time() >= 1:
			self.player.calc_tree()
		else:
			self.player.calc_tree2()

		self.player.roundnumber()
		self.player.compare()


class Results(Page):
	def is_displayed(self):
		if self.participant.vars['time']=='delay':
			if self.participant.vars['version']=='Vorgabe':
				if self.participant.vars['tak']=='Umweltaufgabe':
					return self.round_number > self.subsession.in_round(1).rand_max_round
			elif self.participant.vars['version']!='Vorgabe': 
				if self.participant.vars['tak']=='Umweltaufgabe':
					return self.participant.vars['expiry'] - time.time() < 1 
		

	def vars_for_template(self):
		question = self.player.vars_for_template()
		return question

	def before_next_page(self):
		self.player.save_payoff()


#class Thanks(Page):##
##
#	def is_displayed(self):
#		if self.participant.vars['tak']=='Umweltaufgabe':
#			if self.participant.vars['time']=='delay':
#				if self.participant.vars['version']=='Vorgabe':
#					return self.round_number > self.subsession.in_round(1).rand_max_round
#				else:
#					return self.participant.vars['expiry'] - time.time() < 1
#		elif:
#			if self.participant.vars['wowe']>0:
#				return self.round_number==self.participant.vars['woto']
#			else:
#				return self.round_number==1
#


page_sequence = [
	noi_Start,
	noi_Effort,
	noi_Results,
	A_Start,
    B_Effort,
    Results,
]
