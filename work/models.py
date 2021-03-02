from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
	Currency as c, currency_range
)
import random


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
	name_in_url = 'work'
	players_per_group = None
	num_rounds = 1


class Subsession(BaseSubsession):
	pass


class Group(BaseGroup):
	pass


class Player(BasePlayer):
	worktoday = models.IntegerField()
	workweek = models.IntegerField()
	devup1 = models.IntegerField()
	devup2 = models.IntegerField()
	devup3 = models.IntegerField()
	devup4 = models.IntegerField()
	devup5 = models.IntegerField()
	devup6 = models.IntegerField()
	devup7 = models.IntegerField()
	devup8 = models.IntegerField()
	devup9 = models.IntegerField(blank=True)
	devdown1 = models.IntegerField()
	devdown2 = models.IntegerField()
	devdown3 = models.IntegerField()
	devdown4 = models.IntegerField()
	devdown5 = models.IntegerField()
	devdown6 = models.IntegerField()
	devdown7 = models.IntegerField()
	devdown8 = models.IntegerField()
	devdown9 = models.IntegerField(blank=True)
	decsion = models.IntegerField()
	workchoi = models.IntegerField()
	extrapay = models.FloatField()
	wotod = models.IntegerField()
	woweek = models.IntegerField()
	mod = models.StringField()
	alter1 = models.IntegerField(blank=True)
	alter2 = models.IntegerField(blank=True)
	ran = models.IntegerField()

	def modi(self):
		self.mod = 'Aufgabenaufteilung'#random.choice(['Umweltaufgabe','Aufgabenaufteilung'])
		self.participant.vars['tak']=self.mod


	def choice_dev(self):
		if self.worktoday==30:
			self.ran=random.randint(0,7)
			self.participant.vars['rand']=self.ran
			var1=[self.devdown1,self.devdown2,self.devdown3,self.devdown4,self.devdown5,self.devdown6,self.devdown7,self.devdown8]
			self.workchoi=var1[self.ran]
			if self.workchoi==2:
				var2=[0,0.05,0.1,0.25,0.5,0.75,1,2]
				self.extrapay=var2[self.ran]
				self.participant.vars['expay']=self.extrapay
				self.participant.vars['endowment'] += self.extrapay
				self.wotod=self.worktoday-1
				self.participant.vars["woto"]=self.wotod
				self.woweek=self.workweek+1
				self.participant.vars["wowe"]=self.woweek
			else:
				self.ran=0
				self.participant.vars['rand']=self.ran
				self.extrapay=0
				self.participant.vars['expay']=self.extrapay
				self.participant.vars['endowment'] += self.extrapay
				self.wotod=self.worktoday-1
				self.participant.vars["woto"]=self.wotod
				self.woweek=self.workweek+1
				self.participant.vars["wowe"]=self.woweek

		elif self.workweek==30:
			self.ran=random.randint(0,7)
			self.participant.vars['rand']=self.ran
			var1=[self.devup1,self.devup2,self.devup3,self.devup4,self.devup5,self.devup6,self.devup7,self.devup8]
			self.workchoi=var1[self.ran]
			if self.workchoi==2:
				var2=[0,0.05,0.1,0.25,0.5,0.75,1,2]
				self.extrapay=var2[self.ran]
				self.participant.vars['expay']=self.extrapay
				self.participant.vars['endowment'] += self.extrapay
				self.wotod=self.worktoday+1
				self.participant.vars["woto"]=self.wotod
				self.woweek=self.workweek-1
				self.participant.vars["wowe"]=self.woweek

				
			else:
				self.ran=0
				self.participant.vars['rand']=self.ran
				self.extrapay=0
				self.participant.vars['expay']=self.extrapay
				self.participant.vars['endowment'] += self.extrapay
				self.wotod = self.worktoday
				self.participant.vars["woto"]=self.wotod
				self.woweek = self.workweek
				self.participant.vars["wowe"]=self.woweek

		else:
			self.ran=random.randint(0,15)
			self.participant.vars['rand']=self.ran
			var1=[self.devup1,self.devup2,self.devup3,self.devup4,self.devup5,self.devup6,self.devup7,self.devup8,self.devdown1,self.devdown2,self.devdown3,self.devdown4,self.devdown5,self.devdown6,self.devdown7,self.devdown8]
			self.workchoi=var1[self.ran]
			if self.workchoi==2:
				var2=[0,0.05,0.1,0.25,0.5,0.75,1,2,0,0.05,0.1,0.25,0.5,0.75,1,2]
				self.extrapay=var2[self.ran]
				self.participant.vars['expay']=self.extrapay
				if self.ran<9:
					self.wotod=self.worktoday+1
					self.participant.vars["woto"]=self.wotod
					self.woweek=self.workweek-1
					self.participant.vars["wowe"]=self.woweek
				else:
					self.wotod=self.worktoday-1
					self.participant.vars["woto"]=self.wotod
					self.woweek=self.workweek+1
					self.participant.vars["wowe"]=self.woweek

				
			else:
				self.ran=0
				self.participant.vars['rand']=self.ran
				self.extrapay=0
				self.participant.vars['expay']=self.extrapay
				self.wotod = self.worktoday
				self.participant.vars["woto"]=self.wotod
				self.woweek = self.workweek
				self.participant.vars["wowe"]=self.woweek



	def vars_for_template(self):
		return {
		'wtodayup':self.worktoday+1,
		'wweekdown':self.workweek-1,
		'wtodaydown':self.worktoday-1,
		'wweekup':self.workweek+1,
		'wtoday':self.worktoday,
		'wweek':self.workweek,
		'wt':self.wotod,
		'ww':self.woweek,
		'modi':self.mod,
		}
