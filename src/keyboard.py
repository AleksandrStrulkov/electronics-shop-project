from src.item import Item


class MixinChange:
	"""Миксин класс, реализующий интерфейс Language"""
	Language = 'EN'

	def __init__(self):
		self.__language = self.Language

	@property
	def language(self):
		return self.__language

	def change_lang(self):
		if self.__language == 'EN':
			self.__language = 'RU'
		else:
			self.__language = 'EN'
		return self.language


class Keyboard(Item, MixinChange):
	pass



