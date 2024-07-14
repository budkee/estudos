from django import forms

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=100, label='Assunto')
    message = forms.CharField(widget=forms.Textarea, label='Mensagem')
    recipient = forms.EmailField(label='Destinatário')
