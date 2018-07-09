from .scripts.multiply import Multiplier

import fire


class ComputeStuff(object):
    version = 0.1

    def add_stuff(self, first_number, second_number):
        return float(first_number) + float(second_number)

    def substract_stuff(self, first_number, second_number):
        return float(first_number) - float(second_number)

    def multiply_stuff(self, first_number, second_number):
        m = Multiplier(first_number, second_number)
        return m.multiply()


def main():
    fire.Fire(ComputeStuff)
