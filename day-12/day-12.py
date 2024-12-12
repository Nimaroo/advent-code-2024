from base_class import BaseClass
import numpy as np


class Region:
    def __init__(self, letter, area, perimeter):
        self.letter = letter
        self.area = area
        self.perimeter = perimeter
        self.cost = area * perimeter


class Day12(BaseClass):
    def __init__(self, inputs):
        super().__init__(inputs)
        self.rows, self.columns = self.inputs.shape
        self.regions = []

    def parse_inputs(self, inputs):
        with open(inputs, "r") as f:
            field = np.array([list(line.strip()) for line in f])
        return field

    def find_all_neighbours(self, letter, seed, visited):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        area = 0
        perimeter = 0
        while seed:
            i, j = seed.pop()
            if (0 <= i < self.rows) and (0 <= j < self.columns) and self.inputs[i, j] == letter:
                if not visited[i, j]:
                    area += 1
                    visited[i, j] = True
                    for x, y in directions:
                        seed.append((i + x, j + y))
            else:
                perimeter += 1
        return Region(letter, area, perimeter)

    def find_regions(self):
        visited = np.full((self.rows, self.columns), False)
        for i in range(self.rows):
            for j in range(self.columns):
                letter = self.inputs[i, j]
                if not visited[i, j]:
                    self.regions.append(self.find_all_neighbours(letter, [(i, j)], visited))

    def calculate_final_cost(self):
        cost = 0
        for region in self.regions:
            cost += region.cost
        return cost

    def part1(self):
        # Calculamos todas las regiones. Usamos DFS
        self.find_regions()

        # Y ahora el coste total de todas las regiones
        return self.calculate_final_cost()

    def part2(self):
        pass


if __name__ == '__main__':
    my_inputs = 'field.txt'
    my_class = Day12(my_inputs)
    print(f'El coste final para vallar el campo es de: {my_class.part1()}€')
