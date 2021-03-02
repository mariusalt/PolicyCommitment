from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from . import models
from .models import Constants
import time




class WaitPlayer(WaitPage):
	group_by_arrival_time = True
	title_text = "Warten auf andere Teilnehmende"
	body_text = "Bitte warten Sie, bis alle Teilnehmende ihre Entscheidungen getroffen haben."

	def is_displayed(self):
		if self.round_number == 4:
			return True
		else:
			return False
	def after_all_players_arrive(self):
		self.group.now()


class group(Page):
	def is_displayed(self):
		if self.participant.vars["ref"]=="other":
			if self.round_number == 4:
				return True
			else:
				return False
		else:
			return False


class pre1(Page):
	def is_displayed(self):
		return self.round_number == 4



class motbel(Page):
	form_model=models.Player
	form_fields=["mot1","mot2","mot3","mot4","mot5"]

	def is_displayed(self):
		if self.round_number == 4:
			return True
		else:
			return False


class perbel(Page):
	form_model=models.Player
	form_fields=["belper"]
	


	def is_displayed(self):
		if self.round_number == 4:
			return True
		else:
			return False



class choice1(Page):
	form_model=models.Player
	form_fields=["tryans","dec11","dec21","dec31","dec41","dec51"]

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

	def vars_for_template(self):
		question = self.player.vars_for_template()
		return question

	def before_next_page(self):
		self.player.decsave1()
		self.player.seltask()
	def is_displayed(self):
		if self.round_number == 4:
			return True
		else:
			return False


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

	def before_next_page(self):
		self.player.asssave1()
		self.player.seltask()

	def is_displayed(self):
		if self.round_number == 4:
			return True
		else:
			return False


class Paysplit(Page):
	form_model=models.Player
	form_fields=["ptoday1","ptoday2","ptoday3","ptoday4","ptoday5","ptoday6","ptoday7","ptoday8","ptoday9","ptoday10","ptoday11","alter3"]

	def vars_for_template(self):
		question = self.player.vars_for_template()
		return question


	def before_next_page(self):
		self.player.calc_todaypay()
	def is_displayed(self):
		if self.round_number == 4:
			return True
		else:
			return False



class A_Start(Page):
	def is_displayed(self):
		if self.participant.vars['time']=='immi':
			return self.round_number == 1  

	def before_next_page(self):
		self.participant.vars['expiry'] = time.time()+480
		self.player.calc_first_pay()
		self.player.treaty()
		self.player.ti()

	def is_displayed(self):
		if self.participant.vars['time']=='immi':
			if self.round_number == 4:
				return True
			else:
				return False
		else:
			return False

#        self.subsession.start_rand()
 #       self.player.genriddle()

class B_Effort(Page):
	form_model=models.Player
	form_fields=["answer"]


	timer_text = 'Time left to complete this task:'


	def get_timeout_seconds(self):
		return self.participant.vars['expiry'] - time.time()

	def answer_error_message(self,value):
		if not (value==self.subsession.solution):
			return 'Die Antwort ist nicht korrekt. Bitte korrigieren Sie die Eingabe und versuchen Sie es erneut.'

	def vars_for_template(self):
		question = self.player.vars_for_template()
		if self.round_number>1:
			question.update({'pun_dis':self.player.in_round(self.round_number-1).pun,'wage_dis':(self.player.in_round(self.round_number-1).wage), 'perf25':int(self.player.in_round(self.round_number-1).perf_others25), 'perf5':int(self.player.in_round(self.round_number-1).perf_others5), 'face':int(self.player.in_round(self.round_number-1).emo)})
		return question

	def is_displayed(self):
		if self.participant.vars['time']=='immi':
			if self.round_number > 3:
				if self.participant.vars['expiry'] - time.time() >= 1:
					return True
				else:
					return False
			else:
				return False
		else: 
			return False

		

	def before_next_page(self):
		if self.participant.vars['expiry'] - time.time() >= 0:
			self.player.calc_tree()
		else:
			pass

		self.player.compare()
		self.participant.vars["rn"]=self.round_number


class Results(Page):
	def is_displayed(self):
		if self.participant.vars['time']=='immi':
			if self.participant.vars['expiry'] - time.time() < 1:
				if self.round_number==self.participant.vars["rn"]:
					return True
				else:
					return False
			elif self.round_number==44:
				if self.round_number==self.participant.vars["rn"]:
					return True
				else:
					return False
			else:
				return False
		else: 
			return False

	def vars_for_template(self):
		question = self.player.vars_for_template()
		return question

	def before_next_page(self):
		self.player.save_payoff()











page_sequence = [
	WaitPlayer,
	group,
	motbel,
	perbel,
	#choice2,
	#pred2,
	pre1,
	choice1,
	pred1,
	Paysplit,
	A_Start,
	B_Effort,
	Results,
]
