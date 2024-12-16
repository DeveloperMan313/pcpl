import unittest
import main


class TestTaskFunctions(unittest.TestCase):

    def test_task1(self):
        in_data = (
            ('128', 'Windows 8.1', 2.7),
            ('128', 'Windows 11', 3.4),
            ('212A', 'Windows 10', 3.4),
            ('212A', 'Debian', 2.2),
            ('301', 'Linux Mint', 2.2),
            ('301', 'Windows 7', 1.8),
            ('301', 'Windows XP', 1.8),
        )
        correct_out = [
            (('Windows 11', 3.4), '128'),
            (('Windows 10', 3.4), '212A'),
            (('Windows 8.1', 2.7), '128'),
            (('Debian', 2.2), '212A'),
            (('Linux Mint', 2.2), '301'),
            (('Windows 7', 1.8), '301'),
            (('Windows XP', 1.8), '301'),
        ]
        out = main.task1(in_data)
        self.assertEqual(out, correct_out)

    def test_task2(self):
        in_data = (
            ('128', 'Windows 8.1', 2.7),
            ('128', 'Windows 11', 3.4),
            ('212A', 'Windows 10', 3.4),
            ('212A', 'Debian', 2.2),
            ('301', 'Linux Mint', 2.2),
            ('301', 'Windows 7', 1.8),
            ('301', 'Windows XP', 1.8),
        )
        correct_out = [('128', 2), ('212A', 2), ('301', 3)]
        out = main.task2(in_data)
        self.assertEqual(out, correct_out)

    def test_task3(self):
        in_data = (
            ('128', 'Windows 8.1', 2.7),
            ('212A', 'Windows 8.1', 2.7),
            ('212A', 'Windows 11', 3.4),
            ('212A', 'Windows 10', 3.4),
            ('128', 'Debian', 2.2),
            ('301', 'Linux Mint', 2.2),
            ('301', 'Linux Mint', 2.2),
            ('128', 'Windows 7', 1.8),
            ('301', 'Windows 7', 1.8),
            ('301', 'Windows XP', 1.8),
        )
        correct_out = [
            (('Windows 8.1', 2.7), '128'),
            (('Windows 8.1', 2.7), '212A'),
            (('Windows 11', 3.4), '212A'),
            (('Windows 10', 3.4), '212A'),
            (('Windows 7', 1.8), '128'),
            (('Windows 7', 1.8), '301'),
            (('Windows XP', 1.8), '301'),
        ]
        out = main.task3(in_data)
        self.assertEqual(out, correct_out)


if __name__ == '__main__':
    unittest.main()
