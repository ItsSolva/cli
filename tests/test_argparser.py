import unittest
from unittest.mock import patch, MagicMock
from httpie.cli.argparser import branch_coverages, HTTPieArgumentParser

class TestPrintManualFunction(unittest.TestCase):

    def setUp(self):
        global branch_coverages
        branch_coverages = {
            "man_page_available": True,
            "man_page_not_available": True,
        }

    @patch('httpie.output.ui.man_pages.is_available', return_value=True)
    @patch('httpie.output.ui.man_pages.display_for')
    def test_print_manual_man_page_available(self, mock_display_for, mock_is_available):
        mock_env = MagicMock()
        mock_env.program_name = 'test_program'

        class MockClass:
            env = mock_env
            def format_help(self):
                return 'Help text'

        instance = MockClass()
        instance.print_manual = HTTPieArgumentParser.print_manual.__get__(instance)

        instance.print_manual()

        global branch_coverages
        branch_coverages = {
            "man_page_available": True,
            "man_page_not_available": False,
        }
        mock_display_for.assert_called_once_with(mock_env, 'test_program')

    @patch('httpie.output.ui.man_pages.is_available', return_value=False)
    def test_print_manual_man_page_not_available(self, mock_is_available):
        mock_env = MagicMock()
        mock_env.program_name = 'test_program'
        mock_env.rich_console.pager.return_value.__enter__.return_value = None

        class MockClass:
            env = mock_env
            def format_help(self):
                return 'Help text'

        instance = MockClass()
        instance.print_manual = HTTPieArgumentParser.print_manual.__get__(instance)

        instance.print_manual()

        
        mock_env.rich_console.print.assert_called_once_with('Help text', highlight=False)


if __name__ == '__main__':
    unittest.main()
    
    
