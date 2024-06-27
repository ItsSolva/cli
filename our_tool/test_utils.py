import unittest
from unittest.mock import patch
from pathlib import Path
from httpie.utils import get_site_paths, as_site
from httpie.compat import MIN_SUPPORTED_PY_VERSION, MAX_SUPPORTED_PY_VERSION
from httpie.utils import branch_coverages
import tempfile
from branch_tool import print_colored, get_coverage_percentage

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

    if get_coverage_percentage(branch_coverages) == 100:
        print_colored(f" Total coverage: {get_coverage_percentage(branch_coverages)}%", "green")
    elif get_coverage_percentage(branch_coverages) > 0:
        print_colored(f" Total coverage: {get_coverage_percentage(branch_coverages)}%", "yellow")
    else:
        print_colored(f" Total coverage: {get_coverage_percentage(branch_coverages)}%", "red")


if __name__ == '__main__':
    unittest.main()
