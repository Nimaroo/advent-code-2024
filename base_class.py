from abc import ABC, abstractmethod


class BaseClass(ABC):
    def __init__(self, inputs):
        self.inputs = self.parse_inputs(inputs)

    @abstractmethod
    def parse_inputs(self, inputs):
        pass

    @abstractmethod
    def part1(self):
        pass

    @abstractmethod
    def part2(self):
        pass

