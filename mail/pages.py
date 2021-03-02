from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from . import models
from .models import Constants,  DataExport


class Thanks(Page):
	form_model=models.Player
	form_fields=["mail","tel","mail2","reminder"]

	def before_next_page(self):
		self.player.belbon()
		self.player.save_payoff()
		DataExport.objects.create( mail=self.player.mail,participant_code = self.player.participant.code, payoff = self.player.payoff, ptoday = self.player.participant.vars["woto"],tel=self.player.tel,mail2=self.player.mail2,idp=self.player.id_p)


class Thanks2(Page):
	form_model=models.Player
	form_fields=["spendeWWF","spendeMannTafel","spendeMeerPlastik","mail","tel","mail2"]

	def error_message(self, values):
		try:
			if values["spendeWWF"] + values["spendeMeerPlastik"] + values["spendeMannTafel"] > 100:
					return 'Sie können maximal ihren gesamten auszuzahlenden Betrag spenden'
		except TypeError:
			try:
				if values["spendeMeerPlastik"] + values["spendeMannTafel"] > 100:
					return 'Sie können maximal ihren gesamten auszuzahlenden Betrag spenden'
			except TypeError:
				try:
					if values["spendeWWF"] + values["spendeMeerPlastik"] > 100:
						return 'Sie können maximal ihren gesamten auszuzahlenden Betrag spenden'
				except TypeError:
					try:
						if values["spendeMannTafel"] > 100:
							return 'Sie können maximal ihren gesamten auszuzahlenden Betrag spenden'
					except TypeError:
						try:
							if values["spendeMeerPlastik"] > 100:
								return 'Sie können maximal ihren gesamten auszuzahlenden Betrag spenden'
						except TypeError:
							try:
								if values["spendeWWF"] > 100:
									return 'Sie können maximal ihren gesamten auszuzahlenden Betrag spenden'
							except TypeError:
								pass

class Thanks3(Page):
	form_model=models.Player
	form_fields=["predWWF","predMannTafel","predMeerPlastik"]

	def error_message(self, values):
		try:
			if values["predWWF"] + values["predMeerPlastik"] + values["predMannTafel"] > 100:
					return 'Sie können maximal ihren gesamten auszuzahlenden Betrag spenden'
		except TypeError:
			try:
				if values["predMeerPlastik"] + values["predMannTafel"] > 100:
					return 'Sie können maximal ihren gesamten auszuzahlenden Betrag spenden'
			except TypeError:
				try:
					if values["predWWF"] + values["predMeerPlastik"] > 100:
						return 'Sie können maximal ihren gesamten auszuzahlenden Betrag spenden'
				except TypeError:
					try:
						if values["predMannTafel"] > 100:
							return 'Sie können maximal ihren gesamten auszuzahlenden Betrag spenden'
					except TypeError:
						try:
							if values["predMeerPlastik"] > 100:
								return 'Sie können maximal ihren gesamten auszuzahlenden Betrag spenden'
						except TypeError:
							try:
								if values["predWWF"] > 100:
									return 'Sie können maximal ihren gesamten auszuzahlenden Betrag spenden'
							except TypeError:
								pass


page_sequence = [Thanks, Thanks2,Thanks3]
