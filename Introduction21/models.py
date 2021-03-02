from otree.api import (
	models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
	Currency as c, currency_range
)
import random
import time
import pandas as pd
import numpy as np
from collections import Counter 


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
	name_in_url = 'Introduction21'
	players_per_group = None
	num_rounds = 1
	df0 = pd.read_csv('Introduction21/all_apps_wide_2020-05-13.csv', delimiter=',')
#	df0 = pd.read_excel('Introduction21/all_apps_wide_2020-08-31.xlsx', sheet_name='Sheet1')
	df = df0[['mail.1.player.id_p',
    'Introduction2zwei.4.player.group_idp',
    'Introduction2zwei.4.player.id_in_group2',
    'Introduction2zwei.4.subsession.group_id',
    'Introduction2.1.player.t_no',
    'Introduction2.1.player.t_nu',
    'Introduction2.1.player.t_mo',
    'Introduction2.1.player.t_pu',
    'Introduction1.1.player.t2',
    'Introduction1.1.player.t1',
    'Introduction1.1.player.gr',
    'Introduction2zwei.4.player.grosel',		
    'Introduction2.4.player.first',
    'Introduction2.4.player.second',
    'Introduction2.4.player.third',
    'Introduction2.4.player.fourth',
    'Introduction2zwei.4.player.dec11',
    'Introduction2zwei.4.player.dec21',
    'Introduction2zwei.4.player.dec31',
    'Introduction2zwei.4.player.dec41',
    'Introduction2zwei.4.player.dec51',
    'Introduction2zwei.4.player.ass11',
    'Introduction2zwei.4.player.ass21',
    'Introduction2zwei.4.player.ass31',
    'Introduction2zwei.4.player.ass41',
    'Introduction2zwei.4.player.ass51',
    'Introduction2zwei.4.player.pweek',
    'mail.1.player.payoff',
    'Introduction2zwei.4.player.ptoday',
    'Introduction2zwei.4.player.ptoday10',
    'Introduction2.4.player.vextrapay',
    'Introduction2.4.player.choi',
    'Introduction2zwei.4.player.choi',
    'Introduction2.1.player.versiona',
    'Introduction2.1.player.versionb',
    'Introduction2.1.player.versionc',
    'Introduction2.1.player.versiond', 
    'Introduction2zwei.4.player.belper',  
    'mail.1.player.belbo',
    'mail.1.player.spendeWWF',
    'mail.1.player.spendeMeerPlastik',
    'mail.1.player.spendeMannTafel']]






class Subsession(BaseSubsession):
	group_number=models.IntegerField()


	def create_groups(self):
		players = self.get_players()
		group_matrix=[]
		gru=[]
		for p in players:
			gru.append(p.group_id2)
		gru=np.array(gru)
		self.group_number=len(np.unique(gru))
		for k in range(self.group_number):
			groupy=[i for i in players if self.group_number == k+1]
			new_group=[]
			while len(groupy)>0:
				new_group.append(groupy.pop())
			group_matrix.append(new_group)
		for i in group_matrix:
			for p in i:
				f=np.random.choice(np.arange(0, 2), p=[0.60, 0.40])
				p.sechoi=f
				p.participant.vars["sechoi"]=p.sechoi
		self.set_group_matrix(group_matrix)


		
			


	
	


class Group(BaseGroup):
	pass


class Player(BasePlayer):
	name=models.StringField()
	sechoi=models.IntegerField()
	t1 = models.StringField(
		choices=['immi','delay'],
		widget=widgets.RadioSelect
		)
	t2=models.StringField(
		choices=['self','other1','other2'],
		widget=widgets.RadioSelect
		)
	time1 = models.FloatField()
	time11 = models.FloatField()
	notime = models.IntegerField(choices=[[0,'Ich habe keine terminlichen Konflikte bezüglich der Bearbeitung von Teil 3'],
		[1,'Die Bearbeitung von Teil 3 ist mir aus terminlichen Gründen nicht möglich']],
		widget=widgets.RadioSelect
		)
	mail = models.StringField()
	t_no = models.IntegerField()
	t_nu = models.IntegerField()
	t_mo = models.IntegerField()
	t_pu = models.IntegerField()
	group_id2=models.IntegerField()

	def get_old(self):		
		name=Constants.df[Constants.df['mail.1.player.id_p'].str.contains(str(self.mail), na=False)]

		# self.participant.vars['type']=str(name['Introduction2.8.player.treat'])
		
		self.participant.vars['group_id']=int(name['Introduction2zwei.4.player.group_idp'].values[0])
		self.group_id2=self.participant.vars['group_id']
		self.participant.vars['id_in_group2']=int(name['Introduction2zwei.4.player.id_in_group2'].values[0])
		self.participant.vars['group_num']=int(name['Introduction2zwei.4.subsession.group_id'].values[0])
		self.participant.vars['noinc']=int(name['Introduction2.1.player.t_no'].values[0])
		self.t_no=int(name['Introduction2.1.player.t_no'].values[0])
		self.participant.vars['nudge']=int(name['Introduction2.1.player.t_nu'].values[0])
		self.t_nu=int(name['Introduction2.1.player.t_nu'].values[0])
		self.participant.vars['mon']=int(name['Introduction2.1.player.t_mo'].values[0])
		self.t_mo=int(name['Introduction2.1.player.t_mo'].values[0])
		self.participant.vars['punish']=int(name['Introduction2.1.player.t_pu'].values[0])
		self.t_pu=int(name['Introduction2.1.player.t_pu'].values[0])
		self.participant.vars['ref']=str(name['Introduction1.1.player.t2'].values[0])
		self.participant.vars['time']=str(name['Introduction1.1.player.t1'].values[0])
		self.participant.vars['gr']=int(name['Introduction1.1.player.gr'].values[0])
		try:
			self.participant.vars['grosel']=int(name['Introduction2zwei.4.player.grosel'].values[0])
		except ValueError:
			pass
		self.participant.vars['firstw1']=str(name['Introduction2.4.player.first'].values[0])
		self.participant.vars['secondw1']=str(name['Introduction2.4.player.second'].values[0])
		self.participant.vars['thirdw1']=str(name['Introduction2.4.player.third'].values[0])
		self.participant.vars['fourthw1']=str(name['Introduction2.4.player.fourth'].values[0])
		self.participant.vars['dec11w1']=int(name['Introduction2zwei.4.player.dec11'].values[0])
		self.participant.vars['dec21w1']=int(name['Introduction2zwei.4.player.dec21'].values[0])
		self.participant.vars['dec31w1']=int(name['Introduction2zwei.4.player.dec31'].values[0])
		self.participant.vars['dec41w1']=int(name['Introduction2zwei.4.player.dec41'].values[0])
		self.participant.vars['dec51w1']=int(name['Introduction2zwei.4.player.dec51'].values[0])
		self.participant.vars['ass11w1']=int(name['Introduction2zwei.4.player.ass11'].values[0])
		self.participant.vars['ass21w1']=int(name['Introduction2zwei.4.player.ass21'].values[0])
		self.participant.vars['ass31w1']=int(name['Introduction2zwei.4.player.ass31'].values[0])
		self.participant.vars['ass41w1']=int(name['Introduction2zwei.4.player.ass41'].values[0])
		self.participant.vars['ass51w1']=int(name['Introduction2zwei.4.player.ass51'].values[0]) 
		self.participant.vars['pweekw1']=float(name['Introduction2zwei.4.player.pweek'].values[0])
		self.participant.vars["payoff1w1"]=int(name['mail.1.player.payoff'].values[0]) 
		self.participant.vars['ptoday']=float(name['Introduction2zwei.4.player.ptoday'].values[0])
		self.participant.vars["payoff1"]=int(name['mail.1.player.payoff'].values[0])-self.participant.vars['pweekw1']
		self.participant.vars['endowment']=self.participant.vars["payoff1"]
		self.participant.vars['ptoday10']=float(name['Introduction2zwei.4.player.ptoday10'].values[0])
		self.participant.vars['vextrapayw1']=float(name['Introduction2.4.player.vextrapay'].values[0])
		self.participant.vars['pweek']=float(self.participant.vars['pweekw1'])-float(self.participant.vars['vextrapayw1'])
		if self.participant.vars["gr"]==0:
			self.participant.vars['chowe']=str(name['Introduction2.4.player.choi'].values[0])
		else:
			self.participant.vars['chowe']=str(name['Introduction2zwei.4.player.choi'].values[0])
		self.participant.vars['versiona']=str(name['Introduction2.1.player.versiona'].values[0])
		self.participant.vars['versionb']=str(name['Introduction2.1.player.versionb'].values[0])
		self.participant.vars['versionc']=str(name['Introduction2.1.player.versionc'].values[0])
		self.participant.vars['versiond']=str(name['Introduction2.1.player.versiond'].values[0])
		if self.participant.vars['chowe']=='Version A':
			self.participant.vars['typewe']=self.participant.vars['versiona']  
		elif self.participant.vars['chowe']=='Version B':
			self.participant.vars['typewe']=self.participant.vars['versionb']  
		elif self.participant.vars['chowe']=='Version C':
			self.participant.vars['typewe']=self.participant.vars['versionc']       
		elif self.participant.vars['chowe']=='Version D':
			self.participant.vars['typewe']=self.participant.vars['versiond']  
		self.participant.vars['belperw1']=int(name['Introduction2zwei.4.player.belper'].values[0])  
		self.participant.vars['belbo']=int(name['mail.1.player.belbo'].values[0]) 
		try:
			self.participant.vars["WWF"]=int(name['mail.1.player.spendeWWF'].values[0]) 
		except ValueError:
			self.participant.vars["WWF"]=0
		try:
			self.participant.vars["Meer"]=int(name['mail.1.player.spendeMeerPlastik'].values[0]) 
		except ValueError:
			self.participant.vars["Meer"]=0
		try:
			self.participant.vars["Mann"]=int(name['mail.1.player.spendeMannTafel'].values[0])     
		except ValueError:
			self.participant.vars["Mann"]=0


		


