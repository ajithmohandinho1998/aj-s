from django import forms
from .models import address

class addr_update(forms.ModelForm):
    class Meta:
        model=address
        fields=['name','ad_l1','ad_l2','lat','long']
