from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
import time


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'Introduction0'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
#    def creating_session(self):
#    	players = self.get_players()
#    	for p in players:
#	    	t=random.choice([1,2])
#	    	if t==1:
#	    		p.t1='immi'
#				p.participant.vars['time']='immi'
#			else:
#				p.t1='delay'
#				p.participant.vars['time']='delay'
#			b=random.choice([1,2])
#	    	if b==1:
#	    		p.t2='self'
#				p.participant.vars['ref']='self'
#			else:
#				p.t2='other'
#				p.participant.vars['ref']='other'
	pass	


class Group(BaseGroup):
    pass


class Player(BasePlayer):
	t1 = models.StringField(
		choices=['immi','delay'],
		widget=widgets.RadioSelect
		)
	t2=models.StringField(
		choices=['self','other'],
		widget=widgets.RadioSelect
		)
	time1 = models.FloatField()
	time11 = models.FloatField()

	notime = models.IntegerField(choices=[[0,'Ich habe keine terminlichen Konflikte bezüglich der Bearbeitung von Teil 2 und 3'],
		[1,'Die Bearbeitung von Teil 2 und 3 ist mir aus terminlichen Gründen nicht möglich']],
		widget=widgets.RadioSelect
		)


	def endow(self):
		self.participant.vars['endowment']=5

	def treatments1(self):
		if self.t1=='immi':
			self.participant.vars['time']='immi'
		else:
			self.participant.vars['time']='delay'

	def treatments2(self):
		if self.t2=='self':
			self.participant.vars['ref']='self'
		else:
			self.participant.vars['ref']='other'