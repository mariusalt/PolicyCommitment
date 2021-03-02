from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import time
import random



class Introduction(Page):
	form_model=models.Player
	form_fields=["answer","wrong"]

	def vars_for_template(self):
		question = self.player.vars_for_template()
		return question
	def is_displayed(self):
		if self.round_number == 1:
			return True
		else:
			return False
	def answer_error_message(self,value):
		if not (value==self.subsession.correct):
			return 'The answer was not correct.'


class control(Page):
	form_model=models.Player
	form_fields=["Q1_1","Q1_2","Q1_3","Q1_4","Q2","Q3","Q4","Q5","Q6","Q7","Q8","wrong"]

	
#	def error_message(self,values):
#		if ((values['Q1_1']**values['Q1_2']) + values['Q1_3']) / values['Q1_4'] + values['Q1_5'] != 126:
#			self.player.wrong +=1
#			return 'Die Antwort ist leider nicht korrekt.'
	def Q1_1_error_message(self,value):
		if not (value==3):
			return 'Das zu der Nummer gehörige Bild entspricht nicht der zugehörigen Version.'
			self.player.wrong +=1
	def Q1_2_error_message(self,value):
		if not (value==4):
			return 'Das zu der Nummer gehörige Bild entspricht nicht der zugehörigen Version.'
			self.player.wrong +=1
	def Q1_3_error_message(self,value):
		if not (value==1):
			return 'Das zu der Nummer gehörige Bild entspricht nicht der zugehörigen Version.'
			self.player.wrong +=1
	def Q1_4_error_message(self,value):
		if not (value==2):
			return 'Das zu der Nummer gehörige Bild entspricht nicht der zugehörigen Version.'
			self.player.wrong +=1			


	def Q2_error_message(self,value):
		if not (value==2):
			return 'Die Antwort ist leider nicht korrekt.'
			self.player.wrong +=1

	def Q3_error_message(self,value):
		if not (value==3):
			return 'Die Antwort ist leider nicht korrekt.'
			self.player.wrong +=1  

	def Q4_error_message(self,value):
		if not (value==1): 
			return 'Die Antwort ist leider nicht korrekt.'
			self.player.wrong +=1

	def Q5_error_message(self,value):
		if not (value==4):
			return 'Die Antwort ist leider nicht korrekt.'
			self.player.wrong +=1

	def Q6_error_message(self,value):
		if not (value==1):
			return 'Die Antwort ist leider nicht korrekt.'
			self.player.wrong +=1

	def Q7_error_message(self,value):
		if not (value==2):
			return 'Die Antwort ist leider nicht korrekt.'
			self.player.wrong +=1	

	def Q8_error_message(self,value):
		if not (value==1):
			return 'Die Antwort ist leider nicht korrekt.'
			self.player.wrong +=1

	def is_displayed(self):
		if self.round_number == 1:
			return True
		else:
			return False


class A_Start(Page):
	def is_displayed(self):
		if self.round_number == 1:
			return True
		else:
			return False



#        self.subsession.start_rand()
 #       self.player.genriddle()

class B_Effort(Page):
	form_model=models.Player
	form_fields=["answer","wrong"]


#	timer_text = 'Time left to complete this task:'


#	def get_timeout_seconds(self):
#		return self.participant.vars['expiry'] - time.time()

	def answer_error_message(self,value):
		if not (value==self.subsession.correct):
			return 'The answer was not correct.'


	def vars_for_template(self):
		question = self.player.vars_for_template()
		return question

	def is_displayed(self):
		if self.round_number>1:	
			if self.round_number<=51:
				return True
			else:
				False
		else:
			False

		





class Results(Page):
	def vars_for_template(self):
		question = self.player.vars_for_template()
		return question

	def is_displayed(self):
		if self.round_number==52:
			return True
		else:
			False

page_sequence = [
	Introduction,
	A_Start,
	B_Effort,
	Results,
]
