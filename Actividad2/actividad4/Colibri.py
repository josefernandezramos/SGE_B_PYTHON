class Colibri:
    def __init__(self, color, tamanyo, plumaje, tipo_pico, velo_aleteo):
        #atributos
        self.color = color
        self.tamanyo = tamanyo
        self.plumaje = plumaje
        self.tipo_pico = tipo_pico
        self.velo_aleteo = velo_aleteo

    #getters/setters

    def setColor(self, new_color):
        self.color = new_color
    def getColor(self):
        return self.color
    
    def setTamanyo(self, new_tamanyo):
        self.tamanyo = new_tamanyo
    def getTamanyo(self):
        return self.tamanyo
    
    def setPlumaje(self, new_plumaje):
        self.plumaje = new_plumaje
    def getPlumaje(self):
        return self.plumaje
    
    def setTipo_pico(self, new_tipo_pico):
        self.tipo_pico = new_tipo_pico
    def getTipo_pico(self):
        return self.tipo_pico
    
    def setVelo_aleteo(self, new_velo_aleteo):
        self.velo_aleteo = new_velo_aleteo
    def getVelo_aleteo(self):
        return self.velo_aleteo