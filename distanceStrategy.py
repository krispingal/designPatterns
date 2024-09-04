"""Class that computes the distance between vectors using various distance methods"""
from abc import ABC, abstractmethod
import math

class DistanceStrategy(ABC):
    @abstractmethod
    def calculate_distance(self, a: list[float], b: list[float]) -> float:
        pass

class EuclideanDistance(DistanceStrategy):
    def calculate_distance(self, a: list[float], b: list[float]) -> float:
        return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

class ManhattanDistance(DistanceStrategy):
    def calculate_distance(self, a: list[float], b: list[float]) -> float:
        return (sum(abs(x - y) for x, y in zip(a, b)))

class VectorSpace:
    def __init__(self, distance_strategy = None):
        self._strategy = distance_strategy

    def set_strategy(self, distance_Strategy: DistanceStrategy):
        self._strategy = distance_Strategy

    def evaluate_distance(self, a: list[float], b: list[float]) -> float:
        if self._strategy:
            return self._strategy.calculate_distance(a, b)
        else:
            raise ValueError("Strategy not set!")


if __name__ == '__main__':
    vector_a = [1.0, 2.0, 3.0]
    vector_b = [4.0, 5.0, 6.0]

    space = VectorSpace()

    print(f"vector a: {vector_a} ;; vector b : {vector_b}")
    # Euclidean Distance
    space.set_strategy(EuclideanDistance())
    print(f"Euclidean Distance: {space.evaluate_distance(vector_a, vector_b):.3f}")

    # Manhattan Distance
    space.set_strategy(ManhattanDistance())
    print(f"Manhattan Distance: {space.evaluate_distance(vector_a, vector_b):.3f}")
