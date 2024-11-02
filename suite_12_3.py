
import unittest
import tests_12_3

runner_tour_ST = unittest.TestSuite()


runner_tour_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
runner_tour_ST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runner_tour_ST)
