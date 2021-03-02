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
        yield Submission(pages.Thanks, dict(mail="hello@web.de",reminder=0,tel='490328509328',mail2='mail2@mail.de'),check_html=False)
        yield Submission(pages.Thanks2, dict(spendeWWF=random.randrange(0,34,1),spendeMeerPlastik=random.randrange(0,34,1),spendeMannTafel=random.randrange(0,34,1)),check_html=True)
        yield Submission(pages.Thanks3, dict(predWWF=random.randrange(0,34,1),predMeerPlastik=random.randrange(0,34,1),predMannTafel=random.randrange(0,34,1)),check_html=True)
