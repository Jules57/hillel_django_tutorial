from django import forms


class TriangleForm(forms.Form):
    leg1 = forms.IntegerField(label='First leg', min_value=1)
    leg2 = forms.IntegerField(label='Second leg', min_value=1)
