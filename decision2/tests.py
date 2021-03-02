from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
import random
from otree.api import (
	Currency as c, currency_range, SubmissionMustFail, Submission
)
import random
import time

class PlayerBot(Bot):

	def play_round(self):
		if self.participant.vars['time']=='immi':
			if self.round_number==4:
				yield	(pages.forward)
		if self.round_number==1:
			if self.participant.vars['time']=='delay':
				yield	(pages.Instr)
		if self.round_number==1:
			if self.participant.vars['time']=='delay':
				if self.participant.vars["sechoi"]==1:
					yield	(pages.Anleitung)
		if self.participant.vars['time']=='delay':
			if self.participant.vars["sechoi"]==1:
				if self.round_number == self.participant.vars['noinc']:
					yield	(pages.b)
		if self.participant.vars['time']=='delay':
			if self.participant.vars["sechoi"]==1:
				if self.round_number == self.participant.vars['nudge']:
					yield	(pages.n)
		if self.participant.vars['time']=='delay':
			if self.participant.vars["sechoi"]==1:
				if self.round_number == self.participant.vars['mon']:
					yield	(pages.m)
		if self.participant.vars['time']=='delay':
			if self.participant.vars["sechoi"]==1:
				if self.round_number == self.participant.vars['punish']:
					yield	(pages.p)
		if self.participant.vars['time']=='delay':
			if self.round_number==4 :
				if self.participant.vars["sechoi"]==1:
					yield	Submission(pages.control, dict(Q1_1=3,Q1_2=4,Q1_3=1,Q1_4=2,Q2=2,Q3=3,Q4=1,Q5=4,Q6=1,Q7=2,wrong=1),check_html=False)
		if self.participant.vars['time']=='delay':
			if self.round_number==4 :
				if self.participant.vars["sechoi"]==1:
					yield	Submission(pages.ranking, dict(first="Version A",second="Version B",third="Version C",fourth="Version D"),check_html=False)
		if self.participant.vars['time']=='delay':
			if self.round_number==4 :
				if self.participant.vars["sechoi"]==1:
					yield	Submission(pages.choi_2, dict(first1="Version A",first2="Version A",first3="Version A",first4="Version A",first5="Version B",first6="Version B",first7="Version B",first8="Version B",first9="Version B",first10="Version B"),check_html=False)
		if self.participant.vars['time']=='delay':
			if self.round_number==4 :
				if self.participant.vars["sechoi"]==1:
					yield	Submission(pages.choi_3,dict(second1="Version A",second2="Version A",second3="Version A",second4="Version A",second5="Version A",second6="Version C",second7="Version C",second8="Version C",second9="Version C",second10="Version C"),check_html=False)
		
		if self.participant.vars['time']=='delay':
			if self.round_number==4 :
				if self.participant.vars["sechoi"]==1:
					yield	Submission(pages.choi_4,dict(third1="Version A",third2="Version A",third3="Version A",third4="Version A",third5="Version A",third6="Version A",third7="Version A",third8="Version D",third9="Version D",third10="Version D"),check_html=False)
		if self.round_number==4:
			if self.participant.vars['time']=='delay':
				yield	Submission(pages.motbel,dict(mot1=random.randrange(0,50,1),mot2=random.randrange(0,50,1),mot3=random.randrange(0,50,1),mot4=random.randrange(0,50,1),mot5=random.randrange(0,50,1)),check_html=False)
		if self.round_number==4:
			if self.participant.vars['time']=='delay':
				yield	Submission(pages.perbel,dict(belper=random.randrange(0,100,1)),check_html=False)
		if self.round_number==4:
			if self.participant.vars['time']=='delay':
				yield	(pages.A_Start)

		if self.participant.vars['time']=='delay':
			if self.round_number>3:
				if self.participant.vars['expiry'] - time.time() >= 1:
					yield   Submission(pages.B_Effort,dict(answer=self.subsession.solution),check_html=False)

		if self.participant.vars['time']=='delay':
			if self.round_number>3:
				if self.participant.vars['expiry'] - time.time() <= 1:
					if self.participant.vars["rnumber"]==self.round_number:
						yield   (pages.Results)
				elif self.round_number==50:
					if self.participant.vars["rnumber"]==self.round_number:
						yield   (pages.Results)
					

