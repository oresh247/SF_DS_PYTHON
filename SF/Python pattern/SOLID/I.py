"""
I - Intarface Segregation Principle
Клиенты не должны зависить от методов, которые они не используют
"""


# Плохой пример
class MultifunctionDevice:
  def print(self, document):
    print("Печать документов")
    
  def scan(self, document):
    print("Сканирование документов")
    
  def fax(self, document):
    print("Отправка факса")
    
    
    
class SimplePrinter(MultifunctionDevice):
  def scan(self, document):
    raise NotImplementedError("Этот принтер не поддерживает сканирование")
  
  def fax(self, document):
    raise NotImplementedError("Этот принтер не поддерживает отправку факса")
  
  

# Хороший пример
class Printable:
  def print(self, document):
    pass
    
    
class Scannable:
  def scan(self, document):
    pass
  

class Faxable:
  def fax(self, document):
    pass


class SimplePrinter(Printable):
  def print(self, document):
    print("Печать документов")
    

class MultifunctionPrinter(Printable, Scannable, Faxable):
  def print(self, document):
    print("Печать документов")
    
  def scan(self, document):
    print("Сканирование документов")
    
  def fax(self, document):
    print("Отправка факса")