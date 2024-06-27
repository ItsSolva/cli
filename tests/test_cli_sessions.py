import unittest
from unittest.mock import MagicMock, patch
import argparse
from httpie.manager.tasks.sessions import cli_sessions, Environment, ExitStatus, branch_coverages

class TestCliSessions(unittest.TestCase):

    def setUp(self):
        self.env = Environment()

    @patch('httpie.manager.tasks.sessions.parser')
    def test_action_none(self, mock_parser):
        args = argparse.Namespace(cli_sessions_action=None)
        mock_parser.error = MagicMock(side_effect=SystemExit)
        with self.assertRaises(SystemExit):
            cli_sessions(self.env, args)
        mock_parser.error.assert_called_once_with("Please specify one of these: 'help', 'upgrade', 'upgrade-all'")

    @patch('httpie.manager.tasks.sessions.cli_upgrade_session')
    def test_action_upgrade(self, mock_upgrade):
        args = argparse.Namespace(cli_sessions_action='upgrade')
        mock_upgrade.return_value = ExitStatus.SUCCESS
        result = cli_sessions(self.env, args)
        mock_upgrade.assert_called_once_with(self.env, args)
        self.assertEqual(result, ExitStatus.SUCCESS)

    @patch('httpie.manager.tasks.sessions.cli_upgrade_all_sessions')
    def test_action_upgrade_all(self, mock_upgrade_all):
        args = argparse.Namespace(cli_sessions_action='upgrade-all')
        mock_upgrade_all.return_value = ExitStatus.SUCCESS
        result = cli_sessions(self.env, args)
        mock_upgrade_all.assert_called_once_with(self.env, args)
        self.assertEqual(result, ExitStatus.SUCCESS)

    def test_action_unexpected(self):
        args = argparse.Namespace(cli_sessions_action='unexpected')
        with self.assertRaises(ValueError) as context:
            cli_sessions(self.env, args)
        self.assertEqual(str(context.exception), 'Unexpected action: unexpected')

if __name__ == '__main__':
    unittest.main()
