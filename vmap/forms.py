from django import forms
from django.core.mail import EmailMessage
from django.core.files.storage import default_storage
from .validate_file import validate_file_extension

class VoiceMapping(forms.Form):
    file = forms.FileField(label='画像ファイル', validators=[validate_file_extension])

    def save(self):
        upload_file = self.cleaned_data['file']
        file_name = default_storage.save(upload_file.name, upload_file)
        return default_storage.url(file_name)

class PlotForm(forms.Form):
    file = forms.FileField(label='音声ファイル', validators=[validate_file_extension])

    def save(self):
        upload_file = self.cleaned_data['file']
        file_name = default_storage.save(upload_file.name, upload_file)
        return default_storage.url(file_name)





