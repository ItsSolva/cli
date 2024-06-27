import unittest
from unittest.mock import Mock, patch
from httpie.compat import get_dist_name, branch_coverages
import importlib_metadata

def print_colored(text, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "reset": "\033[0m"
    }
    
    color_code = colors.get(color.lower(), colors["reset"])
    print(f"{color_code}{text}{colors['reset']}")


def get_coverage_percentage():
    total_branches = len(branch_coverages)
    executed_branches = sum([1 for value in branch_coverages.values() if value])
    return (executed_branches / total_branches) * 100

class TestGetDistName(unittest.TestCase):

    @patch('httpie.compat.getattr')
    def test_get_dist_name_dist_not_none(self, mock_getattr):
        entry_point = Mock()
        dist = Mock()
        dist.name = 'test_dist'
        mock_getattr.return_value = dist

        result = get_dist_name(entry_point)

        self.assertEqual(result, 'test_dist')
        mock_getattr.assert_called_once_with(entry_point, 'dist', None)

    @patch('httpie.compat.getattr', return_value=None)
    def test_get_dist_name_no_match(self, mock_getattr):
        entry_point = Mock()
        entry_point.pattern.match.return_value = None

        result = get_dist_name(entry_point)

        self.assertIsNone(result)
        self.assertIn("get_dist_name_1", branch_coverages)
        self.assertTrue(branch_coverages["get_dist_name_1"])

    @patch('httpie.compat.getattr', return_value=None)
    @patch('httpie.compat.importlib_metadata.metadata')
    def test_get_dist_name_success(self, mock_metadata, mock_getattr):
        entry_point = Mock()
        entry_point.pattern.match.return_value.group.return_value = 'module'
        metadata = {'name': 'test_metadata'}
        mock_metadata.return_value = metadata

        result = get_dist_name(entry_point)

        self.assertEqual(result, 'test_metadata')


def test_print_coverage():
    print("\n==========================================")
    for key, value in branch_coverages.items():
        print(f"Branch {key} was ", end="")
        if value:
            print_colored("executed", "green")
        else:
            print_colored("not executed", "red")
    print("==========================================")

    if get_coverage_percentage() == 100:
        print_colored(f" Total coverage: {get_coverage_percentage()}%", "green")
    elif get_coverage_percentage() > 0:
        print_colored(f" Total coverage: {get_coverage_percentage()}%", "yellow")
    else:
        print_colored(f" Total coverage: {get_coverage_percentage()}%", "red")

if __name__ == '__main__':
    unittest.main()
