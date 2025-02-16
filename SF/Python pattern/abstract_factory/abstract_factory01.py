from abc import ABCMeta, abstractmethod

class IEngine(metaclass=ABCMeta):
  @abstractmethod
  def realese_engine(self):
    pass
  

class JapaneseEngine(IEngine):
  def realese_engine(self):
    print('японский двигатель')
    
    
class RussianEngine(IEngine):
  def realese_engine(self):
    print('российский двигатель')
    
    
class ICar(metaclass=ABCMeta):
  @abstractmethod
  def release_car(self, engine: IEngine):
    pass
  

class JapaneseCar(ICar):
  def release_car(self, engine: IEngine):
    print('Собрали японский автомобиль, ', end ='')
    engine.realese_engine()
    
    
class RussianCar(ICar):
  def release_car(self, engine: IEngine):
    print('Собрали российский автомобиль, ', end ='')
    engine.realese_engine()
    

class IFactory(metaclass=ABCMeta):
  @abstractmethod
  def create_engine(self) -> IEngine:
    pass
  
  @abstractmethod
  def create_car(self) -> ICar:
    pass
  
  
class JapaneseFactory(IFactory):
  def create_engine(self) -> IEngine:
    return JapaneseEngine()
  
  def create_car(self) -> ICar:
    return JapaneseCar()
    
    
class RussianFactory(IFactory):
  def create_engine(self) -> IEngine:
    return RussianEngine()
  
  def create_car(self) -> ICar:
    return RussianCar()
  
  
if __name__ == '__main__':
  j_factiry = JapaneseFactory()
  j_engine = j_factiry.create_engine()
  j_car = j_factiry.create_car()
  
  j_car.release_car(j_engine)
  
  r_factiry = RussianFactory()
  r_engine = r_factiry.create_engine()
  r_car = r_factiry.create_car()
  
  r_car.release_car(r_engine)
  
  r_car.release_car(j_engine)
  