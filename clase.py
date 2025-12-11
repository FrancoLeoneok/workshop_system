import funtion 
import datetime

class Dispositivo:
  def __init__(self, tipo: str, marca, modelo):
    self.tipo = tipo
    self.marca = marca
    self.modelo = modelo


  def __str__(self):
    return f"Dispositivo(tipo={self.tipo)"

