from collections import Mapping
from locale import getdefaultlocale, normalize


def normalize_lang(lang):
    return normalize(lang).split('.')[0]


def get_default_lang():
    return getdefaultlocale()[0]


class LocaleDict(dict):

    def __new__(cls, data=None):
        self = dict.__new__(cls)

        if data:

            if not isinstance(data, Mapping):
                raise ValueError(
                    'Initial data must be instance of any mapping')

            for k, v in data.items():
                self[normalize_lang(k)] = unicode(v)

        return self

    def __init__(self, *args, **kwargs):
        pass

    def __getitem__(self, key):
        return super(LocaleDict, self).__getitem__(normalize_lang(key))

    def __setitem__(self, key, value):
        return super(LocaleDict, self).__setitem__(
            normalize_lang(key), unicode(value))


class MultilingualString(unicode):

    def __new__(cls, translations=None, default_language=None):
        language = (default_language and normalize_lang(default_language) or
            get_default_lang())
        translations = LocaleDict(translations)
        value = translations.get(language, u'')
        self = unicode.__new__(cls, value)
        self.language = language
        self.translations = translations
        return self

    def translate(self, language):
        return self.__class__(self.translations, language)
