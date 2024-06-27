import unittest
from unittest.mock import MagicMock, patch
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

    @patch('importlib_metadata.EntryPoint')
    def test_no_match(self, mock_entry_point):
        mock_entry_point.dist = None
        mock_entry_point.pattern.match.return_value = None
        result = get_dist_name(mock_entry_point)
        self.assertIsNone(result)
        self.assertTrue(branch_coverages["get_dist_name_1"])

    @patch('importlib_metadata.EntryPoint')
    @patch('importlib_metadata.metadata', side_effect=importlib_metadata.PackageNotFoundError)
    def test_package_not_found(self, mock_metadata, mock_entry_point):
        mock_entry_point.dist = None
        mock_entry_point.pattern.match.return_value.group.return_value = 'test_module'
        result = get_dist_name(mock_entry_point)
        self.assertIsNone(result)
        self.assertTrue(branch_coverages["get_dist_name_2"])



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
