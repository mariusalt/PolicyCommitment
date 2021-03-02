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
    name_in_url = 'pebs1'
    players_per_group = None
    num_rounds = 2


class Subsession(BaseSubsession):
	rand_max_round = models.IntegerField()
	solution = models.StringField()
	question = models.StringField()
	code1 = models.StringField()
	code=models.StringField()
	def creating_session(self):
		self.rand_max_round=random.choice([2])
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
				for i in range(8):
					b=next(turn)
					k=Num[b]
					numsub.append(k)
				letsub=[]
				for i in range(8):
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
	wage=models.IntegerField(initial=0)
	runde=models.IntegerField(initial=0)
	indicator=models.IntegerField(initial=0)
	time2 = models.FloatField()
	time21 = models.FloatField()
	time22 = models.FloatField()
	time3 = models.FloatField()
	time31 = models.FloatField()
	time32 = models.FloatField()

	def tim2(self):
		self.time2=time.time()
	def tim3(self):
		self.time3=time.time()
	def tim21(self):
		self.time21=time.time()
	def tim31(self):
		self.time31=time.time()
	def tim22(self):
		self.time22=time.time()
	def tim32(self):
		self.time32=time.time()



	def calc_first_pay(self):
		self.payoff=self.participant.vars['endowment']
		self.participant.vars['start'] = time.time()
		

	def roundnumber(self):
		self.runde=self.round_number
		if self.round_number==self.subsession.in_round(1).rand_max_round:
			self.indicator=1

	def calc_tree(self):
		self.TreeCount=self.round_number/2


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
		'tree':int((self.round_number-1)*5)
		}

