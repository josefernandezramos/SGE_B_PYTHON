class Cotxe:
    def __init__(self, modelo, color, motor, n_puertas, anyo):
        #atributos
        self.modelo = modelo
        self.color = color
        self.motor = motor
        self.n_puertas = n_puertas
        self.anyo = anyo

    #setters/getters
    def setModelo(self, new_modelo):
        self.modelo = new_modelo
    def getModelo(self):
        return self.modelo
    
    def setColor(self, new_color):
        self.color = new_color
    def getColor(self):
        return self.color
    
    def setMotor(self, new_motor):
        self.motor = new_motor
    def getMotor(self):
        return self.motor
    
    def setN_puertas(self, new_n_puertas):
        self.n_puertas = new_n_puertas
    def getN_puertas(self):
        return self.n_puertas
    
    def setAnyo(self, new_anyo):
        self.anyo = new_anyo
    def getAnyo(self):
        return self.anyo