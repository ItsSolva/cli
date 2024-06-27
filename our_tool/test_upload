import unittest
from unittest.mock import MagicMock, call
from io import BytesIO
import threading
from typing import Union
from httpie.uploads import ChunkedUploadStream, ChunkedMultipartUploadStream, branch_coverages

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


class TestChunkedUploadStream(unittest.TestCase):
    def setUp(self):
        self.stream = [b'chunk1', b'chunk2', b'chunk3']
        self.callback = MagicMock()
        self.event = threading.Event()

    def test_iter_without_event(self):
        chunked_upload_stream = ChunkedUploadStream(self.stream, self.callback)

        chunks = list(chunked_upload_stream)

        self.assertEqual(chunks, self.stream)
        self.assertEqual(self.callback.call_count, len(self.stream))
        self.callback.assert_has_calls([call(chunk) for chunk in self.stream])

    def test_iter_with_event(self):
        chunked_upload_stream = ChunkedUploadStream(self.stream, self.callback, self.event)

        chunks = list(chunked_upload_stream)

        self.assertEqual(chunks, self.stream)
        self.assertEqual(self.callback.call_count, len(self.stream))
        self.assertTrue(self.event.is_set())
        self.callback.assert_has_calls([call(chunk) for chunk in self.stream])


class TestChunkedMultipartUploadStream(unittest.TestCase):
    def setUp(self):
        self.chunk_size = 10
        self.data = b'chunk1chunk2chunk3chunk4chunk5'
        self.encoder = BytesIO(self.data)
        self.event = threading.Event()

    def test_iter_without_event(self):
        chunked_multipart_upload_stream = ChunkedMultipartUploadStream(self.encoder)

        chunks = list(chunked_multipart_upload_stream)

        self.assertEqual(b''.join(chunks), self.data)

    def test_iter_with_event(self):
        chunked_multipart_upload_stream = ChunkedMultipartUploadStream(self.encoder, self.event)

        chunks = list(chunked_multipart_upload_stream)

        self.assertEqual(b''.join(chunks), self.data)
        self.assertTrue(self.event.is_set())

    def test_iter_chunk_size(self):
        # Assuming ChunkedMultipartUploadStream uses self.chunk_size
        chunked_multipart_upload_stream = ChunkedMultipartUploadStream(self.encoder, self.event)
        chunked_multipart_upload_stream.chunk_size = self.chunk_size

        chunks = list(chunked_multipart_upload_stream)

        expected_chunks = [self.data[i:i + self.chunk_size] for i in range(0, len(self.data), self.chunk_size)]
        self.assertEqual(chunks, expected_chunks)
        self.assertTrue(self.event.is_set())


def as_bytes(data: Union[str, bytes]) -> bytes:
    if isinstance(data, str):
        return data.encode()
    return data


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
