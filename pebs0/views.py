from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import time
import random




class A_Start(Page):
	def is_displayed(self):
		if self.round_number == 4 :
			if self.participant.vars['expiry'] - time.time() < 1:
				if   self.participant.vars["exwind"] == 1:
					return True
				else:
					return False
			else:
				return False
		else:
			return False

	def before_next_page(self):
		self.participant.vars['expiry1'] = time.time()+45
		self.player.ti()
		self.player.partvars()



#        self.subsession.start_rand()
 #       self.player.genriddle()

class B_Effort(Page):
	form_model=models.Player
	form_fields=["answer","wrong"]


#	timer_text = 'Time left to complete this task:'


#	def get_timeout_seconds(self):
#		return self.participant.vars['expiry'] - time.time()

	def answer_error_message(self,value):
		if self.player.wrong<3:
			if not (value==self.subsession.correct):
				return 'Nicht korrekt. Bitte korrigieren Sie die Eingabe. Sie haben noch ' + str(3-self.player.wrong) +' Versuche.'


	def vars_for_template(self):
		question = self.player.vars_for_template()
		return question

	def is_displayed(self):
		if self.round_number>3:
			if self.participant.vars['expiry'] - time.time() < 1:
				if self.participant.vars["exwind"] == 1:
					if self.round_number<=self.participant.vars["workload"]+3:
						return True
					else:
						return False
				else:
					return False
			else:
				return False
		else:
			return False

		

	def before_next_page(self):
		self.player.compare()
		if time.time()<self.participant.vars['expiry1']:
			if self.participant.vars["hype"]=="punish":
				self.player.calcpun()
			elif self.participant.vars["hype"]=="mon":
				self.player.calcbon()
		self.participant.vars['expiry1'] = time.time()+45
		self.player.calcres()



class don(Page):
	form_model=models.Player
	form_fields=["spendeWWF","spendeMeerPlastik","spendeMannTafel"]

	def vars_for_template(self):
		question = self.player.vars_for_template()
		return question

	def is_displayed(self):
		if self.round_number>3:
			if self.participant.vars['expiry'] - time.time() < 1:
				if self.participant.vars["exwind"] == 0:
					if self.round_number == 4:
						return True
					else:
						return False
				else:
					if self.round_number==self.participant.vars["workload"]+4:
						return True
					else:
						return False
			else:
				return False
		else:
			return False
			
	def error_message(self, values):
		try:
			if values["spendeWWF"] + values["spendeMeerPlastik"] + values["spendeMannTafel"] > 100:
				 	return 'Sie können maximal ihren gesamten auszuzahlenden Betrag spenden'
		except TypeError:
			try:
				if values["spendeMeerPlastik"] + values["spendeMannTafel"] > 100:
				 	return 'Sie können maximal ihren gesamten auszuzahlenden Betrag spenden'
			except TypeError:
				try:
					if values["spendeWWF"] + values["spendeMeerPlastik"] > 100:
						return 'Sie können maximal ihren gesamten auszuzahlenden Betrag spenden'
				except TypeError:
					try:
						if values["spendeMannTafel"] > 100:
							return 'Sie können maximal ihren gesamten auszuzahlenden Betrag spenden'
					except TypeError:
						try:
							if values["spendeMeerPlastik"] > 100:
								return 'Sie können maximal ihren gesamten auszuzahlenden Betrag spenden'
						except TypeError:
							try:
								if values["spendeWWF"] > 100:
									return 'Sie können maximal ihren gesamten auszuzahlenden Betrag spenden'
							except TypeError:
								pass
	def before_next_page(self):
		self.player.savepay()

class Results(Page):

	def vars_for_template(self):
		question = self.player.vars_for_template()
		return question

	def is_displayed(self):
		if self.round_number>3:
			if self.participant.vars['expiry'] - time.time() < 1:
				if self.participant.vars["exwind"] == 0:
					if self.round_number == 4:
						return True
					else:
						return False
				else:
					if self.round_number==self.participant.vars["workload"]+4:
						return True
					else:
						return False
			else:
				return False
		else:
			return False
		

page_sequence = [
	A_Start,
	B_Effort,
	don,
	Results,
]
