import unittest
from unittest.mock import MagicMock, call
from io import BytesIO
import threading
from typing import Union
from httpie.uploads import ChunkedUploadStream, ChunkedMultipartUploadStream, branch_coverages

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


if __name__ == '__main__':
    unittest.main()
