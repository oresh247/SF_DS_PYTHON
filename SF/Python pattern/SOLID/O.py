"""
O - Open-Closed Principle
Классы должны быть открыты для расширения и закрыты для модификации
"""

import math
from abc import ABC

# Плохой пример
class BadShape(ABC):
  def __init__(self, name, radius=None, side=None) -> None:
    self.name = name
    self.radius = radius
    self.side = side
    
  def area(self):
    if self.name == 'circle':
      return self.raius ** 2 * math.pi
    elif self.name == 'square':
      return self.side ** 2

      
# Хороший пример
class Shape(ABC):
  def area(self):
    pass
  
class Circle(Shape):
  def __init__(self, radius=None) -> None:
    self.radius = radius
    
  def area(self):
    return self.raius ** 2 * math.pi

class Square(Shape):
  def __init__(self, side=None) -> None:
    self.side = side
    
  def area(self):
    return self.side ** 2