"""
L - The Liskov Substitution Principle
Объекты базового класса могут быть заменены объ ектами его производного класса без изменения свойств программы
"""

from abc import ABC, abstractmethod

# Плохой пример
class BadBird(ABC):
  def __init__(self, name) -> None:
    self.name = name
    
  @abstractmethod
  def fly(self):
    pass
  
  @abstractmethod
  def swim(self):
    pass
  
  
class Eagle(BadBird):
  def fly(self):
    print("flying high")
    
  def swim(self):
    raise NotImplementedError("Eagle cannot swim")
      
      
# Хороший пример
class Bird(ABC):
  def __init__(self, name) -> None:
    self.name = name
    
  @abstractmethod
  def fly(self):
    pass
  
  
class SwimmingBird(Bird, ABC):
  @abstractmethod
  def swim(self):
    pass
  

class Duck(SwimmingBird):
  def fly(self):
    print("flying")
    
  def swim(self):
    print("swimming")
    
def process_bird(bird: Bird):
  bird.fly()
  
  
duck = Duck('Donald')
process_bird(duck)