class Singleton(object):
  __instance = None
  
  def __new__(cls, *args, **kwds):
    if cls.__instance is None:
      cls.__instance = super(Singleton, cls).__new__(cls, *args, **kwds)
    return cls.__instance
    
    
singleton = Singleton()
singleton_two = Singleton()

print(singleton is singleton_two)