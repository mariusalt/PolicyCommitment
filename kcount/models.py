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
	name_in_url = 'kcount'
	players_per_group = None
	num_rounds = 52


class Subsession(BaseSubsession):
	max_round = models.IntegerField()
	correct = models.IntegerField()
	def creating_session(self):
		if self.round_number==1:
			for p in self.get_players():
				l="A"
				ls=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9"]
				for i in range(10):
					m=random.choice(ls)
					l=l+m
				p.id_p=l
				p.participant.vars["id_p"]=p.id_p
				p.participant.vars["sumcorr"]=1
				p.participant.vars["pex"]=0
				p.participant.vars["pun"]=0
				p.participant.vars["wage"]=0
				p.participant.vars["showpay"]=0
				p.participant.vars["hype"]="noinc"

		self.max_round=random.choice([3])#participant.vars
		for i in range(53):
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


class Group(BaseGroup):
	pass

class Player(BasePlayer):
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
	showpay=models.IntegerField(initial=0)
	undertime=models.IntegerField(initial=0)
	id_p=models.StringField()



	def ti(self):
		self.participant.vars["tita"]=round(time.time()*1000,0)
		self.participant.vars['start'] = time.time()

	# for i in range(1,64):
	# 	exec("self.let"+str(x)+" = 'hello'")
	def partvars(self):##########!!!!!!!!!!!!!!delete before study
		self.participant.vars["wrc"]=0
		self.participant.vars["pun"]=int((self.participant.vars["remun"]*self.participant.vars["workload"])*2)
		self.participant.vars["wage"]=0
		self.participant.vars["emo"]=2

	def ti(self):
		self.participant.vars["tita"]=round(time.time()*1000,0)
		self.participant.vars['start'] = time.time()


	def calcres(self):
		if self.wrong==4:
			if self.round_number==4:
				self.wrcount+=1
				self.participant.vars["wrc"]=self.wrcount
			else:	
				self.wrcount = self.in_round(self.round_number-1).wrcount+1
				self.participant.vars["wrc"]=self.wrcount
		self.sumcorr=self.round_number-3-self.participant.vars["wrc"]
		self.participant.vars["sumcorr"]=self.sumcorr
		self.showpay = self.participant.vars["sumcorr"]*int(self.participant.vars["remun"])
		self.participant.vars["showpay"] = self.showpay
		if self.participant.vars["hype"]=="punish":
			if self.participant.vars["undertime"]<self.participant.vars["workload"]*(1/3):
				self.pex=round(self.participant.vars["paywork"]*self.sumcorr,2)-round((self.participant.vars["paywork"]*self.workload)*0.2,2)
				self.participant.vars["pex"]=self.pex
			else:
				self.pex=round(self.participant.vars["paywork"]*self.sumcorr,2)
				self.participant.vars["pex"]=self.pex
		elif self.participant.vars["hype"]=="mon":
			self.pex=round(self.participant.vars["paywork"]*self.sumcorr,2)-round((self.participant.vars["paywork"]*self.workload)*0.2,2)+self.participant.vars["wage"]
			self.participant.vars["pex"]=self.pex
		else:
			self.pex=round(self.participant.vars["paywork"]*self.sumcorr,2)
			self.participant.vars["pex"]=self.pex

		

	def calcpun(self):
		if self.round_number==4:
			self.undertime=+1
		else:
			self.undertime = self.in_round(self.round_number-1).undertime + 1
		self.participant.vars["undertime"]=self.undertime
		if self.round_number==4:
			self.pun=int((self.participant.vars["remun"]*self.participant.vars["workload"])*2)
			self.participant.vars["pun"]=int((self.participant.vars["remun"]*self.participant.vars["workload"])*2)
		else:
			if self.participant.vars["undertime"]>self.participant.vars["workload"]*(1/3):
				self.participant.vars["pun"]=0
			else:
				self.participant.vars["pun"]=int((self.participant.vars["remun"]*self.participant.vars["workload"])*2)

	def calcbon(self):
		if self.round_number==4:
			self.participant.vars['endowment']=self.participant.vars['endowment']-(self.participant.vars["remun"]*self.participant.vars["workload"])*0.2
			self.wage=int(self.participant.vars["remun"]*3)
		else:
			self.wage=self.in_round(self.round_number-1).wage+self.participant.vars["remun"]*3

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

		if self.round_number==4:
			if self.perf_others25 <= (self.round_number-3)*5:
				self.emo=1
				self.participant.vars["emo"]=self.emo
			elif self.perf_others5 > (self.round_number-3)*5 :
				self.emo=3
				self.participant.vars["emo"]=self.emo
			else:
				self.emo=2
				self.participant.vars["emo"]=self.emo
		else:
			if self.perf_others25 <= (self.round_number-3)*5:
				self.emo=1
				self.participant.vars["emo"]=self.emo
			elif self.perf_others5 > (self.round_number-3)*5:
				self.emo=3
				self.participant.vars["emo"]=self.emo
			else:
				self.emo=2
				self.participant.vars["emo"]=self.emo



	


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
			'round':self.round_number-1,
			'round1':self.round_number-2,

			}

