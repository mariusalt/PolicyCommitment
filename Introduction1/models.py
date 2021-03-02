from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
	Currency as c, currency_range
)
import random
import time
import numpy as np
import itertools


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
	name_in_url = 'Introduction'
	players_per_group = None
	num_rounds = 1


class Subsession(BaseSubsession):
	def creating_session(self):
		players = self.get_players()
		num_group = len(players)/2
		s1=random.choice([0.5,-0.5])
		if (len(players) % 2) != 0:
			num_group1=num_group+s1
			num_group2=num_group-s1
		else:
			num_group1=num_group
			num_group2=num_group			
		s2=random.choice([1,-1])
		if (num_group2 % 2) != 0:
			num_group1=num_group1+s2
			num_group2=num_group2-s2
		if (num_group2 % 8) == 0:
			gr2=num_group2/2
			gr4=num_group2/2
		else:
			s3=np.random.choice(np.arange(0, 2), p=[0.6, 0.4])
			gr2=0
			gr4=0
			num_group21=num_group2
			if int(s3)==0 and int(num_group21)>=2:
				while num_group21>0:
					if num_group21>=4:
						gr4=gr4+4
						num_group21=num_group21-4
					if num_group21>=2:
						gr2=gr2+2
						num_group21=num_group21-2
					if num_group21>=2:
						gr2=gr2+2
						num_group21=num_group21-2
			elif int(s3)==1 and int(num_group21)>=2:
				while num_group21>0:
					if num_group21>=2:
						gr2=gr2+2
						num_group21=num_group21-2
					if num_group21>=2:
						gr2=gr2+2
						num_group21=num_group21-2
					if num_group21>=4:
						gr4=gr4+4
						num_group21=num_group21-4
			else:
				gr2=0
				gr4=0

		pself=players[:int(num_group1)]
		if num_group2>0:
			pother=players[-int(num_group2):]

			pgr2=pother[:int(gr2)]
			if gr4>0:
				pgr4=pother[-int(gr4):]
			else:
				pgr4=[]

		else:
			pother=[]
			pgr2=[]
			pgr4=[]


		s5=itertools.cycle(['immi','immi','delay','delay'])
		s6=itertools.cycle(['delay','delay','immi','immi'])
		s7=itertools.cycle(['delay','delay','delay','delay','immi','immi','immi','immi'])
		s8=itertools.cycle(['immi','immi','immi','immi','delay','delay','delay','delay'])
		so1=random.choice([0,1])
		for p in pself:
			p.t2 = "self"
			p.participant.vars["ref"]=p.t2
			s4=random.choice([0,1])
			p.t1="immi" if s4==0 else "delay"
			p.participant.vars["time"]=p.t1
			p.gr = 0
			p.participant.vars["gr"]=p.gr
		for p in pother:
			p.t2 = "other"
			p.participant.vars["ref"]=p.t2
		for p in pgr2:
			p.gr = 2
			p.participant.vars["gr"]=p.gr
			if so1==0:
				p.t1=next(s5)
				p.participant.vars["time"]=p.t1
			else:
				p.t1=next(s6)
				p.participant.vars["time"]=p.t1
		for p in pgr4:
			p.gr = 4
			p.participant.vars["gr"]=p.gr
			if so1==0:
				p.t1=next(s7)
				p.participant.vars["time"]=p.t1
			else:
				p.t1=next(s8)
				p.participant.vars["time"]=p.t1


		# group_matrix = []

		# for i in range(int(num_group1)-1):
		# 	while len(pself)>0:
		# 		new_group = [pself.pop()]
		# 		group_matrix.append(new_group)

		# lengr2=gr2/2
		# for i in range(int(gr2)-1):
		# 	while len(pgr2)>1:
		# 		new_group = [
		# 			pgr2.pop(),
		# 			pgr2.pop()
		# 		]
		# 		group_matrix.append(new_group)

		# lengr4=gr2/4
		# for i in range(int(gr4)-1):
		# 	while len(pgr4)>3:
		# 		new_group = [
		# 			pgr4.pop(),
		# 			pgr4.pop(),
		# 			pgr4.pop(),
		# 			pgr4.pop()
		# 		]
		# 		group_matrix.append(new_group)

		# self.set_group_matrix(group_matrix)



class Group(BaseGroup):
	pass


class Player(BasePlayer):
	t1 = models.StringField()
	t2=models.StringField()
	gr=models.IntegerField()
	time1 = models.FloatField()
	time11 = models.FloatField()
	notime = models.IntegerField(choices=[[0,'Ich habe keine terminlichen Konflikte bezüglich der Bearbeitung von Teil 2'],
		[1,'Die Bearbeitung von Teil 2 ist mir aus terminlichen Gründen nicht möglich']],
		widget=widgets.RadioSelect
		)


	def endow(self):
		self.participant.vars['endowment']=17
		self.participant.vars['payoff1']=17
		self.participant.vars["treecount"]=0
		self.participant.vars["expiry"]=0

	