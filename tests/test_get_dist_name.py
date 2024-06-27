import unittest
from unittest.mock import Mock, patch
from httpie.compat import get_dist_name, branch_coverages
import importlib_metadata

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


if __name__ == '__main__':
    unittest.main()
