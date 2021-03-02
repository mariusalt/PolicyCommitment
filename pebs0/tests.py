from otree.api import Currency as c, currency_range
from . import views
from ._builtin import Bot
from .models import Constants
from otree.api import (
	Currency as c, currency_range, SubmissionMustFail, Submission
)
import random
import time

class PlayerBot(Bot):

	def play_round(self):
		if self.round_number == 4 :
			if self.participant.vars['expiry'] - time.time() < 1:
				if   self.participant.vars["exwind"] == 1:
					yield	(views.A_Start)
		if self.round_number>3:
			if self.participant.vars['expiry'] - time.time() < 1:
				if self.participant.vars["exwind"] == 1:
					if self.round_number<=self.participant.vars["workload"]+3:
						yield	Submission(views.B_Effort, dict(answer=self.player.corr),check_html=False)
		if self.round_number>3:
			if self.participant.vars['expiry'] - time.time() < 1:
				if self.participant.vars["exwind"] == 0:
					if self.round_number == 4:
						yield	Submission(views.don,dict(spendeWWF=random.randrange(0,34,1),spendeMeerPlastik=random.randrange(0,34,1),spendeMannTafel=random.randrange(0,34,1)),check_html=False)
					
				else:
					if self.round_number==self.participant.vars["workload"]+4:
						yield	Submission(views.don,dict(spendeWWF=random.randrange(0,34,1),spendeMeerPlastik=random.randrange(0,34,1),spendeMannTafel=random.randrange(0,34,1)),check_html=False)
		
		if self.round_number>3:
			if self.participant.vars['expiry'] - time.time() < 1:
				if self.participant.vars["exwind"] == 0:
					if self.round_number == 4:
						yield	(views.Results)
				else:
					if self.round_number==self.participant.vars["workload"]+4:
						yield	(views.Results)
