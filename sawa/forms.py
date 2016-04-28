# -*- coding: utf-8 -*-
from django import forms

class UploadFileForm(forms.Form):
    input_file = forms.FileField(
        label='Select a file',
        help_text='Upload your data for sentiment analysis'
    )
