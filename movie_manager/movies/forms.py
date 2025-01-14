from django.forms import ModelForm
from . models import Movieinfo
from . models import CensorInfo

class CensorForm(ModelForm):
    class Meta:
        model = CensorInfo
        fields = '__all__'


class MovieForm(ModelForm):
    class Meta :
        model = Movieinfo
        fields = ['title', 'year', 'description', 'poster', 'censor_details', 'directed_by']
