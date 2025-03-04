from abc import ABCMeta

class Phone:
  def __init__(self):
    self.data: str = ''
    
  def about_phone(self) -> str:
    return self.data
  
  def append_data(self, string: str):
    self.data += string
    
    
class IDeveloper(metaclass=ABCMeta):
  def create_display(self):
    pass
  
  def create_box(self):
    pass
  
  def system_install(self):
    pass
  
  def get_phone(self) -> Phone:
    pass
  
  
class AndroidDeveloper(IDeveloper):
  
  def __init__(self):
    self.__phone = Phone()
    
  def create_display(self):
    self.__phone.append_data("Произведен дисплей Самсунг; ")

  def create_box(self):
    self.__phone.append_data("Произведен корпус Самсунг; ")
  
  def system_install(self):
    self.__phone.append_data("Установлена система андройд; ")
  
  def get_phone(self) -> Phone:
    return self.__phone
    
    
    
class IphoneDeveloper(IDeveloper):
    
    def __init__(self):
      self.__phone = Phone()
      
    def create_display(self):
      self.__phone.append_data("Произведен дисплей Айфон; ")
  
    def create_box(self):
      self.__phone.append_data("Произведен корпус Айфон; ")
    
    def system_install(self):
      self.__phone.append_data("Установлена система IOS; ")
    
    def get_phone(self) -> Phone:
      return self.__phone
    
class Director:
  def __init__(self, developer: IDeveloper):
    self.__developer = developer
    
  def set_developer(self, developer: IDeveloper):
    self.__developer = developer
    
  def mount_only_phone(self) -> Phone:
    self.__developer.create_box()
    self.__developer.create_display()
    return self.__developer.get_phone()
  
  def mount_full_phone(self) -> Phone:
    self.__developer.create_box()
    self.__developer.create_display()
    self.__developer.system_install()
    return self.__developer.get_phone()
  
  
if __name__ == '__main__':
  android_developer: IDeveloper = AndroidDeveloper()
  director = Director(android_developer)
  sumsung: Phone = director.mount_full_phone()
  print(sumsung.about_phone())
  
  iphone_developer: IDeveloper = IphoneDeveloper()
  director = Director(iphone_developer)
  iphone: Phone = director.mount_only_phone()
  print(iphone.about_phone())