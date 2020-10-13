import unittest
from unittest import mock
from HW_1 import TicTacGame


class TestTicTacGame(unittest.TestCase):
    def setUp(self):
        self.ttg = TicTacGame()

    def test_first_column_win(self):
        self.ttg.cells[1] = "X"
        self.ttg.cells[2] = "X"
        self.ttg.cells[3] = "X"
        self.assertEqual('X', self.ttg.check_winner())

        self.ttg.cells[1] = "O"
        self.ttg.cells[2] = "O"
        self.ttg.cells[3] = "O"
        self.assertEqual('O', self.ttg.check_winner())

    def test_second_column_win(self):
        self.ttg.cells[4] = "X"
        self.ttg.cells[5] = "X"
        self.ttg.cells[6] = "X"
        self.assertEqual('X', self.ttg.check_winner())

        self.ttg.cells[4] = "O"
        self.ttg.cells[5] = "O"
        self.ttg.cells[6] = "O"
        self.assertEqual('O', self.ttg.check_winner())

    def test_third_column_win(self):
        self.ttg.cells[7] = "X"
        self.ttg.cells[8] = "X"
        self.ttg.cells[9] = "X"
        self.assertEqual('X', self.ttg.check_winner())

        self.ttg.cells[7] = "O"
        self.ttg.cells[8] = "O"
        self.ttg.cells[9] = "O"
        self.assertEqual('O', self.ttg.check_winner())

    def test_first_row_win(self):
        self.ttg.cells[1] = "X"
        self.ttg.cells[4] = "X"
        self.ttg.cells[7] = "X"
        self.assertEqual('X', self.ttg.check_winner())

        self.ttg.cells[1] = "O"
        self.ttg.cells[4] = "O"
        self.ttg.cells[7] = "O"
        self.assertEqual('O', self.ttg.check_winner())

    def test_second_row_win(self):
        self.ttg.cells[2] = "X"
        self.ttg.cells[5] = "X"
        self.ttg.cells[8] = "X"
        self.assertEqual('X', self.ttg.check_winner())

        self.ttg.cells[2] = "O"
        self.ttg.cells[5] = "O"
        self.ttg.cells[8] = "O"
        self.assertEqual('O', self.ttg.check_winner())

    def test_third_row_win(self):
        self.ttg.cells[3] = "X"
        self.ttg.cells[6] = "X"
        self.ttg.cells[9] = "X"
        self.assertEqual('X', self.ttg.check_winner())

        self.ttg.cells[3] = "O"
        self.ttg.cells[6] = "O"
        self.ttg.cells[9] = "O"
        self.assertEqual('O', self.ttg.check_winner())

    def test_first_diag_win(self):
        self.ttg.cells[1] = "X"
        self.ttg.cells[5] = "X"
        self.ttg.cells[9] = "X"
        self.assertEqual('X', self.ttg.check_winner())

        self.ttg.cells[1] = "O"
        self.ttg.cells[5] = "O"
        self.ttg.cells[9] = "O"
        self.assertEqual('O', self.ttg.check_winner())

    def test_second_diag_win(self):
        self.ttg.cells[3] = "X"
        self.ttg.cells[5] = "X"
        self.ttg.cells[7] = "X"
        self.assertEqual('X', self.ttg.check_winner())

        self.ttg.cells[3] = "O"
        self.ttg.cells[5] = "O"
        self.ttg.cells[7] = "O"
        self.assertEqual('O', self.ttg.check_winner())

    @mock.patch('builtins.print')
    def test_valudate_input(self, mock_print):
        self.assertEqual(False, self.ttg.validate_input('qwerty'))
        self.assertEqual(False, self.ttg.validate_input(10))
        self.assertEqual(False, self.ttg.validate_input(0))

        self.ttg.cells[5] = "X"
        self.assertEqual(False, self.ttg.validate_input(5))

        self.ttg.cells[5] = "O"
        self.assertEqual(False, self.ttg.validate_input(5))

        self.assertEqual(True, self.ttg.validate_input(1))

    @mock.patch('builtins.print')
    def test_choice_symbol(self, mock_print):
        with mock.patch('builtins.input', return_value='H'):
            self.assertEqual(False, self.ttg.choice_symbol())

        with mock.patch('builtins.input', return_value='O'):
            self.assertEqual(True, self.ttg.choice_symbol())

    def test_change_player(self):
        self.ttg.curr_player = "X"
        self.ttg.change_player()
        self.assertEqual(self.ttg.curr_player, "O")

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
