from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from . import models
from .models import Constants
import time


class forward(Page):
	def before_next_page(self):
		self.participant.vars['expiry'] = 0
		self.participant.vars['tout']=time.time()
	def is_displayed(self):
		if self.participant.vars['time']=='immi':
			if self.round_number==4:
				return True
			else:
				return False
		else:
			return False


class Instr(Page):

	def before_next_page(self):
		self.player.chotreanosec()
		self.participant.vars['tout']=time.time()

	def is_displayed(self):
		if self.round_number==1:
			if self.participant.vars['time']=='delay':
				return True
			else:
				return False
		else:
			return False

class Anleitung(Page):
	def is_displayed(self):
		if self.round_number==1:
			if self.participant.vars['time']=='delay':
				if self.participant.vars["sechoi"]==1:
					return True
				else:
					return False
			else:
				return False
		else:
				return False		
class b(Page):
	def is_displayed(self):
		if self.participant.vars['time']=='delay':
			if self.participant.vars["sechoi"]==1:
				if self.round_number == self.participant.vars['noinc']:
					return True
				else:
					return False
			else:
				return False
		else:
				return False

class n(Page):
	def is_displayed(self):
		if self.participant.vars['time']=='delay':
			if self.participant.vars["sechoi"]==1:
				if self.round_number == self.participant.vars['nudge']:
					return True
				else:
					return False
			else:
				return False
		else:
				return False

class m(Page):
	def is_displayed(self):
		if self.participant.vars['time']=='delay':
			if self.participant.vars["sechoi"]==1:
				if self.round_number == self.participant.vars['mon']:
					return True
				else:
					return False
			else:
				return False
		else:
				return False

class p(Page):
	def is_displayed(self):
		if self.participant.vars['time']=='delay':
			if self.participant.vars["sechoi"]==1:
				if self.round_number == self.participant.vars['punish']:
					return True
				else:
					return False
			else:
				return False
		else:
				return False


class control(Page):
	form_model=models.Player
	form_fields=["Q1_1","Q1_2","Q1_3","Q1_4","Q2","Q3","Q4","Q5","Q6","Q7","wrong"]

	
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

	def is_displayed(self):
		if self.participant.vars['time']=='delay':
			if self.round_number==4 :
				if self.participant.vars["sechoi"]==1:
					return True
				else:
					return False
			else:
				return False
		else:
				return False


class ranking(Page):
	form_model=models.Player
	form_fields=["first","second","third","fourth"]


	def vars_for_template(self):
		question = self.player.vars_for_template()
#		question.update({'choice':if self.out==1: if self.noinc==1:
#				self.participant.vars['type']='force'self.player.in_round(self.round_number-1).pun,'wage_dis':self.player.in_round(self.round_number-1).wage, 'perf25':int(self.player.in_round(self.round_number-1).perf_others25), 'perf5':int(self.player.in_round(self.round_number-1).perf_others5), 'face':int(self.player.in_round(self.round_number-1).emo)})
		return question
#	def before_next_page(self):
#		self.player.treatments()
	#def before_next_page(self):
	#	self.player.chotrea()
	def is_displayed(self):
		if self.participant.vars['time']=='delay':
			if self.round_number==4 :
				if self.participant.vars["sechoi"]==1:
					return True
				else:
					return False
			else:
				return False
		else:
				return False

	def before_next_page(self):
		self.player.saverank()


class choi_2(Page):
	form_model=models.Player
	form_fields=["first1","first2","first3","first4","first5","first6","first7","first8","first9","first10","alter_nu"]
#	def error_message(self, values):
#		if values['noinc'] + values['nudge']+ values['mon']+ values['punish']+ values['force'] != 100:
#			return 'Die Summe der Prozentzahlen muss 100 ergeben.'	

		
	def vars_for_template(self):
		question = self.player.vars_for_template()
	#	question.update({'first': self.in_round(self.round_number-2),
	#	'second':self.in_round(self.round_number-2),
	#	'third':self.in_round(self.round_number-2).third,
	#	'fourth':self.in_round(self.round_number-2).fourth})
#		question.update({'choice':if self.out==1: if self.noinc==1:
#				
#				self.participant.vars['type']='force'self.player.in_round(self.round_number-1).pun,'wage_dis':self.player.in_round(self.round_number-1).wage, 'perf25':int(self.player.in_round(self.round_number-1).perf_others25), 'perf5':int(self.player.in_round(self.round_number-1).perf_others5), 'face':int(self.player.in_round(self.round_number-1).emo)})
		return question

#	def before_next_page(self):
#		self.player.treatments()
		
	def is_displayed(self):
		if self.participant.vars['time']=='delay':
			if self.round_number==4 :
				if self.participant.vars["sechoi"]==1:
					return True
				else:
					return False
			else:
				return False
		else:
				return False

	def before_next_page(self):
		self.player.savechoi2()


class choi_3(Page):
	form_model=models.Player
	form_fields=["second1","second2","second3","second4","second5","second6","second7","second8","second9","second10","alter_mon"]
#		if values['noinc'] + values['nudge']+ values['mon']+ values['third']+ values['force'] != 100:
#			return 'Die Summe der Prozentzahlen muss 100 ergeben.'	

	def vars_for_template(self):
		question = self.player.vars_for_template()
#		question.update({'first': self.in_round(self.round_number-3).first,
#		'second':self.in_round(self.round_number-3).second,
#		'third':self.in_round(self.round_number-3).third,
#		'fourth':self.in_round(self.round_number-3).fourth})
		return question

#	def before_next_page(self):
#		self.player.treatments()
		
	def is_displayed(self):
		if self.participant.vars['time']=='delay':
			if self.round_number==4 :
				if self.participant.vars["sechoi"]==1:
					return True
				else:
					return False
			else:
				return False
		else:
				return False

	def before_next_page(self):
		self.player.savechoi3()


class choi_4(Page):
	form_model=models.Player
	form_fields=["third1","third2","third3","third4","third5","third6","third7","third8","third9","third10","alter_punish"]
#	def error_message(self, values):
#		if values['noinc'] + values['nudge']+ values['mon']+ values['punish']+ values['force'] != 100:
#			return 'Die Summe der Prozentzahlen muss 100 ergeben.'	

	def vars_for_template(self):
		question = self.player.vars_for_template()
#		question.update({'first': self.in_round(self.round_number-4).first,
#		'second':self.in_round(self.round_number-4).second,
#		'third':self.in_round(self.round_number-4).third,
#		'fourth':self.in_round(self.round_number-4).fourth})
		return question

#	def before_next_page(self):
#		self.player.treatments()
		
	def is_displayed(self):
		if self.participant.vars['time']=='delay':
			if self.round_number==4 :
				if self.participant.vars["sechoi"]==1:
					return True
				else:
					return False
			else:
				return False
		else:
				return False

	def before_next_page(self):
		self.player.savechoi4()
		self.player.chotrea()

class WaitPage3(WaitPage):
	title_text = "Warten auf andere Teilnehmende"
	body_text = "Btte warten Sie, bis alle Teilnehmenden Ihre Entscheidungen getroffen haben."
	def after_all_players_arrive(self):
		self.group.now()
		self.group.weekrel()

	def is_displayed(self):
		if self.participant.vars['time']=='delay':
			if self.round_number==4 :
				if self.participant.vars["sechoi"]==1:
					return True
				else:
					return False
			else:
				return False
		else:
				return False


class motbel(Page):
	form_model=models.Player
	form_fields=["mot1","mot2","mot3","mot4","mot5"]

	def is_displayed(self):
		if self.round_number==4:
			if self.participant.vars['time']=='delay':
				return True
			else:
				return False
		else:
			return False
	

class perbel(Page):
	form_model=models.Player
	form_fields=["belper"]

	def is_displayed(self):
		if self.round_number==4 :
			if self.participant.vars['time']=='delay':
				return True
			else:
				return False
		else:
			return False
	def before_next_page(self):
		self.player.savebel()
	





class A_Start(Page):
	def is_displayed(self):
		if self.participant.vars['time']=='delay':
			if self.round_number == 4:
				return True
			else:
				return False
		else:
			return False

	def before_next_page(self):
		self.participant.vars['expiry'] = time.time()+480
		self.player.calc_first_pay()
		self.player.treaty()
		self.player.ti()
		self.participant.vars["rnumber"]=self.round_number

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
			if self.round_number>3:
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

		self.player.roundnumber()
		self.player.compare()
		self.participant.vars["rnumber"]=self.round_number


class Results(Page):
	def is_displayed(self):
		if self.participant.vars['time']=='delay':
			if self.round_number>3:
				if self.participant.vars['expiry'] - time.time() <= 1:
					if self.participant.vars["rnumber"]==self.round_number:
						return True
					else:
						return False
				elif self.round_number==50:
					if self.participant.vars["rnumber"]==self.round_number:
						return True
					else:
						return False
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
		self.participant.vars['tout']=time.time()










page_sequence = [
	forward,
	Instr,
	Anleitung,
	b,
	n,
	m,
	p,
	control,
	ranking,
	choi_2,
	choi_3,
	choi_4,
	WaitPage3,
	motbel,
	perbel,
	A_Start,
    B_Effort,
    Results,
]
