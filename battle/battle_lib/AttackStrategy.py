import random
from abc import ABCMeta, abstractmethod


class AttackStrategy:
    """Each time a squad attacks it must choose a target squad, depending
    on the chosen strategy.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def select_squad(self, army):
        """The squad of the army.

        Args:
            army: army number.
        """
        pass


class Random(AttackStrategy):
    """Attack any random squad.
    """

    def select_squad(self, army):
        """The squad of the army.

        Args:
            army: army number.

        Returns:
            The random squad.
        """
        squads = army.get_squads
        random_squad = random.randint(0, len(squads) - 1)
        return squads[random_squad]


class Weakest(AttackStrategy):
    """Attack the weakest opposing squad.
    """

    def select_squad(self, army):
        """The squad of the army.

        Args:
            army: army number.

        Returns:
            The weakest squad.
        """
        res = None
        squads = army.get_squads
        min_experience = min([i.get_experience for i in squads])
        for i in squads:
            if i.get_experience == min_experience:
                res = i
                break
            else:
                res = None
        return res


class Strongest(AttackStrategy):
    """Attack the strongest opposing squad.
    """

    def select_squad(self, army):
        """The squad of the army.

        Args:
            army: army number.

        Returns:
            The strongest squad.
        """
        res = None
        squads = army.get_squads
        max_experience = max([i.get_experience for i in squads])
        for i in squads:
            if i.get_experience == max_experience:
                res = i
                break
            else:
                res = None
        return res

