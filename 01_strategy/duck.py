class FlyBehaviour:
    """
    FlyBehaviour is an interface that all flying classes implement. All new flying classes just need to implement the fly() method.
    """
    def fly(self):
        raise NotImplementedError


# Implementations of FlyBehaviour
class FlyWithWings(FlyBehaviour):
    def fly(self):
        print("Flying with wings")

class FlyNoWay(FlyBehaviour):
    def fly(self):
        print("Unable to fly")

class FlyRocketPowered(FlyBehaviour):
    def fly(self):
        print("Flying with rocket!")


class QuackBehaviour:
    """
    QuackBehaviour is an interface that all quacking classes implement. All new quacking classes just need to implement the quack() method.
    """
    def quack(self):
        raise NotImplementedError


# Implementations of QuackBehaviour
class Quack(QuackBehaviour):
    def quack(self):
        print("Quack")

class Squeak(QuackBehaviour):
    def quack(self):
        print("Squeak")
    
class MuteQuack(QuackBehaviour):
    def quack(self):
        print("<< silence >>")


class Duck:
    _fly_behaviour = None
    _quack_behaviour = None

    def set_fly_behaviour(self, fly_behaviour):
        self._fly_behaviour = fly_behaviour

    def set_quack_behaviour(self, quack_behaviour):
        self._quack_behaviour = quack_behaviour

    def display(self):
        raise NotImplementedError
    
    def perform_fly(self):
        self._fly_behaviour.fly()
    
    def perform_quack(self):
        self._quack_behaviour.quack()

    def swim(self):
        raise NotImplementedError


# Implementations of Duck
class MallardDuck(Duck):
    _fly_behaviour = FlyWithWings()
    _quack_behaviour = Quack()

    def display(self):
        print("Mallard Duck")

class RubberDuck(Duck):
    _fly_behaviour = FlyNoWay()
    _quack_behaviour = Squeak()

    def display(self):
        print("Rubber Duck")

class ModelDuck(Duck):
    _fly_behaviour = FlyRocketPowered()
    _quack_behaviour = MuteQuack()

    def display(self):
        print("Model Duck")


if __name__ == "__main__":
    # Instantiate ducks
    mallard = MallardDuck()
    rubber = RubberDuck()
    model = ModelDuck()

    # Perform Behaviours
    mallard.perform_fly()
    mallard.perform_quack()

    rubber.perform_quack()
    rubber.set_quack_behaviour(Quack())
    rubber.perform_quack()
    
    model.perform_fly()
    model.set_fly_behaviour(FlyNoWay())
    model.perform_fly()

