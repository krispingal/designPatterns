class Biriyani:
    """Creates a biriyani object."""
    def __init__(self, ingredients):
        self.ingredients = ingredients
    
    def print(self):
        print(self.ingredients)


class BiriyaniFactory:
    """Creates a biriyani from one of the preset options. 
        We can quickly create any of the following biriyanis [chicken, egg, 
        paneer, and mutton biriyani].

        NOTE: Customers cannot make modifications to any of the biryanis nor can they 
        know what spices exactly went into the making of a biryani.
   """
    
    def createChickenBiriyani(self):
        """Creates a chicken biriyani with rice, spices, and chicken."""
        ingredients = ["rice", "spices", "chicken"]
        return Biriyani(ingredients)
    
    def createEggBiriyani(self):
        """Creates a egg biriyani with rice, spices, and egg."""
        ingredients = ["rice", "spices", "egg"]
        return Biriyani(ingredients)
      
    def createPaneerBiriyani(self):
        """Creates a paneer biriyani with rice, spices, and vegetables."""
        ingredients = ["rice", "spices", "paneer"]
        return Biriyani(ingredients)
  
    def createMuttonBiriyani(self):
        """Creates a mutton biriyani with rice, spices, mutton."""
        ingredients = ["rice", "spices", "mutton"]
        return Biriyani(ingredients)


if __name__ == '__main__':
    biriyaniFactory = BiriyaniFactory()
    biriyaniFactory.createPaneerBiriyani().print()
