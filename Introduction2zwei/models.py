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
	name_in_url = 'Decision1'
	players_per_group = None
	tasks = ['A','B','C','D']
	num_rounds = 44


class Subsession(BaseSubsession):
	rand_max_round = models.IntegerField()
	solution = models.StringField()
	question = models.StringField()
	code1 = models.StringField()
	code=models.StringField()
	mail=models.StringField()
	phone=models.StringField()
	max_round = models.IntegerField()
	correct = models.IntegerField()
	group_id = models.IntegerField(initial=1)

	def creating_session(self):

		self.max_round=random.choice([3])#participant.vars
		for i in range(50):
			if self.round_number == i:
				col=[]
				Letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","K","K","K"]
				while col.count('K')==0:
					for k in range(0,100):
						n=random.randint(0,28)
						l=Letters[n]
						col.append(l)
				self.correct=col.count('K')
				sep=","
				for p in self.get_players():
					p.corr=col.count('K')
					p.lets=','.join(col)



		self.rand_max_round=random.choice([10])
		for i in range(45):
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
				
	

	
	def group_by_arrival_time_method(self, waiting_players):

		self_players = [p for p in waiting_players if p.participant.vars['ref'] == 'self']
		gr2_immi_players = [p for p in waiting_players if p.participant.vars['gr'] == 2 and p.participant.vars["time"]=='immi']
		gr2_delay_players = [p for p in waiting_players if p.participant.vars['gr'] == 2 and p.participant.vars["time"]=='delay']
		gr4_immi_players = [p for p in waiting_players if p.participant.vars['gr'] == 4 and p.participant.vars["time"]=='immi']
		gr4_delay_players = [p for p in waiting_players if p.participant.vars['gr'] == 4 and p.participant.vars["time"]=='delay']

		if len(self_players) >=1:
			for p in self_players:
				p.id_in_group2=1
				p.group_idp=self.group_id
			self.group_id=self.group_id+1
			return [self_players[0]]
		if len(gr2_immi_players) >=2:
			ids=[1,2]
			random.shuffle(ids)
			idsz = itertools.cycle(ids)
			for p in gr2_immi_players:
				p.id_in_group2=next(idsz)
				p.group_idp=self.group_id
			self.group_id=self.group_id+1
			return [gr2_immi_players[0], gr2_immi_players[1]]
		if len(gr2_delay_players) >=2:
			ids=[1,2]
			random.shuffle(ids)
			idsz = itertools.cycle(ids)
			for p in gr2_delay_players:
				p.id_in_group2=next(idsz)
				p.group_idp=self.group_id
			self.group_id=self.group_id+1
			return [gr2_delay_players[0], gr2_delay_players[1]]
		if len(gr4_immi_players) >=4:
			ids=[1,2,3,4]
			random.shuffle(ids)
			idsz = itertools.cycle(ids)
			for p in gr4_immi_players:
				p.id_in_group2=next(idsz)
				p.group_idp=self.group_id
			self.group_id=self.group_id+1
			return [gr4_immi_players[0], gr4_immi_players[1], gr4_immi_players[2], gr4_immi_players[3]]
		if len(gr4_delay_players) >=4:
			ids=[1,2,3,4]
			random.shuffle(ids)
			idsz = itertools.cycle(ids)
			for p in gr4_delay_players:
				p.id_in_group2=next(idsz)
				p.group_idp=self.group_id
			self.group_id=self.group_id+1
			return [gr4_delay_players[0], gr4_delay_players[1], gr4_delay_players[2], gr4_delay_players[3]]

		




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
	who2=models.IntegerField()
	who4=models.IntegerField()
	grochoi=models.StringField()
	def now(self):
		self.who2=random.choice([1,2])
		self.who4=random.choice([1,2,3,4])
		for p in self.get_players():
			if p.participant.vars["gr"]==2:
				if p.id_in_group==self.who2:
					p.grosel=1
					p.participant.vars["grosel"]=p.grosel
					self.grochoi=p.participant.vars['type']
					p.choi='Version A' if p.participant.vars['type']==p.participant.vars["versiona"] else 'Version B' if p.participant.vars['type']==p.participant.vars["versionb"] else 'Version C' if p.participant.vars['type']==p.participant.vars["versionc"] else 'Version D'
					for i in p.get_others_in_group():
						i.participant.vars["type"]=self.grochoi
						i.choi='Version A' if i.participant.vars['type']==i.participant.vars["versiona"] else 'Version B' if i.participant.vars['type']==i.participant.vars["versionb"] else 'Version C' if i.participant.vars['type']==i.participant.vars["versionc"] else 'Version D'
						i.participant.vars["cho"]=i.choi
						i.participant.vars['version']='Basisversion' if i.participant.vars['type']=='base' else 'Performancevergleich' if i.participant.vars['type']=='nudge' else 'Geldanreiz' if i.participant.vars['type']=='mon' else 'Sanktion' 
				else:
					p.grosel=0
					p.participant.vars["grosel"]=p.grosel

			elif p.participant.vars["gr"]==4:
				if p.id_in_group==self.who4:
					p.grosel=1
					p.participant.vars["grosel"]=p.grosel
					self.grochoi=p.participant.vars['type']
					p.choi='Version A' if p.participant.vars['type']==p.participant.vars["versiona"] else 'Version B' if p.participant.vars['type']==p.participant.vars["versionb"] else 'Version C' if p.participant.vars['type']==p.participant.vars["versionc"] else 'Version D'
					for i in p.get_others_in_group():
						i.participant.vars["type"]=self.grochoi
						i.choi='Version A' if i.participant.vars['type']==i.participant.vars["versiona"] else 'Version B' if i.participant.vars['type']==i.participant.vars["versionb"] else 'Version C' if i.participant.vars['type']==i.participant.vars["versionc"] else 'Version D'
						i.participant.vars["cho"]=i.choi
						i.participant.vars['version']='Basisversion' if i.participant.vars['type']=='base' else 'Performancevergleich' if i.participant.vars['type']=='nudge' else 'Geldanreiz' if i.participant.vars['type']=='mon' else 'Sanktion' 
				else:
					p.grosel=0
					p.participant.vars["grosel"]=p.grosel
			else:
				p.choi="fail"






class Player(BasePlayer):
	choice = models.StringField(initial="noinc")
	choi=models.StringField()
	num=models.IntegerField()
	dec11 = models.IntegerField(min=0, max=50)
	dec21 = models.IntegerField(min=0, max=50)
	dec31 = models.IntegerField(min=0, max=50)
	dec41 = models.IntegerField(min=0, max=50)
	dec51 = models.IntegerField(min=0, max=50)
	ass11 = models.IntegerField(min=0, max=50)
	ass21 = models.IntegerField(min=0, max=50)
	ass31 = models.IntegerField(min=0, max=50)
	ass41 = models.IntegerField(min=0, max=50)
	ass51 = models.IntegerField(min=0, max=50)
	mod = models.StringField(min=0, max=100)
	tadi = models.IntegerField()
	tava = models.IntegerField()
	tod = models.IntegerField()
	nweek = models.IntegerField()
	ptoday = models.FloatField()
	ptoday1 = models.FloatField()
	ptoday2 = models.FloatField()
	ptoday3 = models.FloatField()
	ptoday4 = models.FloatField()
	ptoday5 = models.FloatField()
	ptoday6 = models.FloatField()
	ptoday7 = models.FloatField()
	ptoday8 = models.FloatField()
	ptoday9 = models.FloatField()
	ptoday10 = models.FloatField()
	ptoday11 = models.FloatField()
	pweek = models.FloatField()
	belper = models.IntegerField(min=0, max=100)
	TreeCount=models.FloatField(initial=0)
	wage=models.IntegerField(initial=0)
	treatment=models.StringField()
	punleft=models.IntegerField(initial=10)
	emo=models.IntegerField(initial=2)
	perf_others25=models.FloatField(initial=0)
	perf_others5=models.FloatField(initial=0)
	time=models.FloatField()
	pun=models.IntegerField(initial=5)
	mot1 = models.IntegerField(min=0, max=100)
	mot2 = models.IntegerField(min=0, max=100)
	mot3 = models.IntegerField(min=0, max=100)
	mot4 = models.IntegerField(min=0, max=100)
	mot5 = models.IntegerField(min=0, max=100)
	alter3 = models.FloatField(blank=True)
	rand=models.IntegerField()
	tita=models.FloatField()
	corr = models.IntegerField()
	lets = models.StringField()
	answer = models.StringField()
	comp = models.FloatField()
	tryans = models.IntegerField(initial=0)
	grosel= models.IntegerField()
	group_idp=models.IntegerField()
	id_in_group2 = models.IntegerField()


	def ti(self):
		self.participant.vars["tita"]=round(time.time()*1000,0)




	def chotrea(self):
		self.sell=random.choice([1,2,3])
		np.random.choice(np.arange(1, 5), p=[0.37, 0.29, 0.21, 0.13])
		if self.sell==1:
			k=[self.participant.vars['first1'],self.participant.vars['first2'],self.participant.vars['first3'],self.participant.vars['first4'],self.participant.vars['first5'],self.participant.vars['first6'],self.participant.vars['first7'],self.participant.vars['first8'],self.participant.vars['first9'],self.participant.vars['first10']]
			di1={0:0,1:0.1,2:0.25,3:0.5,4:0.75,5:1,6:1.5,7:2,8:3,9:5}
			self.num = np.random.choice(np.arange(0,len(k)), p=[0.155, 0.155, 0.115, 0.115,0.115, 0.115, 0.075, 0.075,0.06,0.02])
			self.vextrapay= di1[self.num] if k[self.num]!=self.participant.vars['first'] else 0
			self.comp=1 if k[self.num]!=self.participant.vars['first'] else 0
			self.participant.vars['comp']=self.comp
			self.participant.vars['endowment']+=self.vextrapay
			self.participant.vars['extrpay']=self.vextrapay
			self.choi = k[self.num]
			self.participant.vars['cho']=self.choi
			self.participant.vars['type']=self.in_round(1).versiona if self.choi=='Version A' else self.in_round(1).versionb if self.choi=='Version B' else self.in_round(1).versionc if self.choi=='Version C' else self.in_round(1).versiond if self.choi=='Version D' else self.in_round(1).versione
			self.participant.vars['version']='Basisversion' if self.participant.vars['type']=='base' else 'Performancevergleich' if self.participant.vars['type']=='nudge' else 'Geldanreiz' if self.participant.vars['type']=='mon' else 'Sanktion' if self.participant.vars['type']=='punish' else 'Vorgabe'
		elif self.sell==2:
			l=[self.participant.vars['second1'],self.participant.vars['second2'],self.participant.vars['second3'],self.participant.vars['second4'],self.participant.vars['second5'],self.participant.vars['second6'],self.participant.vars['second7'],self.participant.vars['second8'],self.participant.vars['second9'],self.participant.vars['second10']]
			di1={0:0,1:0.1,2:0.25,3:0.5,4:0.75,5:1,6:1.5,7:2,8:3,9:5}
			self.num = np.random.choice(np.arange(0,len(l)), p=[0.155, 0.155, 0.115, 0.115,0.115, 0.115, 0.075, 0.075,0.06,0.02])
			self.vextrapay= di1[self.num] if l[self.num]!=self.participant.vars['first']  else 0
			self.comp=1 if l[self.num]!=self.participant.vars['first'] else 0
			self.participant.vars['comp']=self.comp
			self.participant.vars['extrpay']=self.vextrapay
			self.participant.vars['endowment']+=self.vextrapay
			self.choi = l[self.num]
			self.participant.vars['cho']=self.choi
			self.participant.vars['type']=self.in_round(1).versiona if self.choi=='Version A' else self.in_round(1).versionb if self.choi=='Version B' else self.in_round(1).versionc if self.choi=='Version C' else self.in_round(1).versiond if self.choi=='Version D' else self.in_round(1).versione
			self.participant.vars['version']='Basisversion' if self.participant.vars['type']=='base' else 'Performancevergleich' if self.participant.vars['type']=='nudge' else 'Geldanreiz' if self.participant.vars['type']=='mon' else 'Sanktion' if self.participant.vars['type']=='punish' else 'Vorgabe'
		elif self.sell==3:
			m=[self.participant.vars['third1'],self.participant.vars['third2'],self.participant.vars['third3'],self.participant.vars['third4'],self.participant.vars['third5'],self.participant.vars['third6'],self.participant.vars['third7'],self.participant.vars['third8'],self.participant.vars['third9'],self.participant.vars['third10']]
			di1={0:0,1:0.1,2:0.25,3:0.5,4:0.75,5:1,6:1.5,7:2,8:3,9:5}
			self.num = np.random.choice(np.arange(0,len(m)), p=[0.155, 0.155, 0.115, 0.115,0.115, 0.115, 0.075, 0.075,0.06,0.02])
			self.vextrapay= di1[self.num] if m[self.num]!=self.participant.vars['first']  else 0
			self.comp=1 if m[self.num]!=self.participant.vars['first'] else 0
			self.participant.vars['comp']=self.comp
			self.participant.vars['endowment']+=self.vextrapay
			self.participant.vars['extrpay']=self.vextrapay
			self.choi = m[self.num]
			self.participant.vars['cho']=self.choi
			self.participant.vars['type']=self.in_round(1).versiona if self.choi=='Version A' else self.in_round(1).versionb if self.choi=='Version B' else self.in_round(1).versionc if self.choi=='Version C' else self.in_round(1).versiond if self.choi=='Version D' else self.in_round(1).versione
			self.participant.vars['version']='Basisversion' if self.participant.vars['type']=='base' else 'Performancevergleich' if self.participant.vars['type']=='nudge' else 'Geldanreiz' if self.participant.vars['type']=='mon' else 'Sanktion' if self.participant.vars['type']=='punish' else 'Vorgabe'

	def versionen(self):
		self.versiona='base' if self.participant.vars['noinc']==1 else 'nudge' if self.participant.vars['nudge']==1 else 'mon' if self.participant.vars['mon']==1 else 'punish' if self.participant.vars['punish']==1 else 'force'
		self.versionb='base' if self.participant.vars['noinc']==2 else 'nudge' if self.participant.vars['nudge']==2 else 'mon' if self.participant.vars['mon']==2 else 'punish' if self.participant.vars['punish']==2 else 'force'
		self.versionc='base' if self.participant.vars['noinc']==3 else 'nudge' if self.participant.vars['nudge']==3 else 'mon' if self.participant.vars['mon']==3 else 'punish' if self.participant.vars['punish']==3 else 'force'		
		self.versiond='base' if self.participant.vars['noinc']==4 else 'nudge' if self.participant.vars['nudge']==4 else 'mon' if self.participant.vars['mon']==4 else 'punish' if self.participant.vars['punish']==4 else 'force'
		self.versione='base' if self.participant.vars['noinc']==5 else 'nudge' if self.participant.vars['nudge']==5 else 'mon' if self.participant.vars['mon']==5 else 'punish' if self.participant.vars['punish']==5 else 'force'
#		
	def saverank(self):
		self.participant.vars['first']=self.first
		self.participant.vars['second']=self.second
		self.participant.vars['third']=self.third
		self.participant.vars['fourth']=self.fourth
	
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
		self.participant.vars["belper"]=self.belper
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
		var1=[self.ptoday1,self.ptoday2,self.ptoday3,self.ptoday4,self.ptoday5,self.ptoday6,self.ptoday7,self.ptoday8,self.ptoday9,self.ptoday10,self.ptoday11]
		self.pweek=var1[self.rand]
		self.participant.vars["wowe"]=var1[self.rand]
		if var1[self.rand]==0:
			self.ptoday=0
			self.participant.vars["woto"]=0
		else:
			self.ptoday=5
			self.participant.vars["woto"]=5


	def treaty(self):
		self.treatment=self.participant.vars['type']
		self.participant.vars["punleft"]=self.punleft

	def calc_first_pay(self):
		self.participant.vars["payoff1"]=self.participant.vars['endowment']
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


		if self.round_number==1:
			if self.perf_others25 <= self.round_number*0.33:
				self.emo=1
			elif self.perf_others5 > self.round_number*0.33 :
				self.emo=3
			else:
				self.emo=2
		else:
			if self.perf_others25 <= self.round_number*0.33:
				self.emo=1
			elif self.perf_others5 > self.round_number*0.33:
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
		self.participant.vars["rn"]=44
		self.participant.vars['first2']='test'
		self.participant.vars['second2']='test'
		self.participant.vars['third2']='test'
		self.participant.vars['fourth2']='test'




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
		'wee': "Gesamtbetrag",
		'now1':"(Gesamtbetrag - 5,25€)",
		'now2':"(Gesamtbetrag - 5,50€)",
		'now3':"(Gesamtbetrag - 5,75€)",
		'now4':"(Gesamtbetrag - 6,00€)",
		'now5':"(Gesamtbetrag - 6,25€)",
		'now6':"(Gesamtbetrag - 6,50€)",
		'now7':"(Gesamtbetrag - 6,75€)",
		'now8':"(Gesamtbetrag - 7,00€)",
		'now9':"(Gesamtbetrag - 7,25€)",
		'now10':"(Gesamtbetrag - 7,50€)",
		'now11':"(Gesamtbetrag - 7,75€)",
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
		'tree':int((self.round_number-4)*333),
		'tree1':int(math.floor(self.round_number-4)/3),
		'tree_count':self.round_number,
		'wage_dis':0,
		'pun_dis':5,
		'perf25':self.perf_others25,
		'perf5':self.perf_others5,
		'face': 2,
		'tita':int(self.participant.vars["tita"]),
		'lets':self.lets.replace(',', ''),
		'A0':self.lets.split(',')[0],
		'A1':self.lets.split(',')[1],
		'A2':self.lets.split(',')[2],
		'A3':self.lets.split(',')[3],
		'A4':self.lets.split(',')[4],
		'A5':self.lets.split(',')[5],
		'A6':self.lets.split(',')[6],
		'A7':self.lets.split(',')[7],
		'A8':self.lets.split(',')[8],
		'A9':self.lets.split(',')[9],
		'A10':self.lets.split(',')[10],
		'A11':self.lets.split(',')[11],
		'A12':self.lets.split(',')[12],
		'A13':self.lets.split(',')[13],
		'A14':self.lets.split(',')[14],
		'A15':self.lets.split(',')[15],
		'A16':self.lets.split(',')[16],
		'A17':self.lets.split(',')[17],
		'A18':self.lets.split(',')[18],
		'A19':self.lets.split(',')[19],
		'A20':self.lets.split(',')[20],
		'A21':self.lets.split(',')[21],
		'A22':self.lets.split(',')[22],
		'A23':self.lets.split(',')[23],
		'A24':self.lets.split(',')[24],
		'A25':self.lets.split(',')[25],
		'A26':self.lets.split(',')[26],
		'A27':self.lets.split(',')[27],
		'A28':self.lets.split(',')[28],
		'A29':self.lets.split(',')[29],
		'A30':self.lets.split(',')[30],
		'A31':self.lets.split(',')[31],
		'A32':self.lets.split(',')[32],
		'A33':self.lets.split(',')[33],
		'A34':self.lets.split(',')[34],
		'A35':self.lets.split(',')[35],
		'A36':self.lets.split(',')[36],
		'A37':self.lets.split(',')[37],
		'A38':self.lets.split(',')[38],
		'A39':self.lets.split(',')[39],
		'A40':self.lets.split(',')[40],
		'A41':self.lets.split(',')[41],
		'A42':self.lets.split(',')[42],
		'A43':self.lets.split(',')[43],
		'A44':self.lets.split(',')[44],
		'A45':self.lets.split(',')[45],
		'A46':self.lets.split(',')[46],
		'A47':self.lets.split(',')[47],
		'A48':self.lets.split(',')[48],
		'A49':self.lets.split(',')[49],
		'A50':self.lets.split(',')[50],
		'A51':self.lets.split(',')[51],
		'A52':self.lets.split(',')[52],
		'A53':self.lets.split(',')[53],
		'A54':self.lets.split(',')[54],
		'A55':self.lets.split(',')[55],
		'A56':self.lets.split(',')[56],
		'A57':self.lets.split(',')[57],
		'A58':self.lets.split(',')[58],
		'A59':self.lets.split(',')[59],
		'A60':self.lets.split(',')[60],
		'A61':self.lets.split(',')[61],
		'A62':self.lets.split(',')[62],
		'A63':self.lets.split(',')[63],
		'A64':self.lets.split(',')[64],
		'A65':self.lets.split(',')[65],
		'A66':self.lets.split(',')[66],
		'A67':self.lets.split(',')[67],
		'A68':self.lets.split(',')[68],
		'A69':self.lets.split(',')[69],
		'A70':self.lets.split(',')[70],
		'A71':self.lets.split(',')[71],
		'A72':self.lets.split(',')[72],
		'A73':self.lets.split(',')[73],
		'A74':self.lets.split(',')[74],
		'A75':self.lets.split(',')[75],
		'A76':self.lets.split(',')[76],
		'A77':self.lets.split(',')[77],
		'A78':self.lets.split(',')[78],
		'A79':self.lets.split(',')[79],
		'A80':self.lets.split(',')[80],
		'A81':self.lets.split(',')[81],
		'A82':self.lets.split(',')[82],
		'A83':self.lets.split(',')[83],
		'A84':self.lets.split(',')[84],
		'A85':self.lets.split(',')[85],
		'A86':self.lets.split(',')[86],
		'A87':self.lets.split(',')[87],
		'A88':self.lets.split(',')[88],
		'A89':self.lets.split(',')[89],
		'A90':self.lets.split(',')[90],
		'A91':self.lets.split(',')[91],
		'A92':self.lets.split(',')[92],
		'A93':self.lets.split(',')[93],
		'A94':self.lets.split(',')[94],
		'A95':self.lets.split(',')[95],
		'A96':self.lets.split(',')[96],
		'A97':self.lets.split(',')[97],
		'A98':self.lets.split(',')[98],
		'A99':self.lets.split(',')[99],
		'corr':self.corr,
		'answ':self.answer,
	}


	wrong = models.IntegerField(initial=0)

