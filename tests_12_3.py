import unittest
class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_walk(self):
        Bolt = Runner('Bolt')
        for i in range(10):
            Bolt.walk()
        self.assertEqual(Bolt.distance,50)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_run(self):
        Usain = Runner('Usain')
        for i in range(10):
            Usain.run()
        self.assertEqual(Usain.distance, 100)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        Beavis = Runner('Beavis')
        Butt_Head = Runner('Butt_Head')
        for i in range(10):
            Beavis.run()
            Butt_Head.walk()
        self.assertNotEqual(Beavis.distance, Butt_Head.distance)

if __name__ == '__main__':
    unittest.main()

import runner_and_tournament as RT
import unittest

class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.Bolt = RT.Runner('Усэйн',10)
        self.Andrey = RT.Runner('Андрей',9)
        self.Nik = RT.Runner('Ник',3)

    @classmethod
    def tearDownClass(cls):
        print(cls.all_results)

    @unittest.skipIf(is_frozen,'Тесты в этом кейсе заморожены')
    def test_run(self):
        Marathon = RT.Tournament(90, self.Bolt, self.Nik)
        all_results = Marathon.start()
        self.assertTrue(all_results[2] == self.Nik)


if __name__ == '__main__':
    unittest.main()




