class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, color):
        coloresValidos = ("rojo", "verde", "amarillo", "negro", "blanco")
        for colorValido in coloresValidos:
            if(colorValido == color.lower()):
                self.color = color
                break

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.registro = registro
        self.tipo = tipo
    
    def cambiarRegistro(self, registro):
        self.registro = registro
    
    def asignarTipo(self, tipo):
        tiposValidos = ("electrico","gasolina")
        for tipoValido in tiposValidos:
            if(tipoValido == tipo.lower):
                self.tipo = tipo
                break

class Auto :
    cantidadCreados = 0
    
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro
        Auto.cantidadCreados += 1
    
    def cantidadAsientos(self):
        numeroAsientos = 0
        for asiento in self.asientos:
            if(asiento != None):
                numeroAsientos += 1
        return numeroAsientos
    
    def verificarIntegridad(self):
        mensajeErroneo = "Las piezas no son originales"
        if(self.registro != self.motor.registro):
            return mensajeErroneo
        
        for asiento in self.asientos:
            if(asiento != None and self.registro != asiento.registro):
                return mensajeErroneo
        
        return "Auto original"