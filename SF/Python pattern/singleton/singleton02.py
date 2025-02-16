
class Singleton(type):
  instances = {}
  def __call__(cls, *args, **kwds):
    if cls not in cls.instances:
      cls.instances[cls] = super(Singleton, cls).__call__(*args, **kwds)
    return cls.instances[cls]
  
  
class DatabaseConnection(metaclass=Singleton):
  pass

class SingletonExample(metaclass=Singleton):
  pass


connection1 = DatabaseConnection()
connection2 = DatabaseConnection()

print(connection1 is connection2)

object1 = SingletonExample()
object2 = SingletonExample()

print(object1 is object2)