from . import Units


class Squad:
    """
    Squads are consisted out of a number of units (soldiers or vehicles),
    that behave as a coherent group.
    A squad is active as long as is contains an active unit.
    """
    __units = None
    __health = None

    def __init__(self, **kwargs):
        self.__units = [Units.Solder() for _ in range(1, kwargs['soldiers'] + 1)]
        self.__units += [Units.Vehicles() for _ in range(1, kwargs['vehicles'] + 1)]

    @property
    def get_experience(self):
        """The experience of the squad.

        Returns:
           The sum of all experiences of units.
        """
        return sum([i.get_experience for i in self.__units])

    @property
    def get_health(self):
        """The health of the squad.

        Returns:
           The sum of all health of units.
        """
        self.__health = sum([i.get_health for i in self.__units])
        return self.__health

    @property
    def do_attack(self):
        """The attack of the squad.

        The attack success probability of a squad is determined as the
        arithmetic average o the attack success probability of each member.

        Returns:
            The value of the attack.
        """
        return sum([i.do_attack for i in self.__units]) / len(self.__units)

    def take_damage(self, damage):
        """The damage of the squad.

        The damage received on a successful attack is distributed evenly
        to all squad members. The damage inflicted on a successful attack
        is the accumulation of the damage inflicted by each squad member.

        Args:
            damage: the value of damage, that caused this squad.
        """
        damage /= len(self.__units)
        for i in self.__units:
            i.take_damage(damage)

