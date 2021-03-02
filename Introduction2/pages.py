from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from . import models
from .models import Constants
import time



class pre(Page):
	def before_next_page(self):
		self.player.versionen()
		self.player.defpartvars()
	def is_displayed(self):
		return self.round_number == 1



class Anleitung(Page):
	def is_displayed(self):
		return self.round_number == 1

class treatment_pres(Page):
	def is_displayed(self):
		return self.round_number == 1


class b(Page):
	def is_displayed(self): 
		 if self.round_number == self.participant.vars['task_rounds']['A']:
		 	return True
		 else:
		 	return False

class n(Page):
	def is_displayed(self):
		if self.round_number == self.participant.vars['task_rounds']['B']:
			return True
		else: 
			return False

class m(Page):
	def is_displayed(self):
		return self.round_number == self.participant.vars['task_rounds']['C']

class p(Page):
	def is_displayed(self):
		return self.round_number == self.participant.vars['task_rounds']['D']


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
		return self.round_number == 4

class grouping(Page):
	def is_displayed(self):
		if self.participant.vars["ref"] == "other":
			if self.round_number == 4:
				return True
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

	def before_next_page(self):
		self.player.saverank()

	def is_displayed(self):
		if self.round_number == 4:
			return True
		else:
			return False


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

	def before_next_page(self):
		self.player.rankval()
		self.player.savechoi2()

	def is_displayed(self):
		if self.round_number == 4:
			return True
		else:
			return False



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

	def before_next_page(self):
		self.player.rankval()
		self.player.savechoi3()

	def is_displayed(self):
		if self.round_number == 4:
			return True
		else:
			return False



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

	def before_next_page(self):
		self.player.savechoi4()
		self.player.rankval()
		self.player.chotrea()


	def is_displayed(self):
		if self.round_number == 4:
			return True
		else:
			return False


class ranking2(Page):
	form_model=models.Player
	form_fields=["fir2","sec2","thi2","fou2"]


	def vars_for_template(self):
		question = self.player.vars_for_template()
#		question.update({'choice':if self.out==1: if self.noinc==1:
#				self.participant.vars['type']='force'self.player.in_round(self.round_number-1).pun,'wage_dis':self.player.in_round(self.round_number-1).wage, 'perf25':int(self.player.in_round(self.round_number-1).perf_others25), 'perf5':int(self.player.in_round(self.round_number-1).perf_others5), 'face':int(self.player.in_round(self.round_number-1).emo)})
		return question
#	def before_next_page(self):
#		self.player.treatments()
	#def before_next_page(self):
	#	self.player.chotrea()
	def before_next_page(self):
		self.player.saverank2()

	def is_displayed(self):
		if self.participant.vars["ref"]=="other":
			if self.round_number == 4:
				return True
			else:
				return False
		else:
			return False



class choi_22(Page):
	form_model=models.Player
	form_fields=["first21","first22","first23","first24","first25","first26","first27","first28","first29","first210","alter2_nu"]
#	def error_message(self, values):
#		if values['noinc'] + values['nudge']+ values['mon']+ values['punish']+ values['force'] != 100:
#			return 'Die Summe der Prozentzahlen muss 100 ergeben.'	

		
	def vars_for_template(self):
		question = self.player.vars_for_template()
	#	question.update({'first2': self.in_round(self.round_number-2),
	#	'second':self.in_round(self.round_number-2),
	#	'third':self.in_round(self.round_number-2).third,
	#	'fourth':self.in_round(self.round_number-2).fourth})
#		question.update({'choice':if self.out==1: if self.noinc==1:
#				
#				self.participant.vars['type']='force'self.player.in_round(self.round_number-1).pun,'wage_dis':self.player.in_round(self.round_number-1).wage, 'perf25':int(self.player.in_round(self.round_number-1).perf_others25), 'perf5':int(self.player.in_round(self.round_number-1).perf_others5), 'face':int(self.player.in_round(self.round_number-1).emo)})
		return question

#	def before_next_page(self):
#		self.player.treatments()

	def before_next_page(self):
		self.player.savechoi22()

	def is_displayed(self):
		if self.participant.vars["ref"]=="other":
			if self.round_number == 4:
				return True
			else:
				return False
		else:
			return False


class choi_23(Page):
	form_model=models.Player
	form_fields=["second21","second22","second23","second24","second25","second26","second27","second28","second29","second210","alter2_mon"]
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

	def before_next_page(self):
		self.player.savechoi23()

	def is_displayed(self):
		if self.participant.vars["ref"]=="other":
			if self.round_number == 4:
				return True
			else:
				return False
		else:
			return False 


class choi_24(Page):
	form_model=models.Player
	form_fields=["third21","third22","third23","third24","third25","third26","third27","third28","third29","third210","alter2_punish"]
#	def error_message(self, values):
#		if values['noinc'] + values['nudge']+ values['mon']+ values['punish']+ values['force'] != 100:
#			return 'Die Summe der Prozentzahlen muss 100 ergeben.'	

	def vars_for_template(self):
		question = self.player.vars_for_template()
#		question.update({'first': self.in_round(self.round_number-4).first,
#		'second':self.in_round(self.round_number-4).second,
#		'third2':self.in_round(self.round_number-4).third,
#		'fourth':self.in_round(self.round_number-4).fourth})
		return question

#	def before_next_page(self):
#		self.player.treatments()

	def before_next_page(self):
		self.player.savechoi24()



	def is_displayed(self):
		if self.participant.vars["ref"]=="other":
			if self.round_number == 4:
				return True
			else:
				return False
		else:
			return False

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
		if self.round_number == 4:
			return True
		else:
			return False

class WaitPlayer(WaitPage):
	group_by_arrival_time = True
	title_text = "Warten auf Gruppenmitglieder"
	body_text = "Btte warten Sie, bis alle Gruppenmitglieder ihre Entscheidungen getroffen haben."
	def before_next_page(self):
		self.group.selplay()
	def is_displayed(self):
		if self.round_number == 4:
			return True
		else:
			return False


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
	form_fields=["ptoday1","ptoday2","ptoday3","ptoday4","ptoday5","ptoday6","ptoday7","ptoday8","ptoday9","ptoday10","alter3"]

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
			return self.round_number == 4

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
			question.update({'pun_dis':self.player.in_round(self.round_number-1).pun,'wage_dis':(self.player.in_round(self.round_number-1).wage-25), 'perf25':int(self.player.in_round(self.round_number-1).perf_others25), 'perf5':int(self.player.in_round(self.round_number-1).perf_others5), 'face':int(self.player.in_round(self.round_number-1).emo)})
		return question

	def is_displayed(self):
		if self.participant.vars['time']=='immi':
			if self.round_number > 3:
				return self.participant.vars['expiry'] - time.time() >= 1 

		

	def before_next_page(self):
		if self.participant.vars['expiry'] - time.time() >= 1:
			self.player.calc_tree()
		else:
			self.player.calc_tree2()

		self.player.compare()


class Results(Page):
	def is_displayed(self):
		if self.participant.vars['time']=='immi':
			if self.round_number==self.participant.vars["rn"]:
				return self.participant.vars['expiry'] - time.time() < 1 
		

	def vars_for_template(self):
		question = self.player.vars_for_template()
		return question

	def before_next_page(self):
		self.player.save_payoff()











page_sequence = [
	pre,
	Anleitung,
	treatment_pres,
	b,
	n,
	m,
	p,
	control,
	grouping,
	ranking,
	choi_2,
	choi_3,
	choi_4,
	ranking2,
	choi_22,
	choi_23,
	choi_24,
]
