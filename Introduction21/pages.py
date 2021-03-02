from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from . import models
from .models import Constants
import time
import pandas as pd



class Mailcheck(Page):
	form_model=models.Player
	form_fields=["mail"]

	def mail_error_message(self,value):
		df = pd.read_csv('Introduction21/all_apps_wide_2020-05-13.csv', delimiter=',')
		name=df[df['mail.1.player.id_p'].str.contains(value, na=False)]
		try:
			n=name['mail.1.player.id_p'].values[0]
		except IndexError:
			n="none"
		if not (str(value)) == str(n):
			return 'Der angegebene Anmeldecode ist nicht korrekt. Bitte versuchen Sie es erneut.'

	def before_next_page(self):
		self.player.get_old()

class WaitPage2(WaitPage):
	title_text = "Warten auf andere Teilnehmende"
	body_text = "Btte warten Sie, bis alle Teilnehmenden sich erfolgreich angemeldet haben."
	wait_for_all_groups = True
	def after_all_players_arrive(self):
		self.subsession.create_groups()

class Introduction(Page):
	pass




#class Anleitung(Page):
#	def before_next_page(self):
#		self.player.tim11()
class Anleitung(Page):
	pass







page_sequence = [
	Mailcheck,
	WaitPage2,
	Introduction,
	Anleitung,
]
