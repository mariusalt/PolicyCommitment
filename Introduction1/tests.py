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
		if self.round_number ==1:
			yield 	Submission(pages.Introduction, dict(notime=1), check_html=False)
			yield	(pages.Intro_vers)
			yield	(pages.Anleitung)
