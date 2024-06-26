import unittest
from unittest.mock import patch
from pathlib import Path
from httpie.utils import get_site_paths, as_site
from httpie.compat import MIN_SUPPORTED_PY_VERSION, MAX_SUPPORTED_PY_VERSION
from httpie.utils import branch_coverages
import tempfile

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

class TestGetSitePaths(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.path = Path(self.temp_dir.name)

    def tearDown(self):
        self.temp_dir.cleanup()

    @patch('httpie.compat.is_frozen', True)
    @patch('httpie.compat.MIN_SUPPORTED_PY_VERSION', (3, 6))
    @patch('httpie.compat.MAX_SUPPORTED_PY_VERSION', (3, 8))
    def test_is_frozen(self):
        expected_paths = [
            as_site(self.path, py_version_short='3.6'),
            as_site(self.path, py_version_short='3.7'),
            as_site(self.path, py_version_short='3.8')
        ]
        result_paths = list(get_site_paths(self.path))
        self.assertEqual(result_paths, expected_paths)

    @patch('httpie.compat.is_frozen', False)
    def test_not_frozen(self):
        expected_path = as_site(self.path)
        result_paths = list(get_site_paths(self.path))
        self.assertEqual(result_paths, [expected_path])

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
