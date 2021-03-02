from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
	Currency as c, currency_range
)
import random
from random import randint
import time
import itertools
import numpy as np
import math 


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
	name_in_url = 'Decision'
	players_per_group = None
	tasks = ['A','B','C','D']
	num_rounds = 4


class Subsession(BaseSubsession):

	def creating_session(self):
		
		if self.round_number == 1:
			for p in self.get_players():
				p.participant.vars['out']=np.random.choice(np.arange(1, 6), p=[0.9, 0.06, 0.03, 0.01, 0])
				round_numbers = list(range(1, Constants.num_rounds+1))
				li=[1,2,3,4]
				random.shuffle(li)
				for k,i in enumerate(li):
					round_numbers[k]=i
				p.participant.vars['task_rounds'] = dict(zip(Constants.tasks, round_numbers))
				p.participant.vars['noinc']=p.participant.vars['task_rounds']['A']
				p.t_no=p.participant.vars['task_rounds']['A']
				p.participant.vars['nudge']=p.participant.vars['task_rounds']['B']
				p.t_nu=p.participant.vars['task_rounds']['B']
				p.participant.vars['mon']=p.participant.vars['task_rounds']['C']
				p.t_mo=p.participant.vars['task_rounds']['C']
				p.participant.vars['punish']=p.participant.vars['task_rounds']['D']
				p.t_pu=p.participant.vars['task_rounds']['D']



		
	
		




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
	


class Group(BaseGroup):
	who=models.IntegerField()
	grochoi=models.StringField()
	def selplay(self):
		if p.participant.vars["gr"]==2:
			self.who=random.choice([1,2])
			if p.id_in_group==self.who:
				p.grosel=1
				self.grochoi=p.type1
				for i in p.get_others_in_group():
					i.participant.vars["type"]=self.grochoi
					i.choi='Version A' if i.participant.vars['type']==i.versiona else 'Version B' if i.participant.vars['type']==i.versionb else 'Version C' if i.participant.vars['type']==i.versionc else 'Version D'
					i.participant.vars['version']='Basisversion' if i.participant.vars['type']=='base' else 'Performancevergleich' if i.participant.vars['type']=='nudge' else 'Geldanreiz' if i.participant.vars['type']=='mon' else 'Sanktion' 
			else:
				p.grosel=0

		elif p.participant.vars["gr"]==4:
			self.who=random.choice([1,2,3,4])
			if p.id_in_group==self.who:
				p.grosel=1
				self.grochoi=p.type1
				for i in p.get_others_in_group():
					i.participant.vars["type"]=self.grochoi
					i.choi='Version A' if i.participant.vars['type']==i.versiona else 'Version B' if i.participant.vars['type']==i.versionb else 'Version C' if i.participant.vars['type']==i.versionc else 'Version D'
					i.participant.vars['version']='Basisversion' if i.participant.vars['type']=='base' else 'Performancevergleich' if i.participant.vars['type']=='nudge' else 'Geldanreiz' if i.participant.vars['type']=='mon' else 'Sanktion' 
			else:
				p.grosel=0



class Player(BasePlayer):
	treat = models.StringField()
	noinc = models.IntegerField()
	nudge = models.IntegerField()
	mon = models.IntegerField()
	punish = models.IntegerField()
	choice = models.StringField(initial="noinc")
	t_no = models.IntegerField()
	t_nu = models.IntegerField()
	t_mo = models.IntegerField()
	t_pu = models.IntegerField()
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
	fifth=models.StringField()
	fir2=models.StringField()
	sec2=models.StringField()
	thi2=models.StringField()
	fou2=models.StringField()
	fifth2=models.StringField()
	choi=models.StringField()
	num=models.IntegerField()
	vextrapay=models.FloatField()
	sell=models.IntegerField()
	versiona=models.StringField()
	versionb=models.StringField()
	versionc=models.StringField()
	versiond=models.StringField()
	versione=models.StringField()
	comp = models.FloatField()
	type1=models.StringField()

	def ti(self):
		self.participant.vars["tita"]=round(time.time()*1000,0)




	def chotrea(self):
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

	def versionen(self):
		self.versiona='base' if self.participant.vars['noinc']==1 else 'nudge' if self.participant.vars['nudge']==1 else 'mon' if self.participant.vars['mon']==1 else 'punish' if self.participant.vars['punish']==1 else 'force'
		self.versionb='base' if self.participant.vars['noinc']==2 else 'nudge' if self.participant.vars['nudge']==2 else 'mon' if self.participant.vars['mon']==2 else 'punish' if self.participant.vars['punish']==2 else 'force'
		self.versionc='base' if self.participant.vars['noinc']==3 else 'nudge' if self.participant.vars['nudge']==3 else 'mon' if self.participant.vars['mon']==3 else 'punish' if self.participant.vars['punish']==3 else 'force'		
		self.versiond='base' if self.participant.vars['noinc']==4 else 'nudge' if self.participant.vars['nudge']==4 else 'mon' if self.participant.vars['mon']==4 else 'punish' if self.participant.vars['punish']==4 else 'force'
		self.versione='base' if self.participant.vars['noinc']==5 else 'nudge' if self.participant.vars['nudge']==5 else 'mon' if self.participant.vars['mon']==5 else 'punish' if self.participant.vars['punish']==5 else 'force'
		self.participant.vars["versiona"]=self.versiona
		self.participant.vars["versionb"]=self.versionb
		self.participant.vars["versionc"]=self.versionc
		self.participant.vars["versiond"]=self.versiond

	def saverank(self):
		self.participant.vars["pay"]=0
		self.participant.vars['first']=self.first
		self.participant.vars['second']=self.second
		self.participant.vars['third']=self.third
		self.participant.vars['fourth']=self.fourth

	def saverank2(self):
		self.participant.vars['fir2']=self.fir2
		self.participant.vars['sec2']=self.sec2
		self.participant.vars['thi2']=self.thi2
		self.participant.vars['fou2']=self.fou2
	
	def rankval(self):
		self.treat=self.in_round(self.round_number-1).treat
		self.first=self.participant.vars['first']
		self.second=self.participant.vars['second']
		self.third=self.participant.vars['third']
		self.fourth=self.participant.vars['fourth']

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

	def savechoi22(self):
		self.participant.vars['first21']=self.first21
		self.participant.vars['first22']=self.first22
		self.participant.vars['first23']=self.first23
		self.participant.vars['first24']=self.first24
		self.participant.vars['first25']=self.first25
		self.participant.vars['first26']=self.first26
		self.participant.vars['first27']=self.first27
		self.participant.vars['first28']=self.first28
		self.participant.vars['first29']=self.first29
		self.participant.vars['first210']=self.first210

	def savechoi23(self):
		self.participant.vars['second21']=self.second21
		self.participant.vars['second22']=self.second22
		self.participant.vars['second23']=self.second23
		self.participant.vars['second24']=self.second24
		self.participant.vars['second25']=self.second25
		self.participant.vars['second26']=self.second26
		self.participant.vars['second27']=self.second27
		self.participant.vars['second28']=self.second28
		self.participant.vars['second29']=self.second29
		self.participant.vars['second210']=self.second210

	def savechoi24(self):
		self.participant.vars['third21']=self.third21
		self.participant.vars['third22']=self.third22
		self.participant.vars['third23']=self.third23
		self.participant.vars['third24']=self.third24
		self.participant.vars['third25']=self.third25
		self.participant.vars['third26']=self.third26
		self.participant.vars['third27']=self.third27
		self.participant.vars['third28']=self.third28
		self.participant.vars['third29']=self.third29
		self.participant.vars['third210']=self.third210



	def decsave1(self):
		self.participant.vars["dec11"]=self.dec11
		self.participant.vars["dec21"]=self.dec21
		self.participant.vars["dec31"]=self.dec31
		self.participant.vars["dec41"]=self.dec41
		self.participant.vars["dec51"]=self.dec51

	def asssave1(self):
		self.participant.vars["ass11"]=self.ass11
		self.participant.vars["ass21"]=self.ass21
		self.participant.vars["ass31"]=self.ass31
		self.participant.vars["ass41"]=self.ass41
		self.participant.vars["ass51"]=self.ass51


	def seltask(self):
		self.tadi = random.choice([2])
		self.participant.vars["tadi"]=self.tadi
		if self.tadi==1:
			self.tava=random.choice([1,2,3,4,5])
			self.participant.vars["tava"]=self.tava
			#...............
		else:
			self.tava=random.choice([1,2,3,4,5])
			self.participant.vars["tava"]=self.tava
			self.tod = self.participant.vars["dec11"] if self.tava == 1 else self.participant.vars["dec21"] if self.tava == 2 else self.participant.vars["dec31"] if self.tava == 3 else self.participant.vars["dec41"] if self.tava == 4 else self.participant.vars["dec51"] 
	#		self.nweek = self.participant.vars["dec12"] if self.tava == 1 else self.participant.vars["dec22"] if self.tava == 2 else self.participant.vars["dec32"] if self.tava == 3 else self.participant.vars["dec42"] if self.tava == 4 else self.participant.vars["dec52"] 
			self.participant.vars["tod"]=self.tod
	#		self.participant.vars["nweek"]=self.nweek

	def calc_todaypay(self):
		self.rand=random.randint(0,9)
		var1=[self.ptoday1,self.ptoday2,self.ptoday3,self.ptoday4,self.ptoday5,self.ptoday6,self.ptoday7,self.ptoday8,self.ptoday9,self.ptoday10]
		self.pweek=var1[self.rand]+self.participant.vars['expay']
		self.participant.vars["wowe"]=var1[self.rand]+self.participant.vars['expay']
		if var1[self.rand]==21:
			self.ptoday=0
			self.participant.vars["woto"]=0
		else:
			self.ptoday=5
			self.participant.vars["woto"]=5





	def treaty(self):
		self.treatment=self.participant.vars['type']

	def calc_first_pay(self):
		self.payoff=self.participant.vars['endowment']
		self.participant.vars['start'] = time.time()

	def calc_tree(self):
		self.TreeCount=round((self.round_number-3)/3,2)
		if self.participant.vars['type']=='mon':
			if self.round_number==4:
				self.wage=self.in_round(self.round_number-1).wage+5
				self.payoff=self.participant.vars['endowment']
			else:
				self.wage=self.in_round(self.round_number-1).wage+5
				self.payoff=self.participant.vars['endowment']+self.wage/10
		else:
			self.payoff=self.participant.vars['endowment']

		if self.participant.vars['type']=='punish':
			if self.round_number==4:
				self.payoff=self.participant.vars['endowment']-self.pun
				self.pun=self.pun-1
			else:
				self.pun=self.in_round(self.round_number-1).pun-1
				self.payoff=self.participant.vars['endowment']-self.pun
		else:
			self.payoff=self.participant.vars['endowment']
		
	def calc_tree2(self):
		self.participant.vars["rn"]=self.round_number
		if self.round_number==4:
			self.TreeCount=0
			self.payoff=self.participant.vars['endowment']
		else:
			self.TreeCount=math.floor(self.in_round(self.round_number-1).TreeCount)

		if self.participant.vars['type']=='mon':
			if self.round_number==4:
				self.wage=0
				self.payoff=self.participant.vars['endowment']
			else:
				self.wage=self.in_round(self.round_number-1).wage
				self.payoff=self.participant.vars['endowment']+self.in_round(self.round_number-1).wage/10
		else:
			self.payoff=self.participant.vars['endowment']

	def calc_score(self):
		if self.round_number==4:
			self.TreeCount=0
			self.payoff=self.participant.vars['endowment']
		else:
			self.TreeCount=self.in_round(self.round_number-1).TreeCount

	def save_payoff(self):
		self.participant.vars['pay']=self.payoff


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

	def defpartvars(self):
		self.participant.vars['expay']=0
		self.participant.vars['cho']='test'
		self.participant.vars['first']='test'
		self.participant.vars['second']='test'
		self.participant.vars['third']='test'
		self.participant.vars['fourth']='test'
		self.participant.vars['tita']=5435634
		self.participant.vars["rn"]=50
		self.participant.vars['fir2']='test'
		self.participant.vars['sec2']='test'
		self.participant.vars['thi2']='test'
		self.participant.vars['fou2']='test'




	def vars_for_template(self):
		return {
		'choice': self.participant.vars['out'],
		'treat': self.participant.vars['cho'],
		'first': self.participant.vars['first'],
		'second': self.participant.vars['second'],
		'third': self.participant.vars['third'],
		'fourth': self.participant.vars['fourth'],
		'fir2': self.participant.vars['fir2'],
		'sec2': self.participant.vars['sec2'],
		'thi2': self.participant.vars['thi2'],
		'fou2': self.participant.vars['fou2'],
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
			[3, 'Durchschnittsperformance und Performance der Personen im oberen 25ten Percentil'],
			[4, "Medianperformance und Performance der Personen im unteren 25ten Percentil"],		
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
	Q8 = models.IntegerField()

	wrong = models.IntegerField(initial=0)

