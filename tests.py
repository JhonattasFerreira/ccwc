import os
import tempfile
import unittest

from ccwc import get_output

TEXT_BYTES = b"Hello, world!\n Hi guys"  # 22 bytes


class TestCcwc(unittest.TestCase):
    def test_should_get_successful_output_with_c_arg(self):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(TEXT_BYTES)
            temp_file_path = temp_file.name
        try:
            args = Args(c=True, l=False, w=False, file=temp_file_path)
            expected_output = f"22 {temp_file_path}"

            result = get_output(args)

            self.assertEqual(result, expected_output)
        finally:
            os.remove(temp_file_path)

    def test_should_get_successful_output_with_l_arg(self):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(TEXT_BYTES)
            temp_file_path = temp_file.name
        try:
            args = Args(c=False, l=True, w=False, file=temp_file_path)
            expected_output = f"2 {temp_file_path}"

            result = get_output(args)

            self.assertEqual(result, expected_output)
        finally:
            os.remove(temp_file_path)

    def test_should_get_successful_output_with_c_and_l_args(self):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(TEXT_BYTES)
            temp_file_path = temp_file.name
        try:
            args = Args(c=True, l=True, w=False, file=temp_file_path)
            expected_output = f"2 22 {temp_file_path}"

            result = get_output(args)

            self.assertEqual(result, expected_output)
        finally:
            os.remove(temp_file_path)

    def test_should_get_successful_output_with_w_arg(self):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(TEXT_BYTES)
            temp_file_path = temp_file.name
        try:
            args = Args(c=False, l=False, w=True, file=temp_file_path)
            expected_output = f"4 {temp_file_path}"

            result = get_output(args)

            self.assertEqual(result, expected_output)
        finally:
            os.remove(temp_file_path)

    def test_should_get_successful_output_with_w_and_c_args(self):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(TEXT_BYTES)
            temp_file_path = temp_file.name
        try:
            args = Args(c=True, l=False, w=True, file=temp_file_path)
            expected_output = f"4 22 {temp_file_path}"

            result = get_output(args)

            self.assertEqual(result, expected_output)
        finally:
            os.remove(temp_file_path)

    def test_should_get_successful_output_with_w_and_l_args(self):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(TEXT_BYTES)
            temp_file_path = temp_file.name
        try:
            args = Args(c=False, l=True, w=True, file=temp_file_path)
            expected_output = f"2 4 {temp_file_path}"

            result = get_output(args)

            self.assertEqual(result, expected_output)
        finally:
            os.remove(temp_file_path)

    def test_should_get_successful_output_with_c_l_and_w_args(self):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(TEXT_BYTES)
            temp_file_path = temp_file.name
        try:
            args = Args(c=True, l=True, w=True, file=temp_file_path)
            expected_output = f"2 4 22 {temp_file_path}"

            result = get_output(args)

            self.assertEqual(result, expected_output)
        finally:
            os.remove(temp_file_path)

    def test_should_get_successful_output_with_m_arg(self):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(TEXT_BYTES)
            temp_file_path = temp_file.name
        try:
            args = Args(c=False, l=False, w=False, m=True, file=temp_file_path)
            expected_output = f"22 {temp_file_path}"

            result = get_output(args)

            self.assertEqual(result, expected_output)
        finally:
            os.remove(temp_file_path)

    def test_should_get_successful_output_with_c_and_m_arg(self):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(TEXT_BYTES)
            temp_file_path = temp_file.name
        try:
            args = Args(c=True, l=False, w=False, m=True, file=temp_file_path)
            expected_output = f"22 22 {temp_file_path}"

            result = get_output(args)

            self.assertEqual(result, expected_output)
        finally:
            os.remove(temp_file_path)

    def test_should_get_successful_output_with_l_and_m_arg(self):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(TEXT_BYTES)
            temp_file_path = temp_file.name
        try:
            args = Args(c=False, l=True, w=False, m=True, file=temp_file_path)
            expected_output = f"2 22 {temp_file_path}"

            result = get_output(args)

            self.assertEqual(result, expected_output)
        finally:
            os.remove(temp_file_path)

    def test_should_get_successful_output_with_w_and_m_arg(self):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(TEXT_BYTES)
            temp_file_path = temp_file.name
        try:
            args = Args(c=False, l=False, w=True, m=True, file=temp_file_path)
            expected_output = f"4 22 {temp_file_path}"

            result = get_output(args)

            self.assertEqual(result, expected_output)
        finally:
            os.remove(temp_file_path)

    def test_should_get_successful_output_with_c_l_and_m_arg(self):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(TEXT_BYTES)
            temp_file_path = temp_file.name
        try:
            args = Args(c=True, l=True, w=False, m=True, file=temp_file_path)
            expected_output = f"2 22 22 {temp_file_path}"

            result = get_output(args)

            self.assertEqual(result, expected_output)
        finally:
            os.remove(temp_file_path)

    def test_should_get_successful_output_with_c_w_and_m_arg(self):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(TEXT_BYTES)
            temp_file_path = temp_file.name
        try:
            args = Args(c=True, l=False, w=True, m=True, file=temp_file_path)
            expected_output = f"4 22 22 {temp_file_path}"

            result = get_output(args)

            self.assertEqual(result, expected_output)
        finally:
            os.remove(temp_file_path)

    def test_should_get_successful_output_with_l_w_and_m_arg(self):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(TEXT_BYTES)
            temp_file_path = temp_file.name
        try:
            args = Args(c=False, l=True, w=True, m=True, file=temp_file_path)
            expected_output = f"2 4 22 {temp_file_path}"

            result = get_output(args)

            self.assertEqual(result, expected_output)
        finally:
            os.remove(temp_file_path)

    def test_should_get_successful_output_with_all_args(self):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(TEXT_BYTES)
            temp_file_path = temp_file.name
        try:
            args = Args(c=True, l=True, w=True, m=True, file=temp_file_path)
            expected_output = f"2 4 22 22 {temp_file_path}"

            result = get_output(args)

            self.assertEqual(result, expected_output)
        finally:
            os.remove(temp_file_path)

    def test_should_get_successful_output_with_no_args(self):
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(TEXT_BYTES)
            temp_file_path = temp_file.name
        try:
            args = Args(c=False, l=False, w=False, m=False, file=temp_file_path)
            expected_output = f"2 4 22 {temp_file_path}"

            result = get_output(args)

            self.assertEqual(result, expected_output)
        finally:
            os.remove(temp_file_path)


class Args:
    def __init__(self, c=False, l=False, w=False, m=False, file=""):  # noqa: E741
        self.c = c
        self.l = l
        self.w = w
        self.m = m
        self.file = file


if __name__ == "__main__":
    unittest.main()
