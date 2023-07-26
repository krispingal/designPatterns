class Omelette:
    """Omelette object; Add your choice of cheese, fillings, herbs."""
    def __init__(self):
        self.cheese: str = ""
        self.fillings: list = []
        self.herbs: list = []
    
    def setCheese(self, cheese: str):
        self.cheese = cheese
    
    def setFillings(self, fillings: list):
        self.fillings = fillings
    
    def setHerbs(self, herbs: list):
        self.herbs = herbs

    def print(self):
        print(f'Omelette has cheese: {self.cheese}, fillings: {",".join(self.fillings)}, and the following herbs: {",".join(self.herbs)}')


class OmeletteBuilder:
    """Build any valid omelette, that is custom to your wants."""
    def __init__(self):
        self.omelette = Omelette()

    def addCheese(self, cheese: str):
        self.omelette.setCheese(cheese)
        return self
    
    def addFillings(self, fillings: list):
        self.omelette.setFillings(fillings)
        return self
    
    def addHerbs(self, herbs: list):
        self.omelette.setHerbs(herbs)
        return self
    
    def build(self):
        return self.omelette
    

if __name__ == '__main__':
    customOmelette = OmeletteBuilder() \
        .addCheese('Feta') \
        .addFillings(['Mushroom', 'Spinach']) \
        .build()
    customOmelette.print()
    