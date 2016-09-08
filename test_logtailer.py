import unittest
import logtailer


class TestConstructor(unittest.TestCase):

    def setUp(self):
        self.matches = []
        self.tail = logtailer.Tail("test_file.txt", [])

    def dummy_callback_function(self, index, matched_pattern):
        self.matches.append({index, matched_pattern})

    def test_initiate(self):
        pattern = ['.*', 'Error']
        log_tail = logtailer.Tail("sample_file.txt", pattern)
        self.assertEqual("sample_file.txt", log_tail.file_name)
        self.assertListEqual(pattern, log_tail.pattern_list)

    def test_initialize(self):
        pattern = ['.*', 'Error']
        log_tail = logtailer.Tail()
        self.assertEqual("", log_tail.file_name)
        self.assertListEqual(['.*'], log_tail.pattern_list)

        # Initialize class
        log_tail.initialize("sample_file.txt", pattern)
        self.assertEqual("sample_file.txt", log_tail.file_name)
        self.assertListEqual(pattern, log_tail.pattern_list)

    def test_start_empty_file_name(self):
        log_tail = logtailer.Tail()
        self.assertFalse(log_tail.start(self.dummy_callback_function))

    def test_add_pattern(self):
        log_tail = logtailer.Tail("test_file.txt", [])
        log_tail.add_pattern('.*')
        self.assertListEqual(['.*'], log_tail.pattern_list)

        log_tail.add_pattern('Error')
        self.assertListEqual(['.*', 'Error'], log_tail.pattern_list)

    def test_remove_pattern(self):
        pattern = ['.*', 'Error']
        log_tail = logtailer.Tail("test_file.txt", pattern)
        self.assertTrue(log_tail.remove_pattern(1))
        self.assertListEqual(['.*'], log_tail.pattern_list)

        # Remove out of range element
        self.assertFalse(log_tail.remove_pattern(10))
        self.assertFalse(log_tail.remove_pattern(-10))

if __name__ == '__main__':
    unittest.main()
