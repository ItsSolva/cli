import unittest
from unittest.mock import MagicMock, patch
import errno

from httpie.output.writer import write_message, branch_coverages

branch_coverages = {
    "no_output_options": False,
    "normal": False,
    "windows_with_colors": False,
    "windows_without_colors": False,
    "oserror": False,
    "oserror_traceback": False
}

class TestWriteMessage(unittest.TestCase):
    def setUp(self):
        self.requests_message = MagicMock()
        self.env = MagicMock()
        self.output_options = MagicMock()
        self.processing_options = MagicMock()
        self.extra_stream_kwargs = {}

        # Set up mocks for required attributes
        self.env.stdout = MagicMock()
        self.env.stdout_isatty = False
        self.env.stderr = MagicMock()
        self.env.is_windows = False
        self.processing_options.get_prettify.return_value = []

    def test_no_output_options(self):
        self.output_options.any.return_value = False
        write_message(self.requests_message, self.env, self.output_options, self.processing_options, self.extra_stream_kwargs)
        branch_coverages["no_output_options"] = True

    @patch('httpie.output.writer.write_stream')
    def test_normal(self, mock_write_stream):
        self.output_options.any.return_value = True
        self.env.is_windows = False
        write_message(self.requests_message, self.env, self.output_options, self.processing_options, self.extra_stream_kwargs)
        mock_write_stream.assert_called_once()
        branch_coverages["normal"] = True

    @patch('httpie.output.writer.write_stream_with_colors_win')
    def test_windows_with_colors(self, mock_write_stream_with_colors_win):
        self.output_options.any.return_value = True
        self.env.is_windows = True
        self.processing_options.get_prettify.return_value = ['colors']
        write_message(self.requests_message, self.env, self.output_options, self.processing_options, self.extra_stream_kwargs)
        branch_coverages["windows_with_colors"] = True
        mock_write_stream_with_colors_win.assert_called_once()

    @patch('httpie.output.writer.write_stream')
    def test_windows_without_colors(self, mock_write_stream):
        self.output_options.any.return_value = True
        self.env.is_windows = True
        self.processing_options.get_prettify.return_value = []
        write_message(self.requests_message, self.env, self.output_options, self.processing_options, self.extra_stream_kwargs)
        branch_coverages["windows_without_colors"] = True
        mock_write_stream.assert_called_once()

    @patch('httpie.output.writer.write_stream')
    def test_oserror(self, mock_write_stream):
        self.output_options.any.return_value = True
        mock_write_stream.side_effect = OSError()
        self.processing_options.show_traceback = False
        with self.assertRaises(OSError):
            write_message(self.requests_message, self.env, self.output_options, self.processing_options, self.extra_stream_kwargs)
        branch_coverages["oserror"] = True

    @patch('httpie.output.writer.write_stream')
    def test_oserror_traceback(self, mock_write_stream):
        self.output_options.any.return_value = True
        e = OSError()
        e.errno = errno.EPIPE
        mock_write_stream.side_effect = e
        self.processing_options.show_traceback = True
        write_message(self.requests_message, self.env, self.output_options, self.processing_options, self.extra_stream_kwargs)
        branch_coverages["oserror_traceback"] = True

if __name__ == '__main__':
    unittest.main()
