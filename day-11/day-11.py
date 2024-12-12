from base_class import BaseClass


class Day11(BaseClass):
    def __init__(self, inputs):
        super().__init__(inputs)
        self.combi = {}

    def parse_inputs(self, inputs):
        return [int(x) for x in inputs.split(' ')]

    def part1(self):
        return self.count_stones(25)

    def part2(self):
        return self.count_stones(75)

    def count_stones(self, blinks):
        count = 0
        for stone in self.inputs:
            count += self.blink(stone, blinks)
        return count

    def blink(self, value, blink):
        # Se acaban los pestañeos
        if blink == 0:
            return 1

        # Devolvemos el valor del diccionario
        if value in self.combi.keys():
            if blink in self.combi[value].keys():
                return self.combi[value][blink]
        else:
            self.combi[value] = {}

        # En caso contrario, calculamos
        if value == 0:
            self.combi[value][blink] = self.blink(1, blink - 1)
        elif len(str(value)) % 2 == 0:
            half = len(str(value)) // 2
            left = int(str(value)[:half])
            right = int(str(value)[half:])
            self.combi[value][blink] = self.blink(left, blink - 1) + self.blink(right, blink - 1)
        else:
            self.combi[value][blink] = self.blink(value * 2024, blink - 1)
        return self.combi[value][blink]


if __name__ == '__main__':
    my_inputs = '7568 155731 0 972 1 6919238 80646 22'
    my_class = Day11(my_inputs)
    print(f'El total de piedras después de 25 saltos es: {my_class.part1()}')
    print(f'El total de piedras después de 75 saltos es: {my_class.part2()}')
