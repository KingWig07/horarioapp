from django import forms

class ExcelUploadForm(forms.Form):
    archivo_excel = forms.FileField(label="Archivo Excel")
