import random
import time
from abc import ABCMeta, abstractmethod, abstractproperty


class Unit:
    """Class-parent.

    It contains the methods of attack, take damage. It allow you to set
    for unit a health, a recharge and next attack time. It allow you to get
    these options, and an experience and checking attack.
    Each unit represents either a soldier or a vehicle maned by
    a predetermined number of soldiers.

    Attributes:
        prev_time: the previous attack.
    """

    __metaclass__ = ABCMeta
    __health = None
    __recharge = None
    __next_attack_time = 0
    prev_time = None

    @abstractproperty
    def do_attack(self):
        # атака
        pass

    @abstractmethod
    def take_damage(self, *args):
        # получение атаки и блок
        pass

    @property
    def get_recharge(self):
        """Represents the number of ms required to recharge the unit
        for an attack.

        Returns:
            The value of the attribute 'recharge'.
        """
        return self.__recharge

    def set_recharge(self, recharge):
        """It set the value of the attribute 'recharge'.

        Represents the number of ms required to recharge the unit
        for an attack.

        Args:
            recharge: the value of the recharge.
        """
        self.__recharge = recharge

    @property
    def get_health(self):
        """Represents the health of the unit.

        Returns:
            The value of the attribute 'health'.
        """
        return self.__health

    def set_health(self, health):
        """It set the value of the attribute 'recharge'.

        Represents the health of the unit.

        Args:
            health: the value of the health.
        """
        self.__health = health

    @abstractproperty
    def get_experience(self):
        """Represents the experience of the unit.
        """
        pass

    @property
    def get_next_attack_time(self):
        """Represents the next attack time of the unit.

        Returns:
            The value of the attribute 'next_attack_time'.
        """
        return self.__next_attack_time

    def set_next_attack_time(self, next_attack_time):
        """It set the value of the attribute 'next_attack_time'.

        Represents the next attack time of the unit.

        Args:
            next_attack_time: the value of the next attack time.
        """
        self.__next_attack_time = next_attack_time

    def check_attack(self):
        """We check, can a unit to attack.

        Returns:
             True: if now time exceed next attack time or if the unit
             do not attacked.

             False: if now time do not exceed next attack time.
        """
        now = time.time() * 1000
        if self.prev_time is None:
            return True
        else:
            next_time = self.prev_time + self.get_recharge
            if now >= next_time:
                return True
            else:
                return False


class Solder(Unit):
    __experience = 0

    def __init__(self):
        self.set_health(100)
        self.set_recharge(random.randint(100, 2000) / 10000)

    @property
    def get_experience(self):
        """Represents the experience of the solder.
        """
        return self.__experience

    def set_experience(self):
        """We set the experience of the solder.

         The experience property is incremented after each successful attack,
         and is sed to calculate the attack success probability and the
         amount of damage inflicted.
        """
        if self.__experience < 50:
            self.__experience += 1

    @property
    def do_attack(self):
        """Soldier attack

        Soldiers attack success probability is calculated:

        0.5 * (1 + health/100) * random(50 + experience, 100) / 100

        where random(min, max) returns a random number between
        min and max (inclusive).

        Returns:
            The value of soldier attack.
        """
        if self.get_health > 0 and self.check_attack():
            soldiers_attack = 0.5 * (1 + self.get_health) * \
                random.randint(50 + self.__experience, 100) / 100
            self.set_experience()
            self.prev_time = time.time() * 1000
            return soldiers_attack
        else:
            return 0

    def take_damage(self, damage):
        """The amount of damage.

        The amount of damage a soldier can afflict is calculated as follows:

        0.05 + experience / 100

        Args:
            damage:
        """
        attack = damage - (0.05 + self.__experience / 1000)
        self.set_health(self.get_health - attack)


class Vehicles(Unit):
    operators = []

    def __init__(self):
        self.set_recharge(random.randint(1000, 2000) / 10000)
        operator_count = random.randint(1, 3)
        self.operators = [Solder() for _ in range(0, operator_count)]
        list_operators = [i.get_health for i in self.operators]
        self.set_health(sum(list_operators) / len(list_operators))

    def get_operators(self):
        """The operators of the vehicle.

        Returns:
            A list of operators. For example:

            [<Battle.Units.Solder object at 0x7fa64372b588>,
            <Battle.Units.Solder object at 0x7fa64372b5f8>]
        """
        return self.operators

    @property
    def get_experience(self):
        """The experience of the vehicle.

        Returns:
           The sum of all experiences of soldiers.
        """
        return sum([i.get_experience for i in self.operators])

    @staticmethod
    def alive(units):
        """Survivors in the vehicle.

        Args:
            units: operators in the vehicle.

        Returns:
            If there are survivors, return True, else - return False.
        """
        res = False
        for i in units:
            if i.get_health > 0:
                res = True
                break
        return res

    @property
    def do_attack(self):
        """The Vehicle attack.

        The Vehicle attack success probability is determined as follows:

        0.5 * (1 + vehicle.health / 100) * gavg(operators.attack_success)

        where gavg is the geometric average of the attack success of all
        the vehicle operators.

        Returns:
            Total value of the vehicle attack.
        """
        if self.get_health > 0 and self.check_attack() \
                and self.alive(self.operators):
            list_attack_soldiers = [i.do_attack for i in
                                    self.operators]
            vehicles_attack = 0.5 * (1 + self.get_health / 100) * (
                sum(list_attack_soldiers) / len(list_attack_soldiers))
            self.prev_time = time.time() * 1000
            return vehicles_attack
        else:
            return 0

    def take_damage(self, damage):
        """The damage of the vehicle.

        The damage afflicted by a vehicle is calculated:

        0.1 + sum(operators.experience / 100)

        The total damage inflicted on the vehicle is distributed to the
        operators as follows: 60% of the total damage is inflicted on the
        vehicle 20% of the total damage is inflicted on a random vehicle
        operator. The rest of the damage is inflicted evenly to the other
        operators (10% each).

        Args:
            damage: the value of damage, that caused this vehicle.
        """
        list_operators_experience = [i.get_experience / 1000 for i in
                                     self.operators]
        damage -= 0.1 + sum(list_operators_experience)
        # 60% урона на машину
        self.set_health(self.get_health - damage * 0.6)
        # случайный оператор, который получит 20% урона
        random_operator = random.randint(0, len(self.operators) - 1)
        j = 0
        while j < len(self.operators):
            if j == random_operator:
                self.operators[j].take_damage(damage * 0.2)
            else:
                self.operators[j].take_damage(damage * 0.1)
            j += 1
