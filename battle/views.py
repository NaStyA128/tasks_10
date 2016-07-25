from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseRedirect

from .battle_lib.BattleField import BattleField
from .forms import BattleForm


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


def form_django(request):
    title = None
    if request.method == 'POST':
        form = BattleForm(request.POST or None)
        if form.is_valid():
            armies_number = int(request.POST.get('armies_number'))
            strategy = str(request.POST.get('strategy'))
            squads_number = int(request.POST.get('squads_number'))
            soldiers = int(request.POST.get('soldiers'))
            vehicles = int(request.POST.get('vehicles'))
            battle = BattleField(armies_number=armies_number,
                                 strategy=strategy,
                                 squads_number=squads_number,
                                 soldiers_number=soldiers,
                                 vehicles_number=vehicles)
            title = 'Win army: ' + str(battle.start())
    else:
        form = BattleForm()
        title = 'Form for Battle'
    context = {
        "title": title,
        "form": form
    }
    return render(request, "form_django.html", context)
