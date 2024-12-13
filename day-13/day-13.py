from base_class import BaseClass
import re
from sympy import symbols, Eq, solve


class Machine:
    def __init__(self, a, b, prize):
        self.a = a
        self.b = b
        self.prize = prize


class Day13(BaseClass):
    def __init__(self, inputs):
        super().__init__(inputs)
        self.a_cost = 3
        self.b_cost = 1

    def parse_inputs(self, inputs):
        button_pattern = r"Button (A|B): X\+(\d+), Y\+(\d+)"
        prize_pattern = r"Prize: X=(\d+), Y=(\d+)"
        with open(inputs, "r") as file:
            content = file.read()
        blocks = content.strip().split("\n\n")

        machines = []
        for block in blocks:
            a = None
            b = None
            prize = None

            for button_match in re.finditer(button_pattern, block):
                button, x, y = button_match.groups()
                coords = [int(x), int(y)]
                if button == "A":
                    a = coords
                elif button == "B":
                    b = coords

            prize_match = re.search(prize_pattern, block)
            if prize_match:
                prize = list(map(int, prize_match.groups()))

            if a and b and prize:
                machines.append(Machine(a, b, prize))
        return machines

    def calculate_prize_cost(self, prize_adjust, max_movements):
        total_cost = 0
        x, y = symbols('x y')
        for idx, machine in enumerate(self.inputs):
            # Lo primero es calcular el minimo número de movimientos
            ec1 = Eq(machine.a[0] * x + machine.b[0] * y, machine.prize[0] + prize_adjust)
            ec2 = Eq(machine.a[1] * x + machine.b[1] * y, machine.prize[1] + prize_adjust)
            solution = solve((ec1, ec2), (x, y))
            movements_a = solution[x]
            movements_b = solution[y]
            condition_a = movements_a.is_integer and movements_a <= max_movements
            condition_b = movements_b.is_integer and movements_b <= max_movements
            if condition_a and condition_b:
                # Si se cumplen todas las condiciones, sumamos
                total_cost += movements_a * self.a_cost + movements_b * self.b_cost
        return total_cost

    def part1(self):
        return self.calculate_prize_cost(0, 100)

    def part2(self):
        return self.calculate_prize_cost(10000000000000, float('inf'))


if __name__ == '__main__':
    my_inputs = 'machines.txt'
    my_class = Day13(my_inputs)
    print(f'El coste total para conseguir todos los premios de la parte 1 es de {my_class.part1()} tokens')
    print(f'El coste total para conseguir todos los premios de la parte 2 es de {my_class.part2()} tokens')
