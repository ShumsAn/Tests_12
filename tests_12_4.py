import logging
import unittest

logging.basicConfig(filename='runner_tests.log', filemode='w', level=logging.INFO, encoding='UTF-8',
                    format = "%(asctime)s - %(module)s - %(levelname)s  %(funcName)s: - %(lineno)d - %(message)s")
class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class RunnerTest(unittest.TestCase):
    is_frozen = False

    def test_walk(self):
        try:
            Bolt = Runner('Bolt',speed=-50)
            logging.info('test_walk" выполнен успешно')
            for i in range(10):
                Bolt.walk()
            self.assertEqual(Bolt.distance,50)
        except ValueError:
            logging.warning(f"Неверная скорость для Runner")

    def test_run(self):
        try:
            Usain = Runner(777)
            logging.info('"test_run" выполнен успешно')
            for i in range(10):
                Usain.run()
            self.assertEqual(Usain.distance, 100)
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner")


if __name__ == '__main__':
    first = Runner('Вося', -10)
    second = Runner(777, 5)
    # third = Runner('Арсен', 10)

    t = Tournament(101, first, second)
    # print(t.start())