from . import AttackStrategy
from . import Squad


class Army:
    __squads = None
    __health = None
    __name_army = None

    def __init__(self, **kwargs):
        self.__name_army = str(kwargs.pop('name'))
        self.__squads = [Squad.Squad(**kwargs)
                         for _ in range(1, kwargs.pop('squads')+1)]

    def get_health(self):
        """The health of the army.

        Returns:
           The sum of all health of squads.
        """
        self.__health = sum([i.get_health for i in self.__squads])
        return self.__health

    def get_name(self):
        """The name of the army.

        Returns:
             Name army.
        """
        return self.__name_army

    @property
    def get_squads(self):
        """The squads of the squad.

        Returns:
            A list of the squads of this army. For example:

            [<Battle.Squad.Squad object at 0x7f51b8bacba8>,
            <Battle.Squad.Squad object at 0x7f51b8bacf28>]
        """
        return self.__squads

    def attack(self, army, strategy_):
        """The attack of the army.

        The attack success probability of the sum attack of each squad.

        Args:
            army: the army which we attack.
            strategy: the strategy with which we attack.

        Returns:
            The value of the attack.
        """
        damage = sum([i.do_attack for i in self.__squads]) / \
                 len(self.__squads)
        if damage > 0:
            army.take_damage(damage, strategy_, army)

    @staticmethod
    def take_damage(damage, strategy_name, army):
        """The damage of the army.

        Once the target is determined both the attacking and defending squads
        calculate their attack probability success and the squad with the
        highest probability wins. If the attacking squad wins, damage is dealt
        to the defending side, otherwise no damage is inflicted to the
        attacking side.

        Args:
            damage: the damage that we have caused.
            strategy_name: the strategy with which are attacking us.
            army: the army with which are attacking us.
        """
        if strategy_name == 'random':
            strategy_ = AttackStrategy.Random()
        elif strategy_name == 'weakest':
            strategy_ = AttackStrategy.Weakest()
        else:
            strategy_ = AttackStrategy.Strongest()
        squad = strategy_.select_squad(army)
        squad.take_damage(damage)

