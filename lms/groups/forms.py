from django.forms import ModelForm, DateInput
from groups.models import Group


class GroupCreateForm(ModelForm):
    class Meta:
        model = Group
        fields = ["first_name", "last_name", "num_group"]
