import unittest
from unittest.mock import patch, mock_open
from httpie.cli.requestitems import KeyValueArg, ParseError, load_json, load_text_file, branch_coverages
from branch_tool import print_colored, get_coverage_percentage

class TestLoadFunctions(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data=b'test data')
    def test_load_text_file_success(self, mock_file):
        item = KeyValueArg(orig='file', value='test.txt', key='file', sep='=')
        result = load_text_file(item)
        self.assertEqual(result, 'test data')

    @patch('builtins.open', side_effect=OSError('file error'))
    def test_load_text_file_oserror(self, mock_file):
        item = KeyValueArg(orig='file', value='test.txt', key='file', sep='=')
        with self.assertRaises(ParseError) as context:
            load_text_file(item)
        self.assertIn('file error', str(context.exception))

    @patch('builtins.open', new_callable=mock_open, read_data=b'\xff\xff')
    def test_load_text_file_unicode_decode_error(self, mock_file):
        item = KeyValueArg(orig='file', value='test.txt', key='file', sep='=')
        with self.assertRaises(ParseError) as context:
            load_text_file(item)
        self.assertIn('cannot embed the content', str(context.exception))

    @patch('httpie.cli.requestitems.load_json_preserve_order_and_dupe_keys', side_effect=ValueError('json error'))
    def test_load_json_value_error(self, mock_load_json):
        arg = KeyValueArg(orig='json', value='{}', key='json', sep='=')
        with self.assertRaises(ParseError) as context:
            load_json(arg, '{}')
        self.assertIn('json error', str(context.exception))

    @patch('httpie.cli.requestitems.load_json_preserve_order_and_dupe_keys', return_value={'test_key': 'test_value'})
    def test_load_json_success(self, mock_load_json):
        arg = KeyValueArg(orig='json', value='{}', key='json', sep='=')
        result = load_json(arg, '{}')
        self.assertEqual(result, {'test_key': 'test_value'})

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
