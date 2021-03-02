from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
	Currency as c, currency_range
)
import random
from random import randint
import time
import itertools
import numpy as np

author = 'Marius Alt'

doc = """
Pro-Environmental Behavioral Spillover Experiment
"""


class Constants(BaseConstants):
	name_in_url = 'pebs'
	players_per_group = None
	num_rounds = 30


class Subsession(BaseSubsession):
	rand_max_round = models.IntegerField()
	solution = models.StringField()
	question = models.StringField()
	code1 = models.StringField()
	code=models.StringField()
	def creating_session(self):
		self.rand_max_round=random.choice([10])
		for i in range(31):
			if self.round_number == i:
				Letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
				Numbers = [0,1,2,3,4,5,6,7,8,9]
				random.shuffle(Letters)
				random.shuffle(Numbers)
				Let=Letters[:11]    
				Num=Numbers[:11]    
				Codes = dict(zip(Num,Let))
				new = ""
				new1 = ""
				new2 = ""
				new3 = ""
				for x in Let: 
					new += x
				for x in Num: 
					new1 += str(x)
				self.code1=new
				self.code=new1
				numsub=[]
				tur=[i for i in range(10)]
				random.shuffle(tur)
				turn = itertools.cycle(tur)
				for i in range(7):
					b=next(turn)
					k=Num[b]
					numsub.append(k)
				letsub=[]
				for i in range(7):
					m=Codes[numsub[i]]
					letsub.append(m)
				for x in numsub: 
					new2 += str(x)
				self.question=new2
				for x in letsub: 
					new3 += str(x)
				self.solution=new3

class Group(BaseGroup):
	pass

class Player(BasePlayer):
	TreeCount=models.FloatField(initial=0)
	answer = models.StringField()
	wage=models.IntegerField(initial=5)
	treatment=models.StringField()
	runde=models.IntegerField(initial=0)
	indicator=models.IntegerField(initial=0)
	emo=models.IntegerField(initial=2)
	perf_others25=models.FloatField(initial=0)
	perf_others5=models.FloatField(initial=0)
	time=models.FloatField()
	pun=models.FloatField(initial=10)

	def calc_first_pay(self):
		self.payoff=self.participant.vars['endowment']
		self.participant.vars['start'] = time.time()

	def treaty(self):
		self.treatment=self.participant.vars['type']

	def calc_first_pay(self):
		self.payoff=self.participant.vars['endowment']
		self.participant.vars['start'] = time.time()

	def calc_tree(self):
		self.TreeCount=self.round_number/2
		if self.participant.vars['type']=='mon':
			if self.round_number==1:
				self.payoff=self.participant.vars['endowment']
			else:
				self.wage=self.in_round(self.round_number-1).wage+5
				self.payoff=self.participant.vars['endowment']+self.wage/100
		else:
			self.payoff=self.participant.vars['endowment']

		if self.participant.vars['type']=='punish':
			if self.round_number==1:
				self.payoff=self.participant.vars['endowment']-self.pun
				self.pun=self.pun-1
			else:
				self.pun=self.in_round(self.round_number-1).pun-1
				self.payoff=self.participant.vars['endowment']-self.pun
		else:
			self.payoff=self.participant.vars['endowment']
		
	def calc_tree2(self):
		if self.round_number==1:
			self.TreeCount=0
			self.payoff=self.participant.vars['endowment']
		else:
			self.TreeCount=self.in_round(self.round_number-1).TreeCount

		if self.participant.vars['type']=='mon':
			if self.round_number==1:
				self.wage=0
				self.payoff=self.participant.vars['endowment']
			else:
				self.wage=self.in_round(self.round_number-1).wage
				self.payoff=self.participant.vars['endowment']+self.in_round(self.round_number-1).wage/10
		else:
			self.payoff=self.participant.vars['endowment']



	def save_payoff(self):
		self.participant.vars['pay']=self.payoff

	def roundnumber(self):
		self.runde=self.round_number
		if self.round_number==self.subsession.in_round(1).rand_max_round:
			self.indicator=1

	def compare(self):
		self.time=int(round(time.time()-self.participant.vars['start']))
		perf5={25:5,35:7.5,40:10,50:12.5,65:15,75:17.5,85:20,95:22.5,110:25,120:27.5,135:30,145:32.5,160:35,170:37.5,180:40,200:42.5,240:45,260:47.5,300:50,320:52.5,360:55,380:57.5,420:60,440:62.5,480:65,500:67.5,560:70}
		perf25={20:5,28:7.5,35:10,42:12.5,50:15,58:17.5,66:20,74:22.5,84:25,93:27.5,102:30,110:32.5,118:35,126:37.5,135:40,144:42.5,154:45,163:47.5,175:50,185:52.5,195:55,205:57.5,215:60,225:62.5,235:65,245:67.5,260:70}
		for key,value in perf25.items():
			if key < self.time:
				self.perf_others25=value
		for key,value in perf5.items():
			if key < self.time:
				self.perf_others5=value


		if self.round_number==1:
			if self.perf_others25 <= self.round_number*5:
				self.emo=1
			elif self.perf_others5 > self.round_number*5 :
				self.emo=3
			else:
				self.emo=2
		else:
			if self.perf_others25 <= self.round_number*5:
				self.emo=1
			elif self.perf_others5 > self.round_number*5:
				self.emo=3
			else:
				self.emo=2

	def calc_score(self):
		if self.round_number==1:
			self.TreeCount=0
			self.payoff=self.participant.vars['endowment']
		else:
			self.TreeCount=self.in_round(self.round_number-1).TreeCount

	def save_payoff(self):
		self.participant.vars['pay']=self.payoff


	def vars_for_template(self):
		return {
		'A': self.subsession.code1[0],
		'B': self.subsession.code1[1],
		'C': self.subsession.code1[2],
		'D': self.subsession.code1[3],
		'E': self.subsession.code1[4],
		'F': self.subsession.code1[5],
		'G': self.subsession.code1[6],
		'H': self.subsession.code1[7],
		'I': self.subsession.code1[8],
		'J': self.subsession.code1[9],
		'N1': self.subsession.code[0],
		'N2': self.subsession.code[1],
		'N3': self.subsession.code[2],
		'N4': self.subsession.code[3],
		'N5': self.subsession.code[4],
		'N6': self.subsession.code[5],
		'N7': self.subsession.code[6],
		'N8': self.subsession.code[7],
		'N9': self.subsession.code[8],
		'N10': self.subsession.code[9],
		'question': self.subsession.question,
		'solution': self.subsession.solution,
		'tree':int((self.round_number-1)*5),
		'tree1':int((self.round_number-1)*10),
		'tree_count':self.round_number,
		'wage_dis':0,
		'pun_dis':10,
		'perf25':self.perf_others25,
		'perf5':self.perf_others5,
		'face': 2
		}

