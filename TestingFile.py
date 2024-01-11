import unittest
from collections import defaultdict
from task1 import one
from task2 import two

class TestCountLogsFromFile(unittest.TestCase):
    def test_one(self):

        test_filename = "logTest"
        log_count = defaultdict(int)
        one(log_count, test_filename)

        expected_results = {
            ('[DEBUG]', 'BackendApp'): 5,
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
        self.assertEqual(log_count, expected_results)

    def test_two(self):
        test_filename = 'logTest'

        total_run_time = {'BackendApp': 0, 'FrontendApp': 0, 'API': 0}
        successful_run_count = {'BackendApp': 0, 'FrontendApp': 0, 'API': 0}
        average_run_time_per_app = two(test_filename, total_run_time, successful_run_count)

        expected_average_run_time = {'API': 17.0, 'BackendApp': 17.0, 'FrontendApp': 23.666666666666668}
        self.assertEqual(average_run_time_per_app, expected_average_run_time)


if __name__ == '__main__':
    unittest.main()
