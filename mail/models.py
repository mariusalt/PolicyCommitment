from otree.api import (
	models,
	widgets,
	BaseConstants,
	BaseSubsession,
	BaseGroup,
	BasePlayer,
	Currency as c,
	currency_range,
)
import random

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
	name_in_url = 'mail'
	players_per_group = None
	num_rounds = 1


class Subsession(BaseSubsession):
	def creating_session(self):
		for p in self.get_players():
			l="A"
			ls=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9"]
			for i in range(6):
				m=random.choice(ls)
				l=l+m
			l=l+str(p.id_in_group)
			p.id_p=l


class Group(BaseGroup):
	pass


class Player(BasePlayer):
	mail = models.StringField()
	tel = models.StringField(blank=True)
	belbo=models.FloatField()
	mail2 = models.StringField(blank=True)
	spendeWWF=models.IntegerField(blank=True)
	spendeMeerPlastik=models.IntegerField(blank=True)
	spendeMannTafel=models.IntegerField(blank=True)
	reminder = models.IntegerField(choices=[[0,'Ja, ich würde gerne Reminder erhalten.'],
		[1,'Nein, ich möchte keine Reminder erhalten']],
		widget=widgets.RadioSelect
		)

	id_p=models.StringField()
	predWWF = models.IntegerField(blank=True)
	predMannTafel = models.IntegerField(blank=True)
	predMeerPlastik = models.IntegerField(blank=True)


	def belbon(self):
		tperl=self.participant.vars["treecount"]-(self.participant.vars["treecount"]/10)
		tperh=self.participant.vars["treecount"]+(self.participant.vars["treecount"]/10)
		if self.participant.vars["belper"]>tperl and self.participant.vars["belper"]<tperh:
			self.belbo=0.5
		else:
			self.belbo=0
		self.participant.vars["belbo"]=self.belbo

	def save_payoff(self):
		self.payoff=self.participant.vars['payoff1']




class DataExport(models.ExtraModel):
	player = models.Link(Player)
	mail = models.StringField()
	participant_code = models.StringField()
	payoff = models.FloatField()
	ptoday = models.FloatField()
	tel = models.StringField()
	mail2 = models.StringField()
	idp = models.StringField()


def custom_export(players):
	for player in DataExport.objects.order_by('id'):
		yield [player.player, player.participant_code, player.mail,player.payoff,player.ptoday,player.tel,player.mail2,player.idp]
