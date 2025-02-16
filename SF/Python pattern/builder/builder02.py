from abc import ABC, abstractmethod
from enum import Enum, auto
from collections import namedtuple

# Объявляем именнованный кортедж для свойств основы пиццы
PizzaBase = namedtuple('PizzaBase', ['DoughDepth', 'DoughType'])

class PizzaDoughDepth(Enum):
  THIN = auto()
  THICK = auto()
  
  
class PizzaDoughType(Enum):
  WHEAT = auto()
  CORN = auto()
  RYE = auto()
  
  
class PizzaSouceType(Enum):
  PESTO = auto()
  WHITE_GARLIC = auto()
  BARBEQUE = auto()
  TOMATO = auto()


class PizzaTopLevelType(Enum):
  MAZZARELLA = auto()
  SALAMI = auto()
  BACON = auto()
  MUSHROOMS = auto()
  SHRIMPS = auto()


class Pizza:
  def __init__(self, name):
    self.name = name
    self.dough = None
    self.souce = None
    self.topping = []
    self.cooking_time = None
    
  def __str__(self):
    info: str = f"Pizza name: {self.name} \n" \
                f"Pizza dough: {self.dough} \n" \
                f"Pizza souce: {self.souce} \n" \
                f"Pizza topping: {[it.name for it in self.topping]} \n" \
                f"Pizza cooking time: {self.cooking_time} minutes" 
    return info
  
  
class Builder(ABC):
  
  @abstractmethod
  def prepare_dough(self) -> None: pass
  
  @abstractmethod
  def add_souce(self) -> None: pass
  
  @abstractmethod
  def add_topping(self) -> None: pass
  
  @abstractmethod
  def get_pizza(self) -> Pizza: pass
  
  
class MargaritaPizzaBuilder(Builder):
  def __init__(self) -> None:
    self.pizza = Pizza("Margarita")
    self.pizza.cooking_time = 15
    
  def prepare_dough(self) -> None:
    self.pizza.dough = PizzaBase(PizzaDoughDepth.THICK, PizzaDoughType.WHEAT)
  
  
  def add_souce(self) -> None:
    self.pizza.souce = PizzaSouceType.TOMATO
  
  
  def add_topping(self) -> None:
    self.pizza.topping.extend(
      [
        it for it in (PizzaTopLevelType.MAZZARELLA,
                      PizzaTopLevelType.MAZZARELLA,
                      PizzaTopLevelType.BACON,
                      )
      ]
    )
  def get_pizza(self) -> Pizza:
    return self.pizza
  
  
class SalamiPizzaBuilder(Builder):
  def __init__(self) -> None:
    self.pizza = Pizza("Salami")
    self.pizza.cooking_time = 10
    
  def prepare_dough(self) -> None:
    self.pizza.dough = PizzaBase(PizzaDoughDepth.THIN, PizzaDoughType.RYE)
  
  
  def add_souce(self) -> None:
    self.pizza.souce = PizzaSouceType.BARBEQUE
  
  
  def add_topping(self) -> None:
    self.pizza.topping.extend(
      [
        it for it in (PizzaTopLevelType.MAZZARELLA,
                      PizzaTopLevelType.SALAMI,
                      )
      ]
    )
  def get_pizza(self) -> Pizza:
    return self.pizza


class Director:
  def __init__(self) -> None:
    self.builder = None 
    
  def set_builder(self, builder: Builder):
    self.builder = builder
    
  def make_pizza(self):
    if not self.builder:
      raise ValueError("Builder didn`t set")
    
    self.builder.prepare_dough() 
    self.builder.add_souce()
    self.builder.add_topping()

if __name__ == '__main__':
  director = Director()
  for it in (MargaritaPizzaBuilder, SalamiPizzaBuilder):
    builder = it()
    director.set_builder(builder)
    director.make_pizza()
    pizza = builder.get_pizza()
    print(pizza)
    print('---------------------------------')