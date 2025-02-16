import abc

class AbstractCar(abc.ABC):
  number: str
  
  def __init__(self,number: str) -> None:
    self.number = number
  
  @abc.abstractmethod
  def drive(self) -> None:
    pass
  
  
class BMW(AbstractCar):
  def drive(self) -> None:
    print("Driving BMW")
    
    
class Mercedes(AbstractCar):
  def drive(self) -> None:
    print("Driving Mercedes")
    
    
class CarFactory:
  def __init__(self,country: str) -> None:
    self.country = country
  
  def create(self, car_type: str, number: str) -> AbstractCar:
    car_types = {
      "BMW": BMW,
      "Mercedes": Mercedes,
    }
    
    if self.country == "Germany":
      number = f"DE-{number}"
    
    try:
        return car_types[car_type](number)
    except KeyError:
      raise ValueError(f"Unknown car type: {car_type}")

    
car_factory = CarFactory("Germany")
car = car_factory.create("BMW", "A123BC")
print(car.number)
car.drive()