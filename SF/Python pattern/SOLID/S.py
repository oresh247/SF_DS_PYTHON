"""
S - Single Responsibility Principle
Класс отвечает за одну область ответственности
"""
  
# Плохой пример
class GenerateAndSendReport:
  def __init__(self, report) -> None:
    self.report = report
    
  def generate_and_send(self):
    print("Generating report") 
    print("Sending report") 
    
    
# Хороший пример
class ReportGenerate:
  def __init__(self, report) -> None:
    self.report = report
    
  def generate(self):
    print("Generating report") 


class ReportSender:
  def __init__(self, report) -> None:
    self.report = report
    
  def send(self):
    print("Sending report") 
    
    
