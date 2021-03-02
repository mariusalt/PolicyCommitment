from . import views
from ._builtin import Bot
from .models import Constants
from otree.api import (
    Currency as c, currency_range, SubmissionMustFail, Submission
)

class PlayerBot(Bot):

    def play_round(self):
        yield (views.B_Effort, dict(answer=self.subsession.solution))
        
