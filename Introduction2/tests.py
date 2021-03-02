from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
from otree.api import (
	Currency as c, currency_range, SubmissionMustFail, Submission
)
import random


class PlayerBot(Bot):

	def play_round(self):
		if self.round_number == 1:
			yield	(pages.pre)
			yield	(pages.Anleitung)
			yield	(pages.treatment_pres)
		if self.round_number == self.participant.vars['task_rounds']['A']:
			yield	(pages.b)
		if self.round_number == self.participant.vars['task_rounds']['B']:
			yield	(pages.n)
		if self.round_number == self.participant.vars['task_rounds']['C']:
			yield	(pages.m)
		if self.round_number == self.participant.vars['task_rounds']['D']:
			yield	(pages.p)
		if self.round_number == 4:	
				yield	Submission(pages.control, dict(Q1_1=3,Q1_2=4,Q1_3=1,Q1_4=2,Q2=2,Q3=3,Q4=1,Q5=4,Q6=1,Q7=2,Q8=1,wrong=1),check_html=False)
		if self.participant.vars["ref"] == "other":
			if self.round_number == 4:		
				yield	(pages.grouping)
		if self.round_number == 4:
			yield	Submission(pages.ranking, dict(first="Version A",second="Version B",third="Version C",fourth="Version D"),check_html=False)
			yield	Submission(pages.choi_2, dict(first1="Version A",first2="Version A",first3="Version A",first4="Version A",first5="Version B",first6="Version B",first7="Version B",first8="Version B",first9="Version B",first10="Version B"),check_html=False)
			yield	Submission(pages.choi_3,dict(second1="Version A",second2="Version A",second3="Version A",second4="Version A",second5="Version A",second6="Version C",second7="Version C",second8="Version C",second9="Version C",second10="Version C"),check_html=False)
			yield	Submission(pages.choi_4,dict(third1="Version A",third2="Version A",third3="Version A",third4="Version A",third5="Version A",third6="Version A",third7="Version A",third8="Version D",third9="Version D",third10="Version D"),check_html=False)
		if self.participant.vars["ref"]=="other":
			if self.round_number == 4:
				yield	Submission(pages.ranking2, dict(fir2="Version A",sec2="Version B",thi2="Version C",fou2="Version D"),check_html=False)
				yield	Submission(pages.choi_22, dict(first21="Version A",first22="Version A",first23="Version A",first24="Version A",first25="Version B",first26="Version B",first27="Version B",first28="Version B",first29="Version B",first210="Version B"),check_html=False)
				yield	Submission(pages.choi_23,dict(second21="Version A",second22="Version A",second23="Version A",second24="Version A",second25="Version A",second26="Version C",second27="Version C",second28="Version C",second29="Version C",second210="Version C"),check_html=False)
				yield	Submission(pages.choi_24,dict(third21="Version A",third22="Version A",third23="Version A",third24="Version A",third25="Version A",third26="Version A",third27="Version A",third28="Version D",third29="Version D",third210="Version D"),check_html=False)
				