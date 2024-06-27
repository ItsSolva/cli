import unittest
from unittest.mock import patch
from httpie.internal.update_warnings import fetch_updates, branch_coverages, Environment
from branch_tool import print_colored, get_coverage_percentage   

class TestFetchUpdates(unittest.TestCase):

    @patch('httpie.internal.update_warnings.spawn_daemon')
    @patch('httpie.internal.update_warnings._fetch_updates')
    def test_fetch_updates_lazy_true(self, mock_fetch_updates, mock_spawn_daemon):
        env = Environment()
        fetch_updates(env, lazy=True)
        
        # Verify spawn_daemon was called and _fetch_updates was not called
        mock_spawn_daemon.assert_called_once_with('fetch_updates')
        mock_fetch_updates.assert_not_called()
    
    @patch('httpie.internal.update_warnings.spawn_daemon')
    @patch('httpie.internal.update_warnings._fetch_updates')
    def test_fetch_updates_lazy_false(self, mock_fetch_updates, mock_spawn_daemon):
        env = Environment()
        fetch_updates(env, lazy=False)
        
        # Verify _fetch_updates was called and spawn_daemon was not called
        mock_fetch_updates.assert_called_once_with(env)
        mock_spawn_daemon.assert_not_called()

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
