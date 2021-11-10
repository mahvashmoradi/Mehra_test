from django import forms

from .models import ContactInfo


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = ContactInfo
        # fields = ['name','email','comment']
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Name"}),
            'email': forms.TextInput(attrs={'placeholder': "Email"}),
            'comment': forms.Textarea(attrs={'placeholder': "Write Comments", 'cols': 80, 'rows': 3}),
        }
    def clean(self):
        # data from the form is fetched using super function
        super(ContactForm, self).clean()

        # extract the title and text field from the data
        name = self.cleaned_data.get('name')
        comment = self.cleaned_data.get('comment')

        if len(comment) < 10:
            self._errors['comment'] = self.error_class([
                'Your Comment Should Contain a minimum of 10 characters'])

        return self.cleaned_data