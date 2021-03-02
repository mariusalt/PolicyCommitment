from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
	Currency as c, currency_range
)
import random
import itertools
import math
import numpy as np
import time

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
	name_in_url = 'ques'
	players_per_group = None
	num_rounds = 4


class Subsession(BaseSubsession):
	correct = models.IntegerField()
	group_id3 = models.IntegerField(initial=1)
	def creating_session(self):
		players=self.get_players()
		ms=[1,2,3,4]
		ms=random.sample(ms, len(ms))
		turn1 = itertools.cycle(ms)
		for p in players:
			p.participant.vars["noincm"]=next(turn1)
			p.noincm=p.participant.vars["noincm"]
			p.participant.vars["nudgem"]=next(turn1)
			p.nudgem=p.participant.vars["nudgem"]
			p.participant.vars["monm"]=next(turn1)
			p.monm=p.participant.vars["monm"]
			p.participant.vars["punishm"]=next(turn1)
			p.punishm=p.participant.vars["punishm"]
			p.participant.vars["extrawork"]=1
			p.participant.vars["paywork"]=0.12
			p.participant.vars["pex"]=0
			p.participant.vars["sumcorr"]=0
			p.participant.vars["wrc"]=0
			p.participant.vars["remun"]=12
			p.participant.vars["wage"]=0
			p.participant.vars["emo"]=2
			p.participant.vars["pun"]=20
			p.participant.vars["workload"]=1


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


	def group_by_arrival_time_method(self, waiting_players):

		immi_players = [p for p in waiting_players if p.participant.vars["time"]=='immi']
		nochoi_delay_players = [p for p in waiting_players if p.participant.vars['sechoi'] == 0 and p.participant.vars["time"]=='delay']
		sechoi_delay_players = [p for p in waiting_players if p.participant.vars['sechoi'] == 1 and p.participant.vars["time"]=='delay']


		if len(immi_players) >=4:
			ids=[1,2,3,4]
			random.shuffle(ids)
			idsz = itertools.cycle(ids)
			for p in immi_players:
				p.id_in_group3=next(idsz)
				p.group_idp3=self.group_id3
			self.group_id3=self.group_id3+1
			return [immi_players[0],immi_players[1],immi_players[2],immi_players[3]]
		

		if len(nochoi_delay_players) >=4:
			ids=[1,2,3,4]
			random.shuffle(ids)
			idsz = itertools.cycle(ids)
			for p in nochoi_delay_players:
				p.id_in_group3=next(idsz)
				p.group_idp3=self.group_id3
			self.group_id3=self.group_id3+1
			return [nochoi_delay_players[0],nochoi_delay_players[1],nochoi_delay_players[2],nochoi_delay_players[3]]

		if len(sechoi_delay_players) >=4:
			ids=[1,2,3,4]
			random.shuffle(ids)
			idsz = itertools.cycle(ids)
			for p in sechoi_delay_players:
				p.id_in_group3=next(idsz)
				p.group_idp3=self.group_id3
			self.group_id3=self.group_id3+1
			return [sechoi_delay_players[0],sechoi_delay_players[1],sechoi_delay_players[2],sechoi_delay_players[3]]
		waitgroup=[]
		for p in waiting_players:
			if p.waiting_too_long():
				for i in waiting_players:
					waitgroup.append(i)
		waitgroup = list(dict.fromkeys(waitgroup))
			
		if len(waitgroup)==0:
			pass
		elif len(waitgroup)==1:
			return[waitgroup[0]]
		elif len(waitgroup)==2:
			return[waitgroup[0],waitgroup[1]]
		elif len(waitgroup)==3:
			return[waitgroup[0],waitgroup[1],waitgroup[2]]
		elif len(waitgroup)==4:
			return[waitgroup[0],waitgroup[1],waitgroup[2],waitgroup[3]]






class Group(BaseGroup):
	gencon1=models.IntegerField()
	gencon2=models.IntegerField()
	gencon3=models.IntegerField()
	def set_payoff(self):
		contributions = {}
		oldpgg=[10, 0, 13, 3, 20, 0, 0, 0, 8, 0, 0, 0, 3, 10, 13, 10, 0, 0, 0, 10, 1, 0, 1, 0, 13, 0, 0, 7, 0, 0, 20, 7, 13, 13, 0, 0, 0, 20, 20, 0, 0, 20, 0, 0, 13, 3, 7, 7, 13, 4, 0, 0, 9, 20, 20, 20, 20, 11, 9, 20, 7, 3, 10, 7, 4, 10, 0, 13, 13, 0, 0, 7, 3, 0, 3, 0, 3, 0, 3, 0, 7, 5, 13, 0, 0, 0, 4, 8, 0, 20]
		self.gencon1=oldpgg[random.choice(oldpgg)]	
		self.gencon2=oldpgg[random.choice(oldpgg)]	
		self.gencon3=oldpgg[random.choice(oldpgg)]		

		for p in self.get_players():
			if p.id_in_group==1:
				conds = [p.c0,p.c1,p.c2,
						p.c3,p.c4,p.c5,
						p.c6,p.c7,p.c8,
						p.c9,p.c10,p.c11,p.c12,p.c13,p.c14,p.c15,p.c16,p.c17,p.c18,p.c19,p.c20]
				if len(p.get_others_in_group())==3:
					others = p.get_others_in_group()
					av = 0
					for p in others:
						try:
							av+=p.contri
						except TypeError:
							av+=random.choice(oldpgg)
					av=round(av/4)

					contributions[1]=conds[av]
				elif len(p.get_others_in_group())==2:
					others = p.get_others_in_group()
					av = 0
					for p in others:
						try:
							av+=p.contri
						except TypeError:
							av+=random.choice(oldpgg)
					av+=self.gencon1
					av=round(av/4)

					contributions[1]=conds[av]

				elif len(p.get_others_in_group())==1:
					others = p.get_others_in_group()
					av = 0
					for p in others:
						av+=p.contri
					av+=self.gencon1
					av+=self.gencon2
					av=round(av/4)

					contributions[1]=conds[av]
				else:
					av=round((self.gencon1 + self.gencon2 + self.gencon3)/3)
					contributions[1]=conds[av]
					

			else:
				contributions[p.id_in_group]=p.contri
				

		if len(p.get_others_in_group())==2:
			contributions[4]=self.gencon1
		elif len(p.get_others_in_group())==1:
			contributions[3]=self.gencon1
			contributions[4]=self.gencon2
		elif len(p.get_others_in_group())==0:
			contributions[2]=self.gencon1
			contributions[3]=self.gencon2
			contributions[4]=self.gencon3

		all_contri = 0
		for key in contributions:
			all_contri+=contributions[key]

		for p in self.get_players():
			p.set_payoff(all_contri,contributions[p.id_in_group])



	# project = models.FloatField()
	# pay_proj = models.FloatField()

	# def calc_payoff(self):
	# 	PA = self.get_player_by_role('A')
	# 	PB = self.get_player_by_role('B')
	# 	PC = self.get_player_by_role('C')
	# 	PD = self.get_player_by_role('D')
	# 	outcome=random.choice([1,2,3,4])
	# 	if outcome==1:
	# 		self.project=PA.cond+PB.contri+PC.contri+PD.contri
	# 		self.pay_proj=Constants.MPCR*self.project
	# 		PA.payoff=20-PA.cond+self.pay_proj
	# 		PB.payoff=20-PB.contri+self.pay_proj
	# 		PC.payoff=20-PC.contri+self.pay_proj
	# 		PD.payoff=20-PD.contri+self.pay_proj
	# 	elif outcome==2:
	# 		self.project=PA.contri+PB.cond+PC.contri+PD.contri
	# 		self.pay_proj=Constants.MPCR*self.project
	# 		PA.payoff=20-PA.contri+self.pay_proj
	# 		PB.payoff=20-PB.cond+self.pay_proj
	# 		PC.payoff=20-PC.contri+self.pay_proj
	# 		PD.payoff=20-PD.contri+self.pay_proj
	# 	elif outcome==3:
	# 		self.project=PA.contri+PB.contri+PC.cond+PD.contri
	# 		self.pay_proj=Constants.MPCR*self.project
	# 		PA.payoff=20-PA.contri+self.pay_proj
	# 		PB.payoff=20-PB.contri+self.pay_proj
	# 		PC.payoff=20-PC.cond+self.pay_proj
	# 		PD.payoff=20-PD.contri+self.pay_proj
	# 	else:
	# 		self.project=PA.contri+PB.contri+PC.contri+PD.cond
	# 		self.pay_proj=Constants.MPCR*self.project
	# 		PA.payoff=20-PA.contri+self.pay_proj
	# 		PB.payoff=20-PB.contri+self.pay_proj
	# 		PC.payoff=20-PC.contri+self.pay_proj
	# 		PD.payoff=20-PD.cond+self.pay_proj



class Player(BasePlayer):
	c0=models.IntegerField(min=0, max=20)
	c1=models.IntegerField(min=0, max=20)
	c2=models.IntegerField(min=0, max=20)
	c3=models.IntegerField(min=0, max=20)
	c4=models.IntegerField(min=0, max=20)
	c5=models.IntegerField(min=0, max=20)
	c6=models.IntegerField(min=0, max=20)
	c7=models.IntegerField(min=0, max=20)
	c8=models.IntegerField(min=0, max=20)
	c9=models.IntegerField(min=0, max=20)
	c10=models.IntegerField(min=0, max=20)
	c11=models.IntegerField(min=0, max=20)
	c12=models.IntegerField(min=0, max=20)
	c13=models.IntegerField(min=0, max=20)
	c14=models.IntegerField(min=0, max=20)
	c15=models.IntegerField(min=0, max=20)
	c16=models.IntegerField(min=0, max=20)
	c17=models.IntegerField(min=0, max=20)
	c18=models.IntegerField(min=0, max=20)
	c19=models.IntegerField(min=0, max=20)
	c20=models.IntegerField(min=0, max=20)
	contri=models.IntegerField(min=0, max=20)
	tp1 = models.IntegerField()
	tp2 = models.IntegerField()
	tp3 = models.IntegerField()
	tp4 = models.IntegerField()
	tp5 = models.IntegerField()
	r1 = models.IntegerField()
	r2 = models.IntegerField()
	r3 = models.IntegerField()
	r4 = models.IntegerField()
	r5 = models.IntegerField()
	rank1 = models.StringField()
	rank2 = models.StringField()
	rank3 = models.StringField()
	rank4 = models.StringField()
	projectall=models.IntegerField()
	projectpay=models.FloatField()
	conditional=models.IntegerField()
	pay=models.FloatField()
	payall=models.FloatField()
	email=models.StringField(blank=True)
	corr = models.IntegerField()
	lets = models.StringField()
	answer = models.IntegerField()
	wrong = models.IntegerField(initial=0)
	wrcount= models.IntegerField(initial=0)
	sumcorr = models.IntegerField(initial=0)
	pex = models.FloatField()
	pun = models.IntegerField(initial=0)
	wage = models.IntegerField(initial=0)
	tita=models.FloatField()
	emo=models.IntegerField(initial=2)
	time=models.FloatField()
	perf_others25=models.FloatField(initial=0)
	perf_others5=models.FloatField(initial=0)   
	dec11 = models.IntegerField(min=0, max=50)
	dec21 = models.IntegerField(min=0, max=50)
	dec31 = models.IntegerField(min=0, max=50)
	dec41 = models.IntegerField(min=0, max=50)
	dec51 = models.IntegerField(min=0, max=50)
	exwind = models.IntegerField()
	salchoi = models.IntegerField()
	workload = models.IntegerField()
	tryans = models.IntegerField(initial=0)
	eins = models.StringField()
	zwei = models.StringField()
	drei = models.StringField()
	vier = models.StringField()
	week =models.IntegerField()
	noincm=models.IntegerField()
	nudgem=models.IntegerField()
	monm=models.IntegerField()
	punishm=models.IntegerField()
	modind = models.IntegerField()
	selmodi = models.StringField()
	selmotr = models.StringField()
	paywork = models.FloatField()
	id_in_group3 = models.IntegerField()
	group_idp3 = models.IntegerField()
	abcd = models.IntegerField(initial=0)
	ra1=models.FloatField()
	ra2=models.FloatField()
	ra3=models.FloatField()
	ra4=models.FloatField()
	ra5=models.FloatField()
	ra6=models.FloatField()
	ra11=models.FloatField()
	ra12=models.FloatField()
	ra13=models.FloatField()
	ra14=models.FloatField()
	ra15=models.FloatField()
	ra16=models.FloatField()
	ra17=models.FloatField()
	payla=models.FloatField()
	firsto = models.StringField()
	secondo = models.StringField()
	thirdo = models.StringField()
	fourtho = models.StringField()
	guessA = models.IntegerField()
	guessB = models.IntegerField()
	guessC = models.IntegerField()
	guessD = models.IntegerField()
	scoreguess = models.IntegerField(initial=0)
	wrsl1 = models.IntegerField(initial=0, blank=True)
	wrsl2 = models.IntegerField(initial=0, blank=True)
	wrsl3 = models.IntegerField(initial=0, blank=True)
	wrsl4 = models.IntegerField(initial=0, blank=True)
	wrsl5 = models.IntegerField(initial=0, blank=True)





	def waiting_too_long(self):
		return time.time() - self.participant.vars['tout'] > 150


	def set_payoff(self,all_contri,own_contri):
		self.projectall=all_contri
		self.projectpay=all_contri*0.4
		if self.id_in_group==1:
			self.conditional=1
		else:
			self.conditional=2
		self.pay=round(((20-self.contri+self.projectpay)/20),2)
		self.participant.vars["pggpay"] = round(((20-self.contri+self.projectpay)/20),2)
		self.payall = round((self.participant.vars['endowment'] + self.pay),2)
		self.participant.vars['endowment'] = round((self.participant.vars['endowment'] + self.pay),2)


		d={}
		d["Conditional"]=self.id_in_group==1
		d["all_contributions"]=all_contri
		d["other_contri"]=all_contri-own_contri
		d["average_other"]=round((all_contri-own_contri)/3)
		d["own_contri"]=own_contri
		d["pay_from_project"]=c(all_contri*0.4)
		d["pay_from_rest"]=c(20-own_contri)
		self.participant.vars["PGG_dict"]=d

	# def calc_cond(self):
	# 	oldpgg=[0,10,20]
	# 	if len(self.get_others_in_group())==3:
	# 		self.others_contri = int((self.get_others_in_group()[0].contri+self.get_others_in_group()[1].contri+self.get_others_in_group()[2].contri)/3)
	# 		con_lists = [self.c0,self.c1,self.c2,self.c3,self.c4,self.c5,self.c6,self.c7,self.c8,self.c9,self.c10,self.c11,self.c12,self.c13,self.c14,self.c15,self.c16,self.c17,self.c18,self.c19,self.c20]
	# 		self.cond=con_lists[self.others_contri]
	# 	elif len(self.get_others_in_group())==2:
	# 		self.gencon1=oldpgg[random.choice(range(0,len(oldpgg),1))]
	# 		self.others_contri = int((self.get_others_in_group()[0].contri+self.get_others_in_group()[1].contri+self.gencon1)/3)
	# 		con_lists = [self.c0,self.c1,self.c2,self.c3,self.c4,self.c5,self.c6,self.c7,self.c8,self.c9,self.c10,self.c11,self.c12,self.c13,self.c14,self.c15,self.c16,self.c17,self.c18,self.c19,self.c20]
	# 		self.cond=con_lists[self.others_contri]
	# 	elif len(self.get_others_in_group())==2:
	# 		self.gencon1=oldpgg[random.choice(range(0,len(oldpgg),1))]
	# 		self.gencon2=oldpgg[random.choice(range(0,len(oldpgg),1))]
	# 		self.others_contri = int((self.get_others_in_group()[0].contri+self.gencon1+self.gencon2)/3)
	# 		con_lists = [self.c0,self.c1,self.c2,self.c3,self.c4,self.c5,self.c6,self.c7,self.c8,self.c9,self.c10,self.c11,self.c12,self.c13,self.c14,self.c15,self.c16,self.c17,self.c18,self.c19,self.c20]
	# 		self.cond=con_lists[self.others_contri]
	# 	else:
	# 		self.gencon1=oldpgg[random.choice(range(0,len(oldpgg),1))]
	# 		self.gencon2=oldpgg[random.choice(range(0,len(oldpgg),1))]
	# 		self.gencon3=oldpgg[random.choice(range(0,len(oldpgg),1))]
	# 		self.others_contri = int((self.gencon1+self.gencon2+self.gencon3)/3)
	# 		con_lists = [self.c0,self.c1,self.c2,self.c3,self.c4,self.c5,self.c6,self.c7,self.c8,self.c9,self.c10,self.c11,self.c12,self.c13,self.c14,self.c15,self.c16,self.c17,self.c18,self.c19,self.c20]
	# 		self.cond=con_lists[self.others_contri]

	def role(self): 
		if self.id_in_group == 1:
			return "A"
		elif self.id_in_group == 2:
			return "B"
		elif self.id_in_group == 3:
			return "D"
		else:
			return "C"

	def ti(self):
		self.participant.vars["tita"]=round(time.time()*1000,0)
		self.participant.vars['start'] = time.time()


	def calcres(self):
		if self.wrong==4:
			if self.round_number==1:
				self.wrcount+=1
				self.participant.vars["wrc"]=self.wrcount
			else:	
				self.wrcount = self.in_round(self.round_number-1).wrcount+1
				self.participant.vars["wrc"]=self.wrcount
		self.sumcorr=self.round_number-self.participant.vars["wrc"]
		self.participant.vars["sumcorr"]=self.sumcorr
		self.pex=self.participant.vars["paywork"]*self.sumcorr
		self.participant.vars["pex"]=self.pex
		

	def calcpun(self):
		if self.round_number==1:
			self.pun=self.participant.vars["remun"]*self.workload
			self.participant.vars["pun"]=self.participant.vars["remun"]*self.workload
		else:
			self.pun=self.in_round(self.round_number-1).pun+1
			if self.pun>self.workload*(1/3):
				self.participant.vars["pun"]=0
			else:
				self.participant.vars["pun"]=self.participant.vars["remun"]*self.workload

	def calcbon(self):
		if self.round_number==1:
			self.participant.vars['endowment']=self.participant.vars['endowment']-(self.participant.vars["remun"]*self.workload)*0.2
			self.wage=self.participant.vars["remun"]*3
			self.participant.vars['wage']=self.wage/1000
			

		else:
			self.wage=self.in_round(self.round_number-1).wage+self.participant.vars["remun"]*3
			
			self.participant.vars['wage']=self.wage

	def compare(self):
		self.time=int(round(time.time()-self.participant.vars['start']))
		perf5={25:0.8,35:1.6,40:2.4,50:3.2,65:4,75:17.5,85:20,95:22.5,110:25,120:27.5,135:30,145:32.5,160:35,170:37.5,180:40,200:42.5,240:45,260:47.5,300:50,320:52.5,360:55,380:57.5,420:60,440:62.5,480:65,500:67.5,560:70}
		perf25={20:1,28:2,35:3,42:4,50:15,58:17.5,66:20,74:22.5,84:25,93:27.5,102:30,110:32.5,118:35,126:37.5,135:40,144:42.5,154:45,163:47.5,175:50,185:52.5,195:55,205:57.5,215:60,225:62.5,235:65,245:67.5,260:70}
		for key,value in perf25.items():
			if key < self.time:
				self.perf_others25=value
		for key,value in perf5.items():
			if key < self.time:
				self.perf_others5=value

		if self.round_number==1:
			if self.perf_others25 <= self.round_number*5:
				self.emo=1
				self.participant.vars["emo"]=self.emo
			elif self.perf_others5 > self.round_number*5 :
				self.emo=3
				self.participant.vars["emo"]=self.emo
			else:
				self.emo=2
				self.participant.vars["emo"]=self.emo
		else:
			if self.perf_others25 <= self.round_number*5:
				self.emo=1
				self.participant.vars["emo"]=self.emo
			elif self.perf_others5 > self.round_number*5:
				self.emo=3
				self.participant.vars["emo"]=self.emo
			else:
				self.emo=2
				self.participant.vars["emo"]=self.emo

	def decextra(self):
		self.exwind=np.random.choice(np.arange(0,2), p=[0.9, 0.1])#change before run!!!!
		self.participant.vars["exwind"]=self.exwind
		self.week = random.choice([0,1])
		self.participant.vars["week"]=self.week
		if self.week == 0:
			k=[self.participant.vars['dec11w1'],self.participant.vars['dec21w1'],self.participant.vars['dec31w1'],self.participant.vars['dec41w1'],self.participant.vars['dec51w1']]
			self.salchoi=np.random.choice(np.arange(0,5), p=[0.1, 0.2,0.2,0.2,0.3])
			n=[0.14,0.12,0.10,0.08,0.06]
			self.workload=int(round(float(k[self.salchoi])))
			self.participant.vars["workload"]=self.workload
			self.paywork=n[self.salchoi]
			self.participant.vars["paywork"]=n[self.salchoi]
			self.participant.vars["remun"]=self.participant.vars["paywork"]*100
		else:
			k=[self.dec11,self.dec21,self.dec31,self.dec41,self.dec51]
			n=[0.14,0.12,0.10,0.08,0.06]
			self.salchoi=np.random.choice(np.arange(0,5), p=[0.1, 0.2,0.2,0.2,0.3])
			self.workload=int(round(float(k[self.salchoi])))
			self.participant.vars["workload"]=self.workload
			self.paywork=n[self.salchoi]
			self.participant.vars["paywork"]=n[self.salchoi]
			self.participant.vars["remun"]=self.participant.vars["paywork"]*100
		self.participant.vars["pun"]=round(((self.participant.vars["paywork"]*self.workload)*0.2),2)
		self.participant.vars["reward"]=round((self.participant.vars["paywork"]*0.3),2)

	def decextra1(self):
		z=[self.eins,self.zwei,self.drei,self.vier]
		self.modind = np.random.choice(np.arange(0,4), p=[0.4, 0.3, 0.2, 0.1])#change before run!!!!
		self.selmodi = z[self.modind]
		self.participant.vars["selmodi"]=self.selmodi
		if self.selmodi == "Modifikation 1":
			self.selmotr = "noincm" if self.noincm==1 else "nudgem" if self.nudgem==1 else "monm" if self.monm==1 else "punishm"
		elif self.selmodi == "Modifikation 2":
			self.selmotr = "noincm" if self.noincm==2 else "nudgem" if self.nudgem==2 else "monm" if self.monm==2 else "punishm"
		elif self.selmodi == "Modifikation 3":
			self.selmotr = "noincm" if self.noincm==3 else "nudgem" if self.nudgem==3 else "monm" if self.monm==3 else "punishm"
		elif self.selmodi == "Modifikation 4":
			self.selmotr = "noincm" if self.noincm==4 else "nudgem" if self.nudgem==4 else "monm" if self.monm==4 else "punishm"
		self.participant.vars["selmotr"]=self.selmotr
		self.participant.vars["hype"]=self.selmotr

	def guesst(self):
		if self.participant.vars["versiona"]=="noinc":
			if self.guessA>=22 & self.guessA<=24:
				self.scoreguess+=1
		elif self.participant.vars["versiona"]=="nudge":
			if self.guessA>=25 & self.guessA<=27:
				self.scoreguess+=1
		elif self.participant.vars["versiona"]=="mon":
			if self.guessA>=21 & self.guessA<=23:
				self.scoreguess+=1
		elif self.participant.vars["versiona"]=="punish":
			if self.guessA>=20 & self.guessA<=22:
				self.scoreguess+=1

		if self.participant.vars["versionb"]=="noinc":
			if self.guessB>=22 & self.guessB<=24:
				self.scoreguess+=1
		elif self.participant.vars["versionb"]=="nudge":
			if self.guessB>=25 & self.guessB<=27:
				self.scoreguess+=1
		elif self.participant.vars["versionb"]=="mon":
			if self.guessB>=21 & self.guessB<=23:
				self.scoreguess+=1
		elif self.participant.vars["versionb"]=="punish":
			if self.guessB>=20 & self.guessB<=21:
				self.scoreguess+=1

		if self.participant.vars["versionc"]=="noinc":
			if self.guessC>=22 & self.guessC<=24:
				self.scoreguess+=1
		elif self.participant.vars["versionc"]=="nudge":
			if self.guessC>=25 & self.guessC<=26:
				self.scoreguess+=1
		elif self.participant.vars["versionc"]=="mon":
			if self.guessC>=21 & self.guessC<=23:
				self.scoreguess+=1
		elif self.participant.vars["versionc"]=="punish":
			if self.guessC>=20 & self.guessC<=22:
				self.scoreguess+=1

		if self.participant.vars["versiond"]=="noinc":
			if self.guessD>=22 & self.guessD<=24:
				self.scoreguess+=1
		elif self.participant.vars["versiond"]=="nudge":
			if self.guessD>=25 & self.guessD<=27:
				self.scoreguess+=1
		elif self.participant.vars["versiond"]=="mon":
			if self.guessD>=21 & self.guessD<=23:
				self.scoreguess+=1
		elif self.participant.vars["versiond"]=="punish":
			if self.guessD>=20 & self.guessD<=22:
				self.scoreguess+=1


		self.participant.vars["scored"]=round(0.3*self.scoreguess,2)



	def la(self):
		m=random.choice([1,2])
		k=random.choice([self.ra1,self.ra2,self.ra3,self.ra4,self.ra5,self.ra6,self.ra11,self.ra12,self.ra13,self.ra14,self.ra15,self.ra16,self.ra17])
		if float(k)==1.0:
			if m==1:
				self.payla=0
				self.participant.vars["payla"]=self.payla
			else:
				self.payla=1
				self.participant.vars["payla"]=self.payla
		if float(k)!=1.0:
			if float(k)==1.1:
				self.payla=1
				self.participant.vars["payla"]=self.payla
			else:
				self.payla=float(k)
				self.participant.vars["payla"]=self.payla






	def vars_for_template(self):	
			return {
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
			# 'A100':self.lets.split(',')[100],
			# 'A101':self.lets.split(',')[101],
			# 'A102':self.lets.split(',')[102],
			# 'A103':self.lets.split(',')[103],
			# 'A104':self.lets.split(',')[104],
			# 'A105':self.lets.split(',')[105],
			# 'A106':self.lets.split(',')[106],
			# 'A107':self.lets.split(',')[107],
			# 'A108':self.lets.split(',')[108],
			# 'A109':self.lets.split(',')[109],
			# 'A110':self.lets.split(',')[110],
			# 'A111':self.lets.split(',')[111],
			# 'A112':self.lets.split(',')[112],
			# 'A113':self.lets.split(',')[113],
			# 'A114':self.lets.split(',')[114],
			# 'A115':self.lets.split(',')[115],
			# 'A116':self.lets.split(',')[116],
			# 'A117':self.lets.split(',')[117],
			# 'A118':self.lets.split(',')[118],
			# 'A119':self.lets.split(',')[119],
			# 'A120':self.lets.split(',')[120],
			# 'A121':self.lets.split(',')[121],
			# 'A122':self.lets.split(',')[122],
			# 'A123':self.lets.split(',')[123],
			# 'A124':self.lets.split(',')[124],
			# 'A125':self.lets.split(',')[125],
			# 'A126':self.lets.split(',')[126],
			# 'A127':self.lets.split(',')[127],
			# 'A128':self.lets.split(',')[128],
			# 'A129':self.lets.split(',')[129],
			# 'A130':self.lets.split(',')[130],
			# 'A131':self.lets.split(',')[131],
			# 'A132':self.lets.split(',')[132],
			# 'A133':self.lets.split(',')[133],
			# 'A134':self.lets.split(',')[134],
			# 'A135':self.lets.split(',')[135],
			# 'A136':self.lets.split(',')[136],
			# 'A137':self.lets.split(',')[137],
			# 'A138':self.lets.split(',')[138],
			# 'A139':self.lets.split(',')[139],
			# 'A140':self.lets.split(',')[140],
			# 'A141':self.lets.split(',')[141],
			# 'A142':self.lets.split(',')[142],
			# 'A143':self.lets.split(',')[143],
			'corr':self.corr,
			'sumcorr':self.participant.vars["sumcorr"],
			'pex': self.participant.vars["pex"],
			"pun": self.participant.vars["pun"],
			"wage":self.participant.vars["wage"],
			'tita':int(self.participant.vars["tita"]),
			'face': self.participant.vars["emo"],
			'corr':self.corr,
			}
	scu = models.IntegerField()
	ot1 = models.StringField(blank=True)
	ot2 = models.StringField(blank=True)
	ot3 = models.StringField(blank=True)
	ot4 = models.StringField(blank=True)
	makesense = models.PositiveIntegerField(
		choices=[
			[1, "Stimme voll und ganz zu"], 
			[2, "Stimme eher zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher nicht zu"],
			[5, "Stimme überhaupt nicht zu"]
		 ],
		 widget=widgets.RadioSelect)

	selfcont = models.PositiveIntegerField(
		choices=[
			[1, "Trifft überhaupt nicht zu"], 
			[2, "Trifft eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Trifft eher zu"],
			[5, "Trifft voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect)

	patern1 = models.IntegerField(initial=0, blank=True)
	patern2 = models.IntegerField(initial=0, blank=True)
	patern3 = models.IntegerField(initial=0, blank=True)
	patern4 = models.IntegerField(initial=0, blank=True)
	patern5 = models.IntegerField(initial=0, blank=True)
	patern6 = models.IntegerField(initial=0, blank=True)
	patern7 = models.IntegerField(initial=0, blank=True)
	patern8 = models.IntegerField(initial=0, blank=True)
	patern9 = models.IntegerField(initial=0, blank=True)
	patern10 = models.IntegerField(initial=0, blank=True)


	psuswit = models.PositiveIntegerField(
		choices=[
			[1, "eine solche Steuer auf keinen Fall einführen"], 
			[2, "eine solche Steuer eher nicht einführen"],
			[3, "eine solche Steuer eher einführen"],
			[4, "eine solche Steuer auf jeden Fall einführen"],
		 ],
		 widget=widgets.RadioSelect)

	wsuswit = models.PositiveIntegerField(
		choices=[
			[1, "deutlich schlechter stellen"], 
			[2, "ein wenig schlechter stellen"],
			[3, "weder besser noch schlechter stellen"],
			[4, "ein wenig besser stellen"],
			[5, "deutlich besser stellen"],
		 ],
		 widget=widgets.RadioSelect)

	palswit = models.PositiveIntegerField(
		choices=[
			[1, "eine solche Steuer auf keinen Fall einführen"], 
			[2, "eine solche Steuer eher nicht einführen"],
			[3, "eine solche Steuer eher einführen"],
			[4, "eine solche Steuer auf jeden Fall einführen"],
		 ],
		 widget=widgets.RadioSelect)

	walswit = models.PositiveIntegerField(
		choices=[
			[1, "deutlich schlechter stellen"], 
			[2, "ein wenig schlechter stellen"],
			[3, "weder besser noch schlechter stellen"],
			[4, "ein wenig besser stellen"],
			[5, "deutlich besser stellen"],
		 ],
		 widget=widgets.RadioSelect)

	ptaswit = models.PositiveIntegerField(
		choices=[
			[1, "eine solche Steuer auf keinen Fall einführen"], 
			[2, "eine solche Steuer eher nicht einführen"],
			[3, "eine solche Steuer eher einführen"],
			[4, "eine solche Steuer auf jeden Fall einführen"],
		 ],
		 widget=widgets.RadioSelect)

	wtaswit = models.PositiveIntegerField(
		choices=[
			[1, "deutlich schlechter stellen"], 
			[2, "ein wenig schlechter stellen"],
			[3, "weder besser noch schlechter stellen"],
			[4, "ein wenig besser stellen"],
			[5, "deutlich besser stellen"],
		 ],
		 widget=widgets.RadioSelect)

	

	pcrswit = models.PositiveIntegerField(
		choices=[
			[1, "weitgehend eingeschränkt werden (In diesem Fall hätten sehr viel weniger Personen Zugang zu kurzfristigen Krediten)"], 
			[2, "teilweise eingeschränkt werden (In diesem Fall hätten weniger Personen Zugang zu kurzfristigen Krediten"],
			[3, "unverändert beleiben"],
			[4, "liberalisiert werden (In diesem Fall hätten mehr Personen Zugang zu kurzfristigen Krediten)"],
			[5, "weitgehend liberalisiert werden (In diesem Fall hätten sehr viel mehr Personen Zugang zu kurzfristigen Krediten)"],
		 ],
		 widget=widgets.RadioSelect)

	wcrswit = models.PositiveIntegerField(
		choices=[
			[1, "deutlich schlechter stellen"], 
			[2, "ein wenig schlechter stellen"],
			[3, "weder besser noch schlechter stellen"],
			[4, "ein wenig besser stellen"],
			[5, "deutlich besser stellen"],
		 ],
		 widget=widgets.RadioSelect)

	smoke = models.PositiveIntegerField(
		choices=[
			[1, "Nichtraucher"], 
			[2, "Seltener Tabakkonsum"],
			[3, "Gelegentlicher Tabakkonsum"],
			[4, "Häfiger Tabakkonsum"],
		 ],
		 widget=widgets.RadioSelect)

	alc = models.PositiveIntegerField(
		choices=[
			[1, "10 oder mehr die Woche"], 
			[2, "5-10 die Woche"],
			[3, "3-5 die Woche"],
			[4, "1-3 die Woche"],
			[5, "weniger als 1 die Woche, aber manchmal"],
			[6, "Keine"],
		 ],
		 widget=widgets.RadioSelect)

	bmi = models.PositiveIntegerField(
		choices=[
			[1, "Untergewichtig"], 
			[2, "Gesundes Gewicht"],
			[3, "Übergewichtig"],
			[4, "Stark übergewichtig"],
			[5, "Keine Antwort"],
		 ],
		 widget=widgets.RadioSelect)

	altru1 = models.PositiveIntegerField()

	altru2 = models.IntegerField(min=0, max=1000)

	Deserving1 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect)



	Deserving2 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect)

	volun = models.IntegerField(
		choices=[
			[1, '0 gar nicht risikobereit'], 
			[2, '1'],
			[3, '2'],
			[4, "3"],
			[5, "4"],
			[6, "5"],
			[7, "6"],
			[8, "7"],
			[9, "8"],
			[10, "9"],
			[11, "10 sehr risikobereit"]
		 ],
		 blank=True,
		 label="Wie schätzen Sie sich persönlich ein: Sind Sie im Allgemeinen ein risikobereiter Mensch oder versuchen Sie, Risiken zu vermeiden? Bitte kruezen Sie ein Kästchen auf der Skala an, wobei der Wert 0 bedeutet: 'gar nicht risikobereit' und der Wert 10: 'sehr risikobereit'. Mit den Werten dazwischen können Sie Ihre Einschätzung abstufen.",
		 widget=widgets.RadioSelectHorizontal)



	Realization = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect)

	sc1 = models.PositiveIntegerField(
		choices=[
			[1, "Stimmt nicht"], 
			[2, "stimmt kaum"],
			[3, "teils/teils"],
			[4, "stimmt eher"],
			[5, "stimmt genau"],
		 ],
		 widget=widgets.RadioSelect)
	sc1 = models.PositiveIntegerField(
		choices=[
			[1, "Stimmt nicht"], 
			[2, "stimmt kaum"],
			[3, "teils/teils"],
			[4, "stimmt eher"],
			[5, "stimmt genau"],
		 ],
		 widget=widgets.RadioSelect)
	sc2 = models.PositiveIntegerField(
		choices=[
			[1, "Stimmt nicht"], 
			[2, "stimmt kaum"],
			[3, "teils/teils"],
			[4, "stimmt eher"],
			[5, "stimmt genau"],
		 ],
		 widget=widgets.RadioSelect)
	sc3 = models.PositiveIntegerField(
		choices=[
			[1, "Stimmt nicht"], 
			[2, "stimmt kaum"],
			[3, "teils/teils"],
			[4, "stimmt eher"],
			[5, "stimmt genau"],
		 ],
		 widget=widgets.RadioSelect)
	sc1 = models.PositiveIntegerField(
		choices=[
			[1, "Stimmt nicht"], 
			[2, "stimmt kaum"],
			[3, "teils/teils"],
			[4, "stimmt eher"],
			[5, "stimmt genau"],
		 ],
		 widget=widgets.RadioSelect)
	sc4 = models.PositiveIntegerField(
		choices=[
			[1, "Stimmt nicht"], 
			[2, "stimmt kaum"],
			[3, "teils/teils"],
			[4, "stimmt eher"],
			[5, "stimmt genau"],
		 ],
		 widget=widgets.RadioSelect)
	sc5 = models.PositiveIntegerField(
		choices=[
			[1, "Stimmt nicht"], 
			[2, "stimmt kaum"],
			[3, "teils/teils"],
			[4, "stimmt eher"],
			[5, "stimmt genau"],
		 ],
		 widget=widgets.RadioSelect)
	sc6 = models.PositiveIntegerField(
		choices=[
			[1, "Stimmt nicht"], 
			[2, "stimmt kaum"],
			[3, "teils/teils"],
			[4, "stimmt eher"],
			[5, "stimmt genau"],
		 ],
		 widget=widgets.RadioSelect)
	sc7 = models.PositiveIntegerField(
		choices=[
			[1, "Stimmt nicht"], 
			[2, "stimmt kaum"],
			[3, "teils/teils"],
			[4, "stimmt eher"],
			[5, "stimmt genau"],
		 ],
		 widget=widgets.RadioSelect)
	sc8 = models.PositiveIntegerField(
		choices=[
			[1, "Stimmt nicht"], 
			[2, "stimmt kaum"],
			[3, "teils/teils"],
			[4, "stimmt eher"],
			[5, "stimmt genau"],
		 ],
		 widget=widgets.RadioSelect)
	sc9 = models.PositiveIntegerField(
		choices=[
			[1, "Stimmt nicht"], 
			[2, "stimmt kaum"],
			[3, "teils/teils"],
			[4, "stimmt eher"],
			[5, "stimmt genau"],
		 ],
		 widget=widgets.RadioSelect)
	sc10 = models.PositiveIntegerField(
		choices=[
			[1, "Stimmt nicht"], 
			[2, "stimmt kaum"],
			[3, "teils/teils"],
			[4, "stimmt eher"],
			[5, "stimmt genau"],
		 ],
		 widget=widgets.RadioSelect)
	sc11 = models.PositiveIntegerField(
		choices=[
			[1, "Stimmt nicht"], 
			[2, "stimmt kaum"],
			[3, "teils/teils"],
			[4, "stimmt eher"],
			[5, "stimmt genau"],
		 ],
		 widget=widgets.RadioSelect)
	sc12 = models.PositiveIntegerField(
		choices=[
			[1, "Stimmt nicht"], 
			[2, "stimmt kaum"],
			[3, "teils/teils"],
			[4, "stimmt eher"],
			[5, "stimmt genau"],
		 ],
		 widget=widgets.RadioSelect)
	sc13 = models.PositiveIntegerField(
		choices=[
			[1, "Stimmt nicht"], 
			[2, "stimmt kaum"],
			[3, "teils/teils"],
			[4, "stimmt eher"],
			[5, "stimmt genau"],
		 ],
		 widget=widgets.RadioSelect)

	Env1 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect)

	Env2 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect)

	Env3 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect)

	Env4 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect)

	Env5 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect)

	Env6 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect)

	Env7 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect)

	Env8 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect)

	Env9 = models.PositiveIntegerField(
		choices=[
			[1, "Stimme überhaupt nicht zu"], 
			[2, "Stimme eher nicht zu"],
			[3, "Bin unentschieden"],
			[4, "Stimme eher zu"],
			[5, "Stimme voll und ganz zu"],
			[6, "Keine Angabe"]
		 ],
		 widget=widgets.RadioSelect)


	Efficacy1 = models.PositiveIntegerField(
		choices=[
			[1, 'Trifft voll und ganz zu'], 
			[2, 'Trifft zu'],
			[3, 'weder noch'],
			[4, "trifft nicht zu"],
			[5, "Trifft ganz und gar nicht zu"],
			[6, "Keine Angabe"]
		 ],
		 label="Ich definiere mich selbst als umweltbewusste Person.",
		 widget=widgets.RadioSelect)

	Efficacy2 = models.PositiveIntegerField(
		choices=[
			[1, 'Trifft voll und ganz zu'], 
			[2, 'Trifft zu'],
			[3, 'weder noch'],
			[4, "trifft nicht zu"],
			[5, "Trifft ganz und gar nicht zu"],
			[6, "Keine Angabe"]
		 ],
		 label="Ich definiere mich selbst als umweltbewusste Person.",
		 widget=widgets.RadioSelect)

	Efficacy3 = models.PositiveIntegerField(
		choices=[
			[1, 'Trifft voll und ganz zu'], 
			[2, 'Trifft zu'],
			[3, 'weder noch'],
			[4, "trifft nicht zu"],
			[5, "Trifft ganz und gar nicht zu"],
			[6, "Keine Angabe"]
		 ],
		 label="Ich definiere mich selbst als umweltbewusste Person.",
		 widget=widgets.RadioSelect)

	Efficacy4 = models.PositiveIntegerField(
		choices=[
			[1, 'Trifft voll und ganz zu'], 
			[2, 'Trifft zu'],
			[3, 'weder noch'],
			[4, "trifft nicht zu"],
			[5, "Trifft ganz und gar nicht zu"],
			[6, "Keine Angabe"]
		 ],
		 label="Ich definiere mich selbst als umweltbewusste Person.",
		 widget=widgets.RadioSelect)

	wg = models.IntegerField()

	member = models.IntegerField()

	Donation1 = models.PositiveIntegerField(
		choices=[
			[1, 'Ja'], 
			[2, 'Nein'],
			[3, 'Keine Angabe']
		 ],
		 label="Haben Sie im letzten Jahr Spenden über 10€ getätigt?",
		 widget=widgets.RadioSelect)

	Donation2 = models.StringField(
		initial=0,
		blank=True)


	ambig = models.IntegerField(
		choices=[
			[1, '0 gar nicht risikobereit'], 
			[2, '1'],
			[3, '2'],
			[4, "3"],
			[5, "4"],
			[6, "5"],
			[7, "6"],
			[8, "7"],
			[9, "8"],
			[10, "9"],
			[11, "10 sehr risikobereit"]
		 ],
		 label="Wie schätzen Sie sich persönlich ein: Sind Sie im Allgemeinen ein risikobereiter Mensch oder versuchen Sie, Risiken zu vermeiden? Bitte kruezen Sie ein Kästchen auf der Skala an, wobei der Wert 0 bedeutet: 'gar nicht risikobereit' und der Wert 10: 'sehr risikobereit'. Mit den Werten dazwischen können Sie Ihre Einschätzung abstufen.",
		 widget=widgets.RadioSelectHorizontal)
	
	exhaust1 = models.PositiveIntegerField(
		choices=[
			[1, 'Sehr anstrengend'], 
			[2, 'Eher anstrengend'],
			[3, 'Wenig anstrengend'],
			[4, "Überhaupt nicht anstrengend"],
			[5, "Keine Angabe"]         
		 ],
		 label="Wie anstrengend empfanden Sie die Dekodierungsaufgabe in Teil 1?",
		 widget=widgets.RadioSelect)


	gender = models.CharField(
		choices=['weiblich', 'männlich', 'divers', 'keine Angabe'],
		label="Bitte geben Sie ihr Geschlecht an.",
		widget=widgets.RadioSelectHorizontal)

	age = models.PositiveIntegerField(label="Wie alt sind Sie?", min=16, max=100)

	nationality = models.CharField(label="Was ist Ihre Staatsangehörigkeit?")

	language = models.CharField(label="Welche Muttersprache(n) sprechen Sie?")
	uni = models.CharField(label="Welche Muttersprache(n) sprechen Sie?")

	party = models.PositiveIntegerField(
		choices=[
			[1, 'CDU/CSU'], 
			[2, 'SPD'],
			[3, 'AfD'],
			[4, "FDP"],
			[5, "Bündnis 90/Die Grünen"],
			[6, "Die Linke"],
			[7, "andere"],
			[8, "Keine Angabe"]
		 ],
		 label="Welche Partei würden Sie wählen, wenn am nächsten Sonntag Bundestagswahl wäre?",
		 widget=widgets.RadioSelect)



	income = models.CharField(
		choices=['0-500€', '500-1000€', '1500-2000€', '2000-3000€','>3000€','Keine Angabe'],
		label="Bitte geben Sie ihr Geschlecht an.",
		widget=widgets.RadioSelectHorizontal)

	wealth = models.IntegerField()

	encon = models.PositiveIntegerField(
		choices=[
			[1, 'keine Regulierung'],
			[2, 'Vergleich des eignen Verbrauchs mit Energiesparsamen Haushalten in der Nachbarschaft darlegen'], 
			[3, 'Energiesparsamen Haushalten Steuervorteile ermöglichen'],
			[4, 'Zusätzliche Gebühren für energieintensive Haushalte '],
			],

		 label="Welche Regulierung sollte der Staat Ihrer Meinung nach am ehesten anwenden, um energiesparsames Verhalten zum Schutze der Umwelt in deutschen Haushalten zu rhöhen?",
		 widget=widgets.RadioSelect)

	pkw = models.PositiveIntegerField(
		choices=[
			[1, 'keine Regulierung'],
			[2, 'Durch öffentliche Kampagnen gesellschaftliche Normen beeinflussen'], 
			[3, 'Subventionen für umweltfreundliche PKWs'],
			[4, 'Erhöhung der KFZ-Steuer bei Neukauf von weniger umweltfreundlichen PKWs'],
			[5, 'Verbot von weniger umweltfreundlichen PKWs'],
			],

		 label="Welche Regulierung sollte der Staat Ihrer Meinung nach am ehesten anwenden, um den Kauf von umweltfreundlichen PKWs in Deutschland zu fördern?",
		 widget=widgets.RadioSelect)

	flight = models.PositiveIntegerField(
		choices=[
			[1, 'keine Regulierung'],
			[2, 'Durch öffentliche Kampagnen gesellschaftliche Normen beeinflussen'], 
			[3, 'Subventionierung der Bahn'],
			[4, 'Steuer auf Flugtickets erhöhen'],
			[5, 'Inlandsflüge verbieten'],
			],

		 label="Welche Regulierung sollte der Staat Ihrer Meinung nach am ehesten anwenden, um die Anzahl an innerdeutschen Flugreisen zum Schutze des Klimas zu reduzieren?",
		 widget=widgets.RadioSelect)

	nitrat = models.PositiveIntegerField(
		choices=[
			[1, 'keine Regulierung'],
			[2, 'Durch Hervorheben positiver Beispiele die Landwirte zum Umdenken bewegen'], 
			[3, 'Subventionen für sparsame Ausbringung von Düngemitteln auf Feldern'],
			[4, 'Steuern auf Düngemittel'],
			[5, 'Strenge Obergrenzen für Ausbringung von Dünger auf Feldern'],
			],

		 label="Die Ausbringung von Dünger auf landwirtschaftliche Flächen erhöht den Ertrag und senkt tendenziell die Preise für Agrarprodukte. Die Überdüngung landwirtschaftlicher Anbauflächen in Deutschland führt jedoch zu einer Verunreinigung des Grundwassers durch Stickstoff, was vor allem für Kleinkinder schädlich ist. Welche Regulierung sollte der Staat Ihrer Meinung nach am ehesten anwenden, um die Stickstoffbelastung im Grundwasser zu reduzieren?",
		 widget=widgets.RadioSelect)


	
