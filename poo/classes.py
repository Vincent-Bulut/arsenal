""" class
 docs
 dict
 slots
 modules
 attributs
 méthodes (instance, class, static)
 """

from typing import List

class Investor:
    """ Ma documentation"""
    def __init__(self, name: str, product: str, amount: float) -> None:
        self.name = name
        self.asset = product
        self.amout = amount

    def methode_instance(self, *args: List[str], **kwargs) -> None:
        self.name = args[0]

    @classmethod
    def methode_class(cls, *args) -> None:
        cls.country = args[0]

    @staticmethod
    def methode_statique(*args) -> None:
        return "Ceci est méthode statique"


class Slot:
    """ liste des noms d'attributs que l'on souhaite permettre dans les instances
     de cette classe"""

    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Identifiant:
    def __init__(self, login: str, mdp: str) -> None:
        self.login = login
        self.mdp = mdp


class InvestisseurUnique(Investor, Identifiant):
    def __init__(self, login, mdp, name, product, amount):
        Investor.__init__(self, name, product, amount)
        Identifiant.__init__(self, login, mdp)


if __name__ == '__main__':
    investor = Investor("Vince", "ETF", 1000)
    print(investor.__doc__)
    investor.methode_instance("Turgut")
    # Une classe peut avoir ses propres arguments
    Investor.methode_class("France")
    # Pour chaque instance d'une classe __dict__ => {'attribut':'valeur'}
    print(investor.__dict__)
    print(Investor.__dict__)
    test = Slot(8, 10)
    print(test.__slots__)
    # identifie de quel module provient l'instance définie
    print(investor.__module__)
    # récupérer les annotations d'une méthode
    print(investor.methode_instance.__annotations__)
    print(Investor.methode_statique())
    iu = InvestisseurUnique(
        'v7', '****',
        'vince', 'etf', 1000
    )
    print(iu.__dict__)
