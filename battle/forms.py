from django import forms


class BattleForm(forms.Form):
    armies_number = forms.IntegerField(
        label='Armies number',
        min_value=2,
        initial=2
    )
    CHOICES = (
        ('random', 'random'),
        ('weakest', 'weakest'),
        ('strongest', 'strongest'),
    )
    strategy = forms.CharField(
        label='Strategy',
        widget=forms.Select(choices=CHOICES)

    )
    squads_number = forms.IntegerField(
        label='Squads number',
        min_value=2,
        initial=2
    )
    soldiers = forms.IntegerField(
        label='Units number (soldiers and vehicles) 5 to 10. Soldiers',
        min_value=1,
        max_value=5,
        initial=3
    )
    vehicles = forms.IntegerField(
        label='Vehicles',
        min_value=1,
        max_value=5,
        initial=3
    )
