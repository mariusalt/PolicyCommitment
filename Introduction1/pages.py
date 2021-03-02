from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from . import models
from .models import Constants
import time



class Tchoice(Page):
	form_model=models.Player
	form_fields=["t1","t2"]

		


class Introduction(Page):
	form_model=models.Player
	form_fields=["notime"]
	def before_next_page(self):
		self.player.endow()

class Intro_vers(Page):
	pass


#class Anleitung(Page):
#	def before_next_page(self):
#		self.player.tim11()
class Anleitung(Page):
	pass







page_sequence = [
#	Tchoice,
	Introduction,
	Intro_vers,
	Anleitung,
]
