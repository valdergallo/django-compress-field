from django import forms
from core.models import MyContent


class MyContentForm(forms.ModelForm):
    class Meta:
        model = MyContent
        fields = ('name', 'create_date', 'upload_file')
