import runner_and_tournament as RT
import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}


    def setUp(self):
        self.Bolt = RT.Runner('Усэйн',10)
        self.Andrey = RT.Runner('Андрей',9)
        self.Nik = RT.Runner('Ник',3)

    @classmethod
    def tearDownClass(cls):
        print(cls.all_results)

    def test_run(self):
        Marathon = RT.Tournament(90, self.Bolt, self.Nik)
        all_results = Marathon.start()
        self.assertTrue(all_results[2] == self.Nik)


if __name__ == '__main__':
    unittest.main()


