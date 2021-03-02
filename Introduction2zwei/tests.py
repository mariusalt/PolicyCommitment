from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
from otree.api import (
	Currency as c, currency_range, SubmissionMustFail, Submission
)
import random
import time 

class PlayerBot(Bot):

	def play_round(self):
		if self.participant.vars["ref"]=="other":
			if self.round_number == 4:
				yield	(pages.group)
		if self.round_number == 4:
			yield	Submission(pages.motbel,dict(mot1=random.randrange(0,50,1),mot2=random.randrange(0,50,1),mot3=random.randrange(0,50,1),mot4=random.randrange(0,50,1),mot5=random.randrange(0,50,1)),check_html=False)
			yield	Submission(pages.perbel,dict(belper=random.randrange(0,100,1)),check_html=False)
		

			yield	(pages.pre1)
			yield	Submission(pages.choice1,dict(dec11=random.randrange(0,51,1),dec21=random.randrange(0,51,1),dec31=random.randrange(0,51,1),dec41=random.randrange(0,51,1),dec51=random.randrange(0,51,1)),check_html=False)
			yield	Submission(pages.pred1,dict(ass11=random.randrange(0,51,1),ass21=random.randrange(0,51,1),ass31=random.randrange(0,51,1),ass41=random.randrange(0,51,1),ass51=random.randrange(0,51,1)),check_html=False)
			yield	(pages.Paysplit,dict(ptoday1=random.choice([5.25,0]),ptoday2=random.choice([5.25,0]),ptoday3=random.choice([5.25,0]),ptoday4=random.choice([5.25,0]),ptoday5=random.choice([5.25,0]),ptoday6=random.choice([5.25,0]),ptoday7=random.choice([5.25,0]),ptoday8=random.choice([5.25,0]),ptoday9=random.choice([5.25,0]),ptoday10=random.choice([5.25,0]),ptoday11=random.choice([5.25,0])))
		if self.round_number==4:
			if self.participant.vars['time']=='immi':
				yield	(pages.A_Start)

		if self.participant.vars['time']=='immi':
			if self.round_number>3:
				if self.participant.vars['expiry'] - time.time() >= 1:
					yield   Submission(pages.B_Effort,dict(answer=self.subsession.solution),check_html=False)
		if self.participant.vars['time']=='immi':
			if self.participant.vars['expiry'] - time.time() <= 1:
				if self.round_number==self.participant.vars["rn"]:
						yield   (pages.Results)
			elif self.round_number==44:
				if self.round_number==self.participant.vars["rn"]:
					yield   (pages.Results)