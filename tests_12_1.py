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
    def test_walk(self):
        Bolt = Runner('Bolt')
        for i in range(10):
            Bolt.walk()
        self.assertEqual(Bolt.distance,50)

    def test_run(self):
        Usain = Runner('Usain')
        for i in range(10):
            Usain.run()
        self.assertEqual(Usain.distance, 100)

    def test_challenge(self):
        Beavis = Runner('Beavis')
        Butt_Head = Runner('Butt_Head')
        for i in range(10):
            Beavis.run()
            Butt_Head.walk()
        self.assertNotEqual(Beavis.distance, Butt_Head.distance)

if __name__ == '__main__':
    unittest.main()