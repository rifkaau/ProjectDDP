# vehicle.py
from abc import ABC, abstractmethod

# Class Parent untuk Item
class Item(ABC):
    def __init__(self, name, year, purchase_price):
        self.name = name
        self.year = year
        self.purchase_price = purchase_price

    @abstractmethod
    def description(self):
        pass

    def profit(self, selling_price):
        return selling_price - self.purchase_price

# Class Child untuk Kendaraan
class Vehicle(Item):
    def __init__(self, make, model, year, purchase_price):
        super().__init__(f"{make} {model}", year, purchase_price)
        self.make = make
        self.model = model
        self.selling_price = None

    def set_selling_price(self, selling_price):
        self.selling_price = selling_price

    def get_profit(self):
        if self.selling_price is not None:
            return self.profit(self.selling_price)
        return None

    def description(self):
        return f"{self.make} {self.model} ({self.year})"