from django.shortcuts import render
from django.http import HttpResponse

from .battle_lib.BattleField import BattleField


def index(request):
    if request.method == 'POST':
        armies_number = int(request.POST.get('arm_num'))
        strategy = str(request.POST.get('strat'))
        squads_number = int(request.POST.get('squad'))
        soldiers = int(request.POST.get('sold'))
        vehicles = int(request.POST.get('vehic'))
        battle = BattleField(armies_number=armies_number,
                             strategy=strategy,
                             squads_number=squads_number,
                             soldiers_number=soldiers,
                             vehicles_number=vehicles)
        title = 'Win army: ' + str(battle.start())
    else:
        title = 'Form for Battle'
    context = {
        "title": title
    }
    return render(request, "index.html", context)
