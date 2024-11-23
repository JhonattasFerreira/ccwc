import sys

from typing import Optional


def get_lines(file_byte_code: bytes) -> int:
    """
    Counts the number of lines in the decoded file bytecode.

    Args:
        file_byte_code (bytes): The bytecode of the file.

    Returns:
        int: The number of lines in the file.
    """

    content = _decode_file_byte_code(file_byte_code)
    return len(content.splitlines())


def get_words(file_byte_code: bytes) -> int:
    """
    Counts the number of words in the decoded file bytecode.

    Args:
        file_byte_code (bytes): The bytecode of the file.

    Returns:
        int: The number of words in the file.
    """

    content = _decode_file_byte_code(file_byte_code)
    return len(content.split())


def get_characters(file_byte_code: bytes) -> int:
    """
    Counts the number of characters in the decoded file bytecode.

    Args:
        file_byte_code (bytes): The bytecode of the file.

    Returns:
        int: The number of characters in the file.
    """

    return len(_decode_file_byte_code(file_byte_code))


def get_byte_code_of_file(file: Optional[str]) -> Optional[bytes]:
    """
    Retrieves the bytecode of a file or reads from stdin if no file is provided.

    Args:
        file (Optional[str]): The path to the file. It can be None if reading from stdin.

    Returns:
        Optional[bytes]: The bytecode of the file or stdin input, or None if no input is provided.
    """

    if file is not None:
        with open(file, "rb") as f:
            return f.read()

    if not sys.stdin.isatty():
        return sys.stdin.buffer.read()

    return None


def _decode_file_byte_code(file_byte_code: bytes) -> str:
    """
    Decodes the bytecode into a UTF-8 string.

    Args:
        file_byte_code (bytes): The bytecode of the file.

    Returns:
        str: The decoded UTF-8 string.

    Raises:
        UnicodeDecodeError: If the bytecode cannot be decoded into a UTF-8 string.
    """
    try:
        return file_byte_code.decode("utf-8")
    except UnicodeDecodeError:
        print("Error decoding file. Ensure the file is in UTF-8 encoding.")
        sys.exit(1)
