from abc import ABC, abstractmethod


class RouteStrategy(ABC):
    def calculate_route(self, source, destination):
        pass

class ShortestRoute(RouteStrategy):
    def calculate_route(self, source, destination):
        print(f"Calculating shortest routes between {source} and {destination}")
        return None


class FastestRoute(RouteStrategy):
    def calculate_route(self, source, destination):
        print(f"Calculating fastest routes between {source} and {destination}")
        return None

class ScenicRoute(RouteStrategy):
    def calculate_route(self, source, destination):
        print(f"Calculating scenic routes between {source} and {destination}")
        return None

class RoutePlanner:
    def __init__(self, route_strategy: RouteStrategy):
        self.route_strategy = route_strategy

    def set_route_strategy(self, route_strategy):
        self.route_strategy = route_strategy

    def calculte_route(self, source, destination):
        return self.route_strategy.calculate_route(source, destination)


if __name__ == '__main__':
    source = "Seattle"
    destination = "Portland"
    route_planner = RoutePlanner(ShortestRoute())
    route_planner.calculte_route(source, destination)

    route_planner.set_route_strategy(FastestRoute())
    route_planner.calculte_route(source, destination)

    route_planner.set_route_strategy(ScenicRoute())
    route_planner.calculte_route(source, destination)
