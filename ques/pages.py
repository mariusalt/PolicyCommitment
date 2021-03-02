from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
import time
import random


class tp1(Page):
	form_model=models.Player
	form_fields=["tp1","tp2","tp3","tp4","tp5"]

	def is_displayed(self):
		return self.round_number==4

class r1(Page):
	form_model=models.Player
	form_fields=["r1","r2","r3","r4","r5"]
	def is_displayed(self):
		return self.round_number==4

class WaitPlayer1(WaitPage):
	group_by_arrival_time = True
	title_text = "Warten auf andere Teilnehmende"
	body_text = "Bitte warten Sie bis andere Teilnehmende ihre Entscheidungen getroffen haben."

	def is_displayed(self):
		return self.round_number == 4

class others(Page):
	form_model=models.Player
	form_fields=["firsto","secondo","thirdo","fourtho"]
	def is_displayed(self):
		return self.round_number==4



class Questionnaire(Page):
	form_model=models.Player
	form_fields=["wrsl1","wrsl2","wrsl3","wrsl4","wrsl5","scu","nitrat","ot1","ot2","ot3","ot4","guessA","guessB","guessC","guessD","pkw","encon","flight","ra1","ra2","ra3","ra4","ra5","ra6","ra11","ra12","ra13","ra14","ra15","ra16","ra17","abcd","member","wg","patern1","patern2","patern3","patern4","patern5","patern6","patern7","patern8","patern9","patern10","tryans","dec11","dec21","dec31","dec41","dec51",'makesense','sc1','sc2','sc3','sc4','sc5','sc6','sc7','sc8','sc9','sc10','sc11','sc12','sc13','smoke','alc','bmi','psuswit','wsuswit','palswit','walswit','ptaswit','wtaswit','pcrswit','wcrswit','contri','c0','c1','c2','c3','c4','c5','c6','c7','c8','c9','c10','c11','c12','c13','c14','c15','c16','c17','c18','c19','c20','rank1','rank2','rank3','rank4',"r1","r2","r3","r4","r5","tp1","tp2","tp3","tp4","tp5",'exhaust1','altru1','altru2','Env1','Env2','Env3','Env4','Env5','Env6','Env7','Env8','Env9','Donation1','Donation2', 'gender','age', 'language', 'party','income']#,'recall1','recall2','volun', 'uni','exhaust1']

	def c1_max(self):
		return 20
	def c2_max(self):
		return 20
	def c3_max(self):
		return 20
	def c4_max(self):
		return 20
	def c5_max(self):
		return 20
	def c6_max(self):
		return 20
	def c7_max(self):
		return 20
	def c8_max(self):
		return 20
	def c9_max(self):
		return 20
	def c10_max(self):
		return 20
	def c11_max(self):
		return 20
	def c12_max(self):
		return 20
	def c13_max(self):
		return 20
	def c14_max(self):
		return 20
	def c15_max(self):
		return 20
	def c16_max(self):
		return 20
	def c17_max(self):
		return 20
	def c18_max(self):
		return 20
	def c19_max(self):
		return 20
	def c20_max(self):
		return 20


	def vars_for_template(self):
		question = self.player.vars_for_template()
		return question

	def before_next_page(self):
		self.player.decextra()
		self.player.la()
		self.player.guesst()

	def is_displayed(self):
		if self.participant.vars['expiry'] - time.time() < 1:
			return self.round_number==4

class mod(Page):
	form_model=models.Player
	form_fields=["eins","zwei","drei","vier"]

	def before_next_page(self):
		self.player.decextra1()
	def is_displayed(self):
		if self.participant.vars['expiry'] - time.time() < 1:
			if self.round_number==4:
				return True
			else:
				return False
		else:
			return False

class WaitPlayer2(WaitPage):
	def after_all_players_arrive(self):
		self.group.set_payoff()
	def is_displayed(self):
		if self.participant.vars['expiry'] - time.time() < 1:
			return self.round_number==4


class A_Start(Page):
	def is_displayed(self):
		if self.player.exwind == 1:
			return self.round_number == 1  

	def before_next_page(self):
		self.player.ti()

		


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
		if self.player.exwind == 1:
			return self.round_number<=self.participant.vars["workload"]

		

	def before_next_page(self):
		self.player.calcres()
		self.player.compare()
		if time.time()<self.participant.vars['expiry']:
			if self.participant.vars["hype"]=="punish":
				self.player.calcpun()
			elif self.participant.vars["hype"]=="mon":
				self.player.calcbon()
		self.participant.vars['expiry'] = time.time()+45



class Results(Page):
	def vars_for_template(self):
		question = self.player.vars_for_template()
		return question

	def is_displayed(self):
		if self.player.exwind == 1:
	 		return self.round_number==self.participant.vars["workload"]

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
	WaitPlayer1,
	others,
	Questionnaire,
	mod,
	WaitPlayer2,

]

