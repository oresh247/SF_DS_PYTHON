from abc import ABC, abstractmethod

class AbstractSMSProvider(ABC):
  
  @abstractmethod
  def send(self, message: str, to: str) -> tuple[bool, str]:
    pass
  

class AeroSMSProvider(AbstractSMSProvider):
  
  def send(self, message: str, to: str) -> tuple[bool, str]:
    pass
  
  
sms = AeroSMSProvider()

def send_sms(provider: AbstractSMSProvider):
  provider.send(message='hello', to='12421341324')