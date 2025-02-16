"""
D - Dependency Inversion Principle
Модули верхнего уровня не должны зависить от модулей нижнего уровня.
"""

from abc import ABC, abstractmethod

# Плохой пример
class LightBulb:
  def turn_on(self):
    print("Лампочка включена")
    
  def turn_off(self):
    print("Лампочка выключена")
    
    
class LightSwitch:
  def __init__(self, bulb: LightBulb) -> None:
    self.bulb = bulb
    
  def operate(self):
    # Включение/Выключение лампочки
    self.bulb.turn_on()
    # Некоторая логика для выключения лампоски
    self.bulb.turn_off()


# Хороший пример
class Switchable(ABC):
  @abstractmethod
  def turn_on(self):
    pass
  
  @abstractmethod
  def turn_off(self):
    pass
  
class LightBulb(Switchable):
  def turn_on(self):
    print("Лампочка включена")
  
  def turn_off(self):
    print("Лампочка выключена")


class Conditioner(Switchable):
  def turn_on(self):
    print("Кондиционер включен")
  
  def turn_off(self):
    print("Кондиционер выключен")
    
    
class Switch(object):
  def __init__(self, device: Switchable) -> None:
    self.device = device
    
  def on(self):
    self.device.turn_on
    
  def off(self):
    self.device.turn_off