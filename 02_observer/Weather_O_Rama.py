class Subject:
    def register_observer(self, observer):
        raise NotImplementedError
    
    def remove_observer(self, observer):
        raise NotImplementedError
    
    def notify_observers(self):
        raise NotImplementedError
    
class Observer:
    def update(self, temp, humidity, pressure):
        raise NotImplementedError
    
class WeatherData(Subject):
    def __init__(self):
        self._temperature = None
        self._humidity = None
        self._pressure = None
        self._observers = []

    def register_observer(self, observer: Observer):
        self._observers.append(observer)

    def remove_observer(self, observer: Observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature, self._humidity, self._pressure)

    def set_measurements(self, temperature: float, humidity: float, pressure: float):
        self._temperature = temperature
        self._humidity = humidity
        self._pressure = pressure
        self.notify_observers()

class CurrentConditionsDisplay(DisplayElement, Observer):
    def __init__(self, weather_data):
        self._temperature = None
        self._humidity = None
        self._weather_data = weather_data
        weather_data.register_observer(self)

    def display(self):
        print(
            f"Current conditions: "
            f"{self._temperature:.1f}F degrees and "
            f"{self._humidity:.1f}% humidity"
        )

    def update(self, temp: float, humidity: float, pressure: float):
        self._temperature = temp
        self._humidity = humidity
        self.display()