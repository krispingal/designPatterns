class BasicSandwich:
    def __init__(self, bread_type = "White bread"):
        self._bread_type = bread_type

    def get_cost(self) -> float:
        cost = 5.00
        if self._bread_type == "Wheat bread":
            cost += 1.00
        elif self._bread_type == "Rye bread":
            cost += 1.25
        return cost

    def get_description(self):
        return f"Basic sandwich with {self._bread_type}"

class IngredientDecorator:
    def __init__(self, sandwich: BasicSandwich):
        self._sandwich = sandwich
class BaconDecorator(IngredientDecorator):
    def get_description(self):
        return self._sandwich.get_description() + ', Bacon'

    def get_cost(self):
        return self._sandwich.get_cost() + 1.50

class LettuceDecorator(IngredientDecorator):
    def get_description(self):
        return self._sandwich.get_description() + ', Lettuce'

    def get_cost(self):
        return self._sandwich.get_cost() + 0.50

class CheeseDecorator(IngredientDecorator):
    def get_description(self):
        return self._sandwich.get_description() + ', Cheese'

    def get_cost(self):
        return self._sandwich.get_cost() + 1.00

class TomatoDecorator(IngredientDecorator):
    def get_description(self):
        return self._sandwich.get_description() + ', Tomato'

    def get_cost(self):
        return self._sandwich.get_cost() + 0.75

def build_sandwich(bread_type, ingredients):
    sandwich = BasicSandwich(bread_type)
    decoratorMap = {"Bacon": BaconDecorator, "Lettuce": LettuceDecorator, "Tomato": TomatoDecorator, "Cheese": CheeseDecorator}
    for i in ingredients:
        sandwich = decoratorMap[i](sandwich)
    return sandwich

if __name__ == '__main__':
    sandwich = build_sandwich("White bread", ["Cheese", "Lettuce", "Tomato"])
    print(sandwich.get_description())
    print(sandwich.get_cost())

    sandwich = build_sandwich("Wheat bread", ["Bacon", "Lettuce", "Tomato"])
    print(sandwich.get_description())
    print(sandwich.get_cost())





