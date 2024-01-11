import unittest
from collections import defaultdict
from task1 import one
from task2 import two
from task8 import eight
from service import three, four, six
from main import read_logs


class TestCountLogsFromFile(unittest.TestCase):
    def test_one(self):
        expected_results = {('[DEBUG]', 'BackendApp'): 5,
                            ('[DEBUG]', 'FrontendApp'): 1,
                            ('[DEBUG]', 'SYSTEM'): 1,
                            ('[ERROR]', 'API'): 2,
                            ('[ERROR]', 'FrontendApp'): 3,
                            ('[ERROR]', 'SYSTEM'): 2,
                            ('[INFO]', 'API'): 2,
                            ('[INFO]', 'BackendApp'): 1,
                            ('[INFO]', 'FrontendApp'): 3,
                            ('[INFO]', 'SYSTEM'): 1
                            }
        self.assertEqual(one("logTest"), expected_results)

    def test_two(self):

        expected_average_run_time = {'API': 17.0, 'BackendApp': 17.0, 'FrontendApp': 23.666666666666668}
        self.assertEqual(two("logTest"), expected_average_run_time)

    def test_three(self):
        expected_results = {'API': 2, 'BackendApp': 0, 'FrontendApp': 3, 'SYSTEM': 2}
        log_dict = read_logs("logTest")
        self.assertEqual(three(log_dict), expected_results)

    def test_four(self):
        expected_results = ('FrontendApp', 3)
        log_dict = read_logs("logTest")
        self.assertEqual(four(log_dict), expected_results)

    def test_six(self):
        expected_results = {1: 2, 2: 3, 3: 2}
        log_dict = read_logs("logTest")
        self.assertEqual(six(log_dict), expected_results)

    def test_eight(self):
        expected_results = {'API': {'DEBUG': {'count': 0, 'hour': None},
                                    'ERROR': {'count': 2, 'hour': 9},
                                    'INFO': {'count': 2, 'hour': 5}},
                            'BackendApp': {'DEBUG': {'count': 1, 'hour': 16},
                                           'ERROR': {'count': 0, 'hour': None},
                                           'INFO': {'count': 2, 'hour': 22}},
                            'FrontendApp': {'DEBUG': {'count': 1, 'hour': 8},
                                            'ERROR': {'count': 1, 'hour': 3},
                                            'INFO': {'count': 2, 'hour': 17}}}
        self.assertEqual(eight("logTest"), expected_results)


if __name__ == '__main__':
    unittest.main()
