import unittest
from unittest.mock import patch
from functions import main, vars, balance_stat, budget_stat, income_stat, invest, transfer

class TestFunctions(unittest.TestCase):

    def setUp(self):
        vars()

    @patch('builtins.input', side_effect=["user123", "password", "USD", "E"])
    @patch('builtins.print')
    def test_main_first_time(self, mock_print, mock_input):
        main()
        self.assertFalse(firstTime)
        self.assertEqual(userId, "user123")
        self.assertEqual(password, "password")
        self.assertEqual(currency, "USD")
        mock_print.assert_any_call("As a signing bonus, you get 5000 USD")

    @patch('builtins.input', side_effect=["user123", "wrongpassword", "E"])
    @patch('builtins.print')
    def test_main_not_first_time_wrong_password(self, mock_print, mock_input):
        global firstTime, userId, password
        firstTime = False
        userId = "user123"
        password = "password"
        main()
        mock_print.assert_any_call("Wrong password")

    @patch('builtins.input', side_effect=["user123", "password", "I", "1000", "E"])
    @patch('builtins.print')
    def test_main_invest(self, mock_print, mock_input):
        global firstTime, userId, password
        firstTime = False
        userId = "user123"
        password = "password"
        balance = 6000
        main()
        self.assertNotEqual(balance, 6000)  # Balance should change after investing

    @patch('builtins.input', side_effect=["user123", "password", "T", "balance", "1000", "budget", "E"])
    @patch('builtins.print')
    def test_main_transfer(self, mock_print, mock_input):
        global firstTime, userId, password, balance, budget
        firstTime = False
        userId = "user123"
        password = "password"
        balance = 6000
        budget = 2000
        main()
        self.assertEqual(balance, 5000)  # Balance should decrease
        self.assertEqual(budget, 3000)  # Budget should increase

    @patch('builtins.print')
    def test_balance_stat(self, mock_print):
        global balance, currency
        balance = 5000
        currency = "USD"
        balance_stat()
        mock_print.assert_called_with("Your balance has been updated to 5000 USD")

    @patch('builtins.print')
    def test_budget_stat(self, mock_print):
        global budget, currency
        budget = 2000
        currency = "USD"
        budget_stat()
        mock_print.assert_called_with("Your budget has been updated to 2000 USD")

    @patch('builtins.print')
    def test_income_stat(self, mock_print):
        global income, currency
        income = 3000
        currency = "USD"
        income_stat()
        mock_print.assert_called_with("Your income has been updated to 3000 USD")

    @patch('builtins.input', side_effect=["1000"])
    @patch('builtins.print')
    def test_invest_invalid_amount(self, mock_print, mock_input):
        global balance
        balance = 500
        invest()
        mock_print.assert_any_call("Invalid investment amount.")

    @patch('builtins.input', side_effect=["balance", "1000", "invalid"])
    @patch('builtins.print')
    def test_transfer_invalid_account(self, mock_print, mock_input):
        transfer()
        mock_print.assert_any_call("Invalid account specified.")

if __name__ == "__main__":
    unittest.main()
