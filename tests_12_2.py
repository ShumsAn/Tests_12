import runner_and_tournament as RT
import unittest

class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for place,name in cls.all_results.items():
            print(place,name)

    def setUp(self):
        self.Bolt = RT.Runner('Усэйн',10)
        self.Andrey = RT.Runner('Андрей',9)
        self.Nik = RT.Runner('Ник',3)


    def test_run(self):
        Marathon = RT.Tournament(90, self.Bolt, self.Nik)
        TournamentTest.all_results = Marathon.start()
        self.assertTrue(TournamentTest.all_results[2] == self.Nik)


if __name__ == '__main__':
    unittest.main()
