from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import time
import random

class Anleitung(Page):
	pass

class choice1(Page):
	form_model=models.Player
	form_fields=["dec11","dec21","dec31","dec41","dec51"]

	def dec11_error_message(self,value):
		if not (str(type(value))=="<class 'int'>"):
			return 'Bitte klicken Sie in die blaue Leiste um die Aufgaben aufzuteilen.'

	
	def dec21_error_message(self,value):
		if not (str(type(value))=="<class 'int'>"):
			return 'Bitte klicken Sie in die blaue Leiste um die Aufgaben aufzuteilen.'

	
	def dec31_error_message(self,value):
		if not (str(type(value))=="<class 'int'>"):
			return 'Bitte klicken Sie in die blaue Leiste um die Aufgaben aufzuteilen.'

	
	def dec41_error_message(self,value):
		if not (str(type(value))=="<class 'int'>"):
			return 'Bitte klicken Sie in die blaue Leiste um die Aufgaben aufzuteilen.'

	
	def dec51_error_message(self,value):
		if not (str(type(value))=="<class 'int'>"):
			return 'Bitte klicken Sie in die blaue Leiste um die Aufgaben aufzuteilen.'

class choice2(Page):
	form_model=models.Player
	form_fields=["dec12","dec22","dec32","dec42","dec52"]

	def dec12_error_message(self,value):
		if not (str(type(value))=="<class 'int'>"):
			return 'Bitte klicken Sie in die blaue Leiste um die Aufgaben aufzuteilen.'

	
	def dec22_error_message(self,value):
		if not (str(type(value))=="<class 'int'>"):
			return 'Bitte klicken Sie in die blaue Leiste um die Aufgaben aufzuteilen.'

	
	def dec32_error_message(self,value):
		if not (str(type(value))=="<class 'int'>"):
			return 'Bitte klicken Sie in die blaue Leiste um die Aufgaben aufzuteilen.'

	
	def dec42_error_message(self,value):
		if not (str(type(value))=="<class 'int'>"):
			return 'Bitte klicken Sie in die blaue Leiste um die Aufgaben aufzuteilen.'

	
	def dec52_error_message(self,value):
		if not (str(type(value))=="<class 'int'>"):
			return 'Bitte klicken Sie in die blaue Leiste um die Aufgaben aufzuteilen.'


class pred1(Page):
	form_model=models.Player
	form_fields=["ass11","ass21","ass31","ass41","ass51"]
	def ass11_error_message(self,value):
		if not (str(type(value))=="<class 'int'>"):
			return 'Bitte klicken Sie in die blaue Leiste um die Aufgaben aufzuteilen.'

	
	def ass21_error_message(self,value):
		if not (str(type(value))=="<class 'int'>"):
			return 'Bitte klicken Sie in die blaue Leiste um die Aufgaben aufzuteilen.'

	
	def ass31_error_message(self,value):
		if not (str(type(value))=="<class 'int'>"):
			return 'Bitte klicken Sie in die blaue Leiste um die Aufgaben aufzuteilen.'

	
	def ass41_error_message(self,value):
		if not (str(type(value))=="<class 'int'>"):
			return 'Bitte klicken Sie in die blaue Leiste um die Aufgaben aufzuteilen.'

	
	def ass51_error_message(self,value):
		if not (str(type(value))=="<class 'int'>"):
			return 'Bitte klicken Sie in die blaue Leiste um die Aufgaben aufzuteilen.'

	
class pred2(Page):
	form_model=models.Player
	form_fields=["ass12","ass22","ass32","ass42","ass52"]
	
	def ass12_error_message(self,value):
		if not (str(type(value))=="<class 'int'>"):
			return 'Bitte klicken Sie in die blaue Leiste um die Aufgaben aufzuteilen.'

	def ass22_error_message(self,value):
		if not (str(type(value))=="<class 'int'>"):
			return 'Bitte klicken Sie in die blaue Leiste um die Aufgaben aufzuteilen.'

	def ass32_error_message(self,value):
		if not (str(type(value))=="<class 'int'>"):
			return 'Bitte klicken Sie in die blaue Leiste um die Aufgaben aufzuteilen.'


	def ass42_error_message(self,value):
		if not (str(type(value))=="<class 'int'>"):
			return 'Bitte klicken Sie in die blaue Leiste um die Aufgaben aufzuteilen.'


	def ass52_error_message(self,value):
		if not (str(type(value))=="<class 'int'>"):
			return 'Bitte klicken Sie in die blaue Leiste um die Aufgaben aufzuteilen.'



class thanks(Page):
	form_model=models.Player
	form_fields=["tel","email"]



page_sequence = [Anleitung,choice1,pred1,choice2,pred2,thanks]
