from otree.api import Currency as c, currency_range
from . import pages
from ._builtin import Bot
from .models import Constants
from otree.api import (
	Currency as c, currency_range, SubmissionMustFail, Submission
)
import random
import itertools

class PlayerBot(Bot):

	def play_round(self):
		if self.round_number ==1:
			part=["A3z5asn1"]
			random.shuffle(part)
			part = itertools.cycle(part)
			yield Submission(pages.Mailcheck, {'mail':next(part)},check_html=False)
			yield pages.Introduction
			yield pages.Anleitung


