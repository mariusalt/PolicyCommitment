from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
	Currency as c, currency_range
)
import random
import csv
import time
import itertools
import numpy as np
import math



author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
	name_in_url = 'Decision2'
	players_per_group = None
	num_rounds = 50


class Subsession(BaseSubsession):
	rand_max_round = models.IntegerField()
	solution = models.StringField()
	question = models.StringField()
	code1 = models.StringField()
	code=models.StringField()
	mail=models.StringField()
	phone=models.StringField()

#    def creating_session(self):
#    	players = self.get_players()
#    	for p in players:
#	    	t=random.choice([1,2,3,4,5,6])
#	    	if t==1:
#	    		p.treatment='baseline'
#	    	elif t==2:
#	    		p.treatment='nudge'
#	    	elif t==3:
#	    		p.treatment='mon'
#	    	elif t==4:
#	    		p.treatment='pun'
#	    	elif t==5:
#	    		p.treatment='force'
#			else:
#				p.treatment='noinc'
	def creating_session(self):
		players = self.get_players()
		for p in players:
			p.participant.vars["relweek"]=1
			p.participant.vars["exwind"]=0
			p.participant.vars['out']=np.random.choice(np.arange(1, 6), p=[0.9, 0.06, 0.03, 0.01, 0])
			p.participant.vars['tita']=5435634
			p.participant.vars["swwf"]=0
			p.participant.vars["smeer"]=0
			p.participant.vars["staf"]=0
		self.rand_max_round=random.choice([10])
		for i in range(51):
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
	who2=models.IntegerField()
	who4=models.IntegerField()
	grochoi=models.StringField()
	relweekgr=models.IntegerField()
	def now(self):
		self.who2=random.choice([i for i in range(1,len(self.get_players())+1)])
		self.who4=random.choice([i for i in range(1,len(self.get_players())+1)])
		for p in self.get_players():
			if p.participant.vars["sechoi"]==1:
				if p.participant.vars["gr"]==2:
					if p.id_in_group==self.who2:
						if p.relweek==0:
							self.relweekgr==0
							p.grosel=1
							p.participant.vars["grosel"]=p.grosel
							self.grochoi=p.participant.vars["typewe"]
							p.choi='Version A' if p.participant.vars['typewe']==p.participant.vars["versiona"] else 'Version B' if p.participant.vars['typewe']==p.participant.vars["versionb"] else 'Version C' if p.participant.vars['typewe']==p.participant.vars["versionc"] else 'Version D'
							
							for i in p.get_others_in_group():
								i.participant.vars["type"]=self.grochoi
								i.choi='Version A' if i.participant.vars['type']==i.participant.vars["versiona"] else 'Version B' if i.participant.vars['type']==i.participant.vars["versionb"] else 'Version C' if i.participant.vars['type']==i.participant.vars["versionc"] else 'Version D'
								i.participant.vars["cho"]=i.choi
								i.participant.vars['version']='Basisversion' if i.participant.vars['type']=='base' else 'Performancevergleich' if i.participant.vars['type']=='nudge' else 'Geldanreiz' if i.participant.vars['type']=='mon' else 'Sanktion' 
			
						elif p.relweek==1:
							self.relweekgr==1
							p.grosel=1
							self.grochoi=p.participant.vars['type']
							for i in p.get_others_in_group():
								i.participant.vars["type"]=self.grochoi
								i.choi='Version A' if i.participant.vars['type']==i.participant.vars["versiona"] else 'Version B' if i.participant.vars['type']==i.participant.vars["versionb"] else 'Version C' if i.participant.vars['type']==i.participant.vars["versionc"] else 'Version D'
								i.participant.vars["cho"]=i.choi
								i.participant.vars['version']='Basisversion' if i.participant.vars['type']=='base' else 'Performancevergleich' if i.participant.vars['type']=='nudge' else 'Geldanreiz' if i.participant.vars['type']=='mon' else 'Sanktion' 
			
					else:
						p.grosel=0
						p.participant.vars["grosel"]=p.grosel
						p.relweek=self.relweekgr

				elif p.participant.vars["gr"]==4:
					if p.id_in_group==self.who4:
						if p.relweek==0:
							self.relweekgr==0
							p.grosel=1
							p.participant.vars["grosel"]=p.grosel
							self.grochoi=p.participant.vars["typewe"]
							p.choi='Version A' if p.participant.vars['typewe']==p.participant.vars["versiona"] else 'Version B' if p.participant.vars['typewe']==p.participant.vars["versionb"] else 'Version C' if p.participant.vars['typewe']==p.participant.vars["versionc"] else 'Version D'
							
							for i in p.get_others_in_group():
								i.participant.vars["type"]=self.grochoi
								i.choi='Version A' if i.participant.vars['type']==i.participant.vars["versiona"] else 'Version B' if i.participant.vars['type']==i.participant.vars["versionb"] else 'Version C' if i.participant.vars['type']==i.participant.vars["versionc"] else 'Version D'
								i.participant.vars["cho"]=i.choi
								i.participant.vars['version']='Basisversion' if i.participant.vars['type']=='base' else 'Performancevergleich' if i.participant.vars['type']=='nudge' else 'Geldanreiz' if i.participant.vars['type']=='mon' else 'Sanktion' 
			

						elif p.relweek==1:
							self.relweekgr==1
							p.grosel=1
							p.participant.vars["grosel"]=p.grosel
							self.grochoi=p.participant.vars['type']
							
							for i in p.get_others_in_group():
								i.participant.vars["type"]=self.grochoi
								i.choi='Version A' if i.participant.vars['type']==i.participant.vars["versiona"] else 'Version B' if i.participant.vars['type']==i.participant.vars["versionb"] else 'Version C' if i.participant.vars['type']==i.participant.vars["versionc"] else 'Version D'
								i.participant.vars["cho"]=i.choi
								i.participant.vars['version']='Basisversion' if i.participant.vars['type']=='base' else 'Performancevergleich' if i.participant.vars['type']=='nudge' else 'Geldanreiz' if i.participant.vars['type']=='mon' else 'Sanktion' 
			
					else:
						p.grosel=0
						p.participant.vars["grosel"]=p.grosel
						p.relweek=self.relweekgr

				else:
					pass

			else:
				if p.participant.vars["gr"]==2:
					if p.id_in_group==self.who2:
						if p.relweek==0:
							self.relweekgr==0
							p.grosel=1
							p.participant.vars["grosel"]=p.grosel
							self.grochoi=p.participant.vars["typewe"]
							p.choi='Version A' if p.participant.vars['typewe']==p.participant.vars["versiona"] else 'Version B' if p.participant.vars['typewe']==p.participant.vars["versionb"] else 'Version C' if p.participant.vars['typewe']==p.participant.vars["versionc"] else 'Version D'
							
							for i in p.get_others_in_group():
								i.participant.vars["type"]=self.grochoi
								i.choi='Version A' if i.participant.vars['type']==i.participant.vars["versiona"] else 'Version B' if i.participant.vars['type']==i.participant.vars["versionb"] else 'Version C' if i.participant.vars['type']==i.participant.vars["versionc"] else 'Version D'
								i.participant.vars["cho"]=i.choi
								i.participant.vars['version']='Basisversion' if i.participant.vars['type']=='base' else 'Performancevergleich' if i.participant.vars['type']=='nudge' else 'Geldanreiz' if i.participant.vars['type']=='mon' else 'Sanktion' 
			
					else:
						p.grosel=0
						p.participant.vars["grosel"]=p.grosel
						p.relweek=self.relweekgr

				elif p.participant.vars["gr"]==4:
					if p.id_in_group==self.who4:
						if p.relweek==0:
							self.relweekgr==0
							p.grosel=1
							p.participant.vars["grosel"]=p.grosel
							self.grochoi=p.participant.vars["typewe"]
							p.choi='Version A' if p.participant.vars['typewe']==p.participant.vars["versiona"] else 'Version B' if p.participant.vars['typewe']==p.participant.vars["versionb"] else 'Version C' if p.participant.vars['typewe']==p.participant.vars["versionc"] else 'Version D'
							
							for i in p.get_others_in_group():
								i.participant.vars["type"]=self.grochoi
								i.choi='Version A' if i.participant.vars['type']==i.participant.vars["versiona"] else 'Version B' if i.participant.vars['type']==i.participant.vars["versionb"] else 'Version C' if i.participant.vars['type']==i.participant.vars["versionc"] else 'Version D'
								i.participant.vars["cho"]=i.choi
								i.participant.vars['version']='Basisversion' if i.participant.vars['type']=='base' else 'Performancevergleich' if i.participant.vars['type']=='nudge' else 'Geldanreiz' if i.participant.vars['type']=='mon' else 'Sanktion' 
			
					else:
						p.grosel=0
						p.participant.vars["grosel"]=p.grosel
						p.relweek=self.relweekgr

				else:
					pass

	def weekrel(self):
		for p in self.get_players():
			p.relweek=self.relweekgr
			p.participant.vars["relweek"]=p.relweek

			


class Player(BasePlayer):
	randnu = models.IntegerField()
	t_no = models.IntegerField()
	t_nu = models.IntegerField()
	t_mo = models.IntegerField()
	t_pu = models.IntegerField()
	t_fo = models.IntegerField()
	first1=models.StringField()
	first2=models.StringField()
	first3=models.StringField()
	first4=models.StringField()
	first5=models.StringField()
	first6=models.StringField()
	first7=models.StringField()
	first8=models.StringField()
	first9=models.StringField()
	first10=models.StringField()
	alter_nu=models.FloatField(blank=True)
	second1=models.StringField()
	second2=models.StringField()
	second3=models.StringField()
	second4=models.StringField()
	second5=models.StringField()
	second6=models.StringField()
	second7=models.StringField()
	second8=models.StringField()
	second9=models.StringField()
	second10=models.StringField()
	alter_mon=models.FloatField(blank=True)
	third1=models.StringField()
	third2=models.StringField()
	third3=models.StringField()
	third4=models.StringField()
	third5=models.StringField()
	third6=models.StringField()
	third7=models.StringField()
	third8=models.StringField()
	third9=models.StringField()
	third10=models.StringField()
	alter_punish=models.FloatField(blank=True)
	first21=models.StringField()
	first22=models.StringField()
	first23=models.StringField()
	first24=models.StringField()
	first25=models.StringField()
	first26=models.StringField()
	first27=models.StringField()
	first28=models.StringField()
	first29=models.StringField()
	first210=models.StringField()
	alter2_nu=models.FloatField(blank=True)
	second21=models.StringField()
	second22=models.StringField()
	second23=models.StringField()
	second24=models.StringField()
	second25=models.StringField()
	second26=models.StringField()
	second27=models.StringField()
	second28=models.StringField()
	second29=models.StringField()
	second210=models.StringField()
	alter2_mon=models.FloatField(blank=True)
	third21=models.StringField()
	third22=models.StringField()
	third23=models.StringField()
	third24=models.StringField()
	third25=models.StringField()
	third26=models.StringField()
	third27=models.StringField()
	third28=models.StringField()
	third29=models.StringField()
	third210=models.StringField()
	alter2_punish=models.FloatField(blank=True)
	first=models.StringField()
	second=models.StringField()
	third=models.StringField()
	fourth=models.StringField()
	choi=models.StringField()
	num=models.IntegerField()
	vextrapay=models.FloatField()
	sell=models.IntegerField()
	ref = models.StringField()
	time = models.StringField()
	treat = models.StringField()
	noinc = models.IntegerField()
	nudge = models.IntegerField()
	mon = models.IntegerField()
	punish = models.IntegerField()
	force = models.IntegerField()
	TreeCount=models.FloatField(initial=0)
	answer = models.StringField()
	wage=models.IntegerField(initial=0)
	punleft=models.IntegerField(initial=10)
	treatment=models.StringField()
	runde=models.IntegerField(initial=0)
	indicator=models.IntegerField(initial=0)
	emo=models.IntegerField(initial=2)
	perf_others25=models.FloatField(initial=0)
	perf_others5=models.FloatField(initial=0)
	time=models.FloatField()
	pun=models.IntegerField(initial=5)
	mail = models.StringField()
	belper = models.IntegerField(min=0, max=100)
	mot1 = models.IntegerField(min=0, max=100)
	mot2 = models.IntegerField(min=0, max=100)
	mot3 = models.IntegerField(min=0, max=100)
	mot4 = models.IntegerField(min=0, max=100)
	mot5 = models.IntegerField(min=0, max=100)
	alter3 = models.FloatField(blank=True)
	rand=models.IntegerField()
	endow=models.FloatField()
	relweek = models.IntegerField(initial=1)
	tita=models.FloatField()
	grosel = models.IntegerField()
	belbo=models.FloatField()

	def ti(self):
		self.participant.vars["tita"]=round(time.time()*1000,0)



		
	def saverank(self):
		self.participant.vars['first']=self.first
		self.participant.vars['second']=self.second
		self.participant.vars['third']=self.third
		self.participant.vars['fourth']=self.fourth

	def savechoi2(self):
		self.participant.vars['first1']=self.first1
		self.participant.vars['first2']=self.first2
		self.participant.vars['first3']=self.first3
		self.participant.vars['first4']=self.first4
		self.participant.vars['first5']=self.first5
		self.participant.vars['first6']=self.first6
		self.participant.vars['first7']=self.first7
		self.participant.vars['first8']=self.first8
		self.participant.vars['first9']=self.first9
		self.participant.vars['first10']=self.first10

	def savechoi3(self):
		self.participant.vars['second1']=self.second1
		self.participant.vars['second2']=self.second2
		self.participant.vars['second3']=self.second3
		self.participant.vars['second4']=self.second4
		self.participant.vars['second5']=self.second5
		self.participant.vars['second6']=self.second6
		self.participant.vars['second7']=self.second7
		self.participant.vars['second8']=self.second8
		self.participant.vars['second9']=self.second9
		self.participant.vars['second10']=self.second10

	def savechoi4(self):
		self.participant.vars['third1']=self.third1
		self.participant.vars['third2']=self.third2
		self.participant.vars['third3']=self.third3
		self.participant.vars['third4']=self.third4
		self.participant.vars['third5']=self.third5
		self.participant.vars['third6']=self.third6
		self.participant.vars['third7']=self.third7
		self.participant.vars['third8']=self.third8
		self.participant.vars['third9']=self.third9
		self.participant.vars['third10']=self.third10



	def chotrea(self):
		self.relweek = random.choice([0,1])
		self.participant.vars["relweek"]=self.relweek
		if self.relweek==1:
			self.sell=random.choice([1,2,3])
			np.random.choice(np.arange(1, 5), p=[0.37, 0.29, 0.21, 0.13])
			if self.sell==1:
				k=[self.participant.vars["first1"],self.participant.vars["first2"],self.participant.vars["first3"],self.participant.vars["first4"],self.participant.vars["first5"],self.participant.vars["first6"],self.participant.vars["first7"],self.participant.vars["first8"],self.participant.vars["first9"],self.participant.vars["first10"]]
				di1={0:0,1:0.1,2:0.25,3:0.5,4:0.75,5:1,6:1.5,7:2,8:3,9:5}
				self.num = np.random.choice(np.arange(0,len(k)), p=[0.155, 0.155, 0.115, 0.115,0.115, 0.115, 0.075, 0.075,0.06,0.02])
				self.vextrapay= di1[self.num] if k[self.num]!=self.participant.vars["first"] else 0
				self.participant.vars['comp']=1 if k[self.num]!=self.participant.vars["first"] else 0
				self.participant.vars['endowment']=float(self.vextrapay)+float(self.participant.vars['endowment'])
				self.participant.vars['extrpay']=self.vextrapay
				self.choi = k[self.num]
				self.participant.vars['cho']=self.choi
				self.participant.vars['type']=self.participant.vars["versiona"] if self.choi=='Version A' else self.participant.vars["versionb"] if self.choi=='Version B' else self.participant.vars["versionc"] if self.choi=='Version C' else self.participant.vars["versiond"] 
				self.participant.vars['version']='Basisversion' if self.participant.vars['type']=='base' else 'Performancevergleich' if self.participant.vars['type']=='nudge' else 'Geldanreiz' if self.participant.vars['type']=='mon' else 'Sanktion' if self.participant.vars['type']=='punish' else 'Vorgabe'
			elif self.sell==2:
				l=[self.participant.vars["second1"],self.participant.vars["second2"],self.participant.vars["second3"],self.participant.vars["second4"],self.participant.vars["second5"],self.participant.vars["second6"],self.participant.vars["second7"],self.participant.vars["second8"],self.participant.vars["second9"],self.participant.vars["second10"]]
				di1={0:0,1:0.1,2:0.25,3:0.5,4:0.75,5:1,6:1.5,7:2,8:3,9:5}
				self.num = np.random.choice(np.arange(0,len(l)), p=[0.155, 0.155, 0.115, 0.115,0.115, 0.115, 0.075, 0.075,0.06,0.02])
				self.vextrapay= di1[self.num] if l[self.num]!=self.participant.vars["first"] else 0
				self.participant.vars['comp']=1 if l[self.num]!=self.participant.vars["first"] else 0
				self.participant.vars['extrpay']=float(self.vextrapay)
				self.participant.vars['endowment']=float(self.vextrapay)+float(self.participant.vars['endowment'])
				self.choi = l[self.num]
				self.participant.vars['cho']=self.choi
				self.participant.vars['type']=self.participant.vars["versiona"] if self.choi=='Version A' else self.participant.vars["versionb"] if self.choi=='Version B' else self.participant.vars["versionc"] if self.choi=='Version C' else self.participant.vars["versiond"] 
				self.participant.vars['version']='Basisversion' if self.participant.vars['type']=='base' else 'Performancevergleich' if self.participant.vars['type']=='nudge' else 'Geldanreiz' if self.participant.vars['type']=='mon' else 'Sanktion' if self.participant.vars['type']=='punish' else 'Vorgabe'
			elif self.sell==3:
				m=[self.participant.vars["third1"],self.participant.vars["third2"],self.participant.vars["third3"],self.participant.vars["third4"],self.participant.vars["third5"],self.participant.vars["third6"],self.participant.vars["third7"],self.participant.vars["third8"],self.participant.vars["third9"],self.participant.vars["third10"]]
				di1={0:0,1:0.1,2:0.25,3:0.5,4:0.75,5:1,6:1.5,7:2,8:3,9:5}
				self.num = np.random.choice(np.arange(0,len(m)), p=[0.155, 0.155, 0.115, 0.115,0.115, 0.115, 0.075, 0.075,0.06,0.02])
				self.vextrapay= di1[self.num] if m[self.num]!=self.participant.vars["first"] else 0
				self.participant.vars['comp']=1 if m[self.num]!=self.participant.vars["first"] else 0
				self.participant.vars['endowment']=float(self.vextrapay)+float(self.participant.vars['endowment'])
				self.participant.vars['extrpay']=self.vextrapay
				self.choi = m[self.num]
				self.participant.vars['cho']=self.choi
				self.participant.vars['type']=self.participant.vars["versiona"] if self.choi=='Version A' else self.participant.vars["versionb"] if self.choi=='Version B' else self.participant.vars["versionc"] if self.choi=='Version C' else self.participant.vars["versiond"] 
				self.participant.vars['version']='Basisversion' if self.participant.vars['type']=='base' else 'Performancevergleich' if self.participant.vars['type']=='nudge' else 'Geldanreiz' if self.participant.vars['type']=='mon' else 'Sanktion' if self.participant.vars['type']=='punish' else 'Vorgabe'

		else:
			self.participant.vars['type']=self.participant.vars['typewe']
			self.choi='Version A' if self.participant.vars['typewe']==self.participant.vars["versiona"] else 'Version B' if self.participant.vars['typewe']==self.participant.vars["versionb"] else 'Version C' if self.participant.vars['typewe']==self.participant.vars["versionc"] else 'Version D'
			self.participant.vars['extrpay']=self.participant.vars['vextrapayw1']
			self.participant.vars['cho']=self.participant.vars['chowe']

	def chotreanosec(self):
		self.participant.vars['type']=self.participant.vars['typewe']
		self.participant.vars['extrpay']=self.participant.vars['vextrapayw1']
		self.participant.vars['cho']=self.participant.vars['chowe']
		self.participant.vars["first"]=self.participant.vars["firstw1"]
		self.participant.vars["second"]=self.participant.vars["secondw1"]
		self.participant.vars["third"]=self.participant.vars["thirdw1"]
		self.participant.vars["fourth"]=self.participant.vars["fourthw1"]
		self.participant.vars['version']='Basisversion' if self.participant.vars['type']=='base' else 'Performancevergleich' if self.participant.vars['type']=='nudge' else 'Geldanreiz' if self.participant.vars['type']=='mon' else 'Sanktion' if self.participant.vars['type']=='punish' else 'Vorgabe'

	def savebel(self):
		self.participant.vars["belper"]=self.belper

	def treaty(self):
		self.treatment=self.participant.vars['type']
		self.participant.vars["punleft"]=self.punleft

	def calc_first_pay(self):
		self.participant.vars["payoff1"]=float(self.participant.vars['endowment'])
		self.participant.vars['start'] = time.time()

	def calc_tree(self):
		self.TreeCount=round((self.round_number-3)/3,2)
		self.participant.vars["treecount"]=self.TreeCount
		if self.participant.vars['type']=='mon':
			if self.round_number==4:
				self.participant.vars["endowment"]=12
				self.wage=self.in_round(self.round_number-1).wage+25
				self.participant.vars["wage"]=self.wage/100
				self.participant.vars["payoff1"]=self.participant.vars['endowment']+0.25
			elif self.round_number>4 and self.round_number<33:
				self.wage=self.in_round(self.round_number-1).wage+25
				self.participant.vars["wage"]=self.wage/100
				self.participant.vars["payoff1"]=self.participant.vars['endowment']+self.participant.vars["wage"]
			elif self.round_number>=33:
				self.wage=self.in_round(self.round_number-1).wage
				self.participant.vars["wage"]=self.wage/100
				self.participant.vars["payoff1"]=self.participant.vars['endowment']+self.participant.vars["wage"]

		elif self.participant.vars['type']=='punish':
			if self.round_number==4:
				self.participant.vars["payoff1"]=self.participant.vars['endowment']-self.pun
				self.punleft=13-self.round_number
				self.participant.vars["punleft"]=self.punleft
			elif self.round_number > 4 and self.round_number < 13:
				self.participant.vars["payoff1"]=self.participant.vars['endowment']-self.pun
				self.punleft=13-self.round_number
				self.participant.vars["punleft"]=self.punleft

			elif self.round_number>=13:
				self.pun=0
				self.punleft=0
				self.participant.vars["punleft"]=self.punleft
				self.participant.vars["payoff1"]=self.participant.vars['endowment']
		else:
			self.participant.vars["payoff1"]=self.participant.vars['endowment']
		
	


	def save_payoff(self):
		self.payoff=self.participant.vars["payoff1"]
		self.TreeCount=round((self.round_number-3)/3,2)
		self.participant.vars["treecount"]=self.TreeCount

	def roundnumber(self):
		self.runde=self.round_number
		if self.round_number==self.subsession.in_round(1).rand_max_round:
			self.indicator=1

	def compare(self):
		self.time=int(round(time.time()-self.participant.vars['start']))
		perf5={28435:0.33,52370:0.66,77652:1,101457:1.33,126065:1.66,148152:2,172543:2.33,194913:2.66,217783:3,242304:3.33,266348:3.66,289478:4,310370:4.33,333000:4.66,355783:5,379022:5.33,401697:5.66,424371:6,447046:6.33,469720:6.66}
		perf25={22273:0.33,43545:0.66,63909:1,81909:1.33,102455:1.66,119273:2,138000:2.33,156818:2.66,175091:3,194909:3.33,213818:3.66,233455:4,251364:4.33,268636:4.66,286273:5,309091:5.33,326818:5.66,344273:6,361818:6.33,382091:6.66,402818:7,420182:7.33,437091:7.66,452909:8,456250:8.33,471197:8.66}
		for key,value in perf25.items():
			if key < self.time:
				self.perf_others25=value
		for key,value in perf5.items():
			if key < self.time:
				self.perf_others5=value


		if self.round_number==4:
			if self.perf_others25 <= (self.round_number-3)*0.33:
				self.emo=1
			elif self.perf_others5 > (self.round_number-3)*0.33 :
				self.emo=3
			else:
				self.emo=2
		else:
			if self.perf_others25 <= (self.round_number-3)*0.33:
				self.emo=1
			elif self.perf_others5 > (self.round_number-3)*0.33:
				self.emo=3
			else:
				self.emo=2

	def belbon(self):
		tperl=self.participant.vars["treecount"]-(self.participant.vars["treecount"]/10)
		tperh=self.participant.vars["treecount"]+(self.participant.vars["treecount"]/10)
		if self.participant.vars["belper"]>tperl and self.participant.vars["belper"]<tperh:
			self.belbo=0.5
		else:
			self.belbo=0
		self.participant.vars["belbo"]=self.belbo

	def vars_for_template(self):
		return {
		'choice': self.participant.vars['out'],
		'treat': self.in_round(self.round_number-1).treat,
		'first': self.participant.vars['first'],
		'second':self.participant.vars['second'],
		'third':self.participant.vars['third'],
		'fourth':self.participant.vars['fourth'],
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
		'tree':int((self.round_number-4)*33),
		'tree1':int(math.floor(self.round_number-4)/3),
		'tree_count':self.round_number-4,
		'wage_dis':0,
		'pun_dis':10,
		'perf25':self.perf_others25,
		'perf5':self.perf_others5,
		'face': 2,
		'tita':int(self.participant.vars["tita"]),
		'pingro':self.get_others_in_group(),
		} 
 
	Q1_1 = models.IntegerField()
	Q1_2 = models.IntegerField()
	Q1_3 = models.IntegerField()
	Q1_4 = models.IntegerField()
	Q1_5 = models.IntegerField()
	Q2 = models.IntegerField(
		choices=[
			[1, '5'], 
			[2, '3'],
			[3, '1'],
			[4, "4"],		
		 ],
		 widget=widgets.RadioSelect
		)
	Q3 = models.IntegerField(
		choices=[
			[1, 'Durchschnittsperformance und Medianperformance'], 
			[2, 'Medianperformance und Performance der Person im oberen 10ten Percentil'],
			[3, 'Durchschnittsperformance und Performance der Person im oberen 25ten Percentil'],
			[4, "Medianperformance und Performance der Person im unteren 25ten Percentil"],		
		 ],
		 widget=widgets.RadioSelect
		)
	Q4 = models.IntegerField(
		choices=[
			[1, '0,25€'], 
			[2, '0,1€'],
			[3, '0,5€'],
			[4, "0,15€"],		
		 ],
		 widget=widgets.RadioSelect
		)
	Q5 = models.IntegerField(
		choices=[
			[1, '19€'], 
			[2, '10€'],
			[3, '17€'],
			[4, "12€"],		
		 ],
		 widget=widgets.RadioSelect
		)
	Q6 = models.IntegerField(
		choices=[
			[1, '10'], 
			[2, '5'],
			[3, '16'],
			[4, "20"],	
		 ],
		 widget=widgets.RadioSelect
		)
	Q7 = models.IntegerField(
		choices=[
			[1, 'Teilnahmevergütung: 12,00€, max. Bonus: keine Obergrenze'], 
			[2, 'Teilnahmevergütung: 12,00€, max. Bonus: 7,00€'],
			[3, 'Teilnahmevergütung: 17,00€, max. Bonus: 7,00€'],
			[4, 'Teilnahmevergütung: 17,00€, max. Bonus: 0€'],	
		 ],
		 widget=widgets.RadioSelect
		)
	wrong = models.IntegerField(initial=0)