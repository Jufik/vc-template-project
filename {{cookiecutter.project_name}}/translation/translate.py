import json
from django.contrib.gis.db import models
from django.conf import settings as SETTINGS
from django import forms


LANGUAGES_CODE = []

for lang in SETTINGS.LANGUAGES:
    if lang[0] not in SETTINGS.BASE_LANGUAGE:
        LANGUAGES_CODE.append(lang[0])


class Translation(models.Model):

    translation = models.TextField(default="{}", editable=False)

    def get_all_translations(self):
        return json.loads(self.translation)

    def set_translation(self, key, lang, value):
        translation = self.get_all_translations()
        if key not in self._translated_fields:
            raise ValueError('%s is not in _translated_fields' % key)
        if lang not in LANGUAGES_CODE:
            raise ValueError('%s is not in LANGUAGES' % lang)
        if key not in translation:
            translation[key] = {}
        translation[key][lang] = value
        self.translation = json.dumps(translation)

    def get_translation(self, key, lang):
        translation = self.get_all_translations()
        if key not in translation:
            return getattr(self, key)
        if lang not in translation[key]:
            return getattr(self, key)
        return translation[key][lang]

    @classmethod
    def add_translation_method(cls, field, lang):
        def translation(self):
            return self.get_translation(field, lang)
        translation.__name__ = '%s_%s' % (field, lang)
        setattr(cls, '%s_%s' % (field, lang), translation)

    @classmethod
    def add_translations_method(cls):
        for field in cls._translated_fields:
            for lang in LANGUAGES_CODE:
                cls.add_translation_method(field, lang)

    class Meta:
        abstract = True


def translatefields(fields):
    def _translatefields(cls):
        # bases = (Translation, ) + cls.__bases__
        # res = type(cls.__name__, bases, {'__module__': __name__})
        # cls.__bases__ = bases
        cls._translated_fields = fields
        cls.add_translations_method()
        return cls
    return _translatefields


def translation_form_for_model(m):

    methods = {}
    for field in m._translated_fields:
        field_type = m._meta.get_field(field).__class__.__name__
        for lang in LANGUAGES_CODE:
            name = '%s_%s' % (field, lang)
            options = {
                'label': name,
                'required': False
            }
            if field_type == 'TextField':
                options['widget'] = forms.Textarea
            if field_type == 'CharField':
                options['max_length'] = m._meta.get_field(field).max_length
            methods[name] = forms.CharField(**options)

    def init(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        for field in m._translated_fields:
            for lang in LANGUAGES_CODE:
                name = '%s_%s' % (field, lang)
                self.fields[name].initial = self.instance.get_translation(field, lang)

    def save(self, *args, **kwargs):
        obj = super(forms.ModelForm, self).save(commit=False)
        for field in m._translated_fields:
            for lang in LANGUAGES_CODE:
                name = '%s_%s' % (field, lang)
                obj.set_translation(field, lang, self.cleaned_data.get(name))
        return obj

    methods['__init__'] = init
    methods['save'] = save
    methods['Meta'] = type('Meta', (object, ), {'model': m, 'exclude': []})

    return type('TranslationForm', (forms.ModelForm, ), methods)

    # class TranslationForm(forms.ModelForm):

    #     class Meta:
    #         # model = m
    #         exclude = []

    #     def __init__(self, *args, **kwargs):
    #         super(TranslationForm, self).__init__(*args, **kwargs)

    # return TranslationForm
