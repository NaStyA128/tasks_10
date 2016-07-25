from . import Army


class BattleField:
    """This simulator is determine a battle outcome based on probability
    calculations.
    """
    __armies_number = 2
    __strategy = 'random'
    __squads_number = 2
    __soldiers_number = 2
    __vehicles_number = 3

    def __init__(self, **kwargs):
        self.__armies_number = kwargs['armies_number']
        self.__strategy = kwargs['strategy']
        self.__squads_number = kwargs['squads_number']
        self.__soldiers_number = kwargs['soldiers_number']
        self.__vehicles_number = kwargs['vehicles_number']

    def start(self):
        """Once the simulator is started all the army squads will start
        attacking each other until there is only one army left.

        Returns:
            Number army, that won the battle.
        """
        win = None
        armies = [Army.Army(squads=self.__squads_number,
                            soldiers=self.__soldiers_number,
                            vehicles=self.__vehicles_number, name=i)
                  for i in range(1, self.__armies_number + 1)]
        while True:
            if len(armies) == 1:
                win = armies[0].get_name()
                break
            else:
                for i in armies:
                    target = armies.copy()
                    target.remove(i)
                    for j in target:
                        i.attack(j, self.__strategy)
                        j.attack(i, self.__strategy)
                        if j.get_health() <= 0:
                            armies.remove(j)
                            target.remove(j)
                    if i.get_health() <= 0:
                        armies.remove(i)
                    if len(armies) == 1:
                        win = armies[0].get_name()
                        break
        return win
