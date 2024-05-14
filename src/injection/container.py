import inspect

class Dependency_Container:

  _instance=None
  _dependencies=None
  
  def __new__(cls, *args, **kwargs):
    if cls._instance is None:
      cls._instance = super().__new__(cls, *args, **kwargs)
      cls._dependencies = {}
    return cls._instance
  
  def register(self,obj):
    if self._dependencies is None: 
      self._dependencies = obj
    else:
      self._dependencies = {**self._dependencies, **obj}
  
  def resolve(self, key:str):
    if key not in self._registry:
            raise ValueError(f"{key} is not registered in the container.")
    
    target_dependency= self._dependencies[key]
    constructor_params = inspect.signature(target_dependency.__init__).parameters.values()
    dependencies = [
      self.resolve(param.annotation)
      for param in constructor_params
      if param.annotation is not inspect.Parameter.empty
    ]
    return target_dependency(*dependencies)
  
  @staticmethod
  def create_container():
    return Dependency_Container()