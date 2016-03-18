
from django.forms import CheckboxSelectMultiple
from django.utils.html import conditional_escape, format_html, html_safe


class ThumbnailWidget(CheckboxSelectMultiple):

    def render(self, name, value, attrs=None):
        if self.id_for_label:
            label_for = format_html(' for="{}"', self.id_for_label)
        else:
            label_for = ''

        attrs = dict(self.attrs, **attrs) if attrs else self.attrs

        return format_html(
            '<label{}>{} {} {} </label>',
            label_for, self.tag(attrs), self.choice_label, self
        )
    
    def is_checked(self):
        return self.value == self.choice_value

    def tag(self, attrs=None):
        attrs = attrs or self.attrs
        final_attrs = dict(attrs, type=self.input_type, name=self.name, value=self.choice_value)
        if self.is_checked():
            final_attrs['checked'] = 'checked'
        return format_html('<input{} />', flatatt(final_attrs))

        # '<img src="%s"/>' % value.url

    # def render(self, name=None, value=None, attrs=None, choices=()):
    #     if self.id_for_label:
    #         label_for = format_html(' for="{}"', self.id_for_label)
    #     else:
    #         label_for = ''
    #     attrs = dict(self.attrs, **attrs) if attrs else self.attrs
    #     return format_html(
    #         '<label{}>{} {}</label>', label_for, self.tag(attrs), self.choice_label
    #     )
