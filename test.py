# coding: u8
import unittest

from i18n_string import MultilingualString, LocaleDict


class TestMultilingualString(unittest.TestCase):

    def setUp(self):
        self.s = MultilingualString({'en': 'Hermitage', 'ru': u'Эрмитаж'})

    def test001_string_type(self):
        self.assertIsInstance(self.s, MultilingualString)
        s = self.s.translate('en')
        self.assertIsInstance(s, MultilingualString)

    def test002_translations_type(self):
        self.assertIsInstance(self.s.translations, LocaleDict)
        s = self.s.translate('en')
        self.assertIsInstance(s.translations, LocaleDict)

    def test003_translations_data(self):
        self.assertDictEqual(
            self.s.translations,
            {'en_US': u'Hermitage', 'ru_RU': u'Эрмитаж'})

    def test004_translate(self):
        s = self.s.translate('en')
        self.assertMultiLineEqual(s, u'Hermitage')
        s = self.s.translate('ru')
        self.assertMultiLineEqual(s, u'Эрмитаж')

    def test005_translations_update(self):
        self.s.translations['ru'] = u'Государственный Эрмитаж'
        self.assertIsInstance(self.s.translations, LocaleDict)
        self.assertMultiLineEqual(
            self.s.translations['ru'], u'Государственный Эрмитаж')


if __name__ == '__main__':
    unittest.main()
