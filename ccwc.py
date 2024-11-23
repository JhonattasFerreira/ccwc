#!/usr/bin/env python3
import sys

from cli import get_args
from helper import get_lines, get_words, get_characters, get_byte_code_of_file

NO_FILE_TEXT = "Provide a file or a text."


def main():
    """
    Main function that processes arguments, gets the output based on file or stdin,
    and writes the result to stdout. Exits with code 1 if no file or text is provided,
    otherwise exits with code 0.

    Returns:
        int: Exit status code (0 for success, 1 for error).
    """

    args = get_args()
    output = get_output(args)

    sys.stdout.write(output + "\n")

    if output.startswith(NO_FILE_TEXT):
        sys.exit(1)

    sys.exit(0)


def get_output(args) -> str:
    """
    Generates output based on the provided arguments (count lines, words, characters, and file size).
    If no valid file is provided, it returns an error message.

    Args:
        args: Command line arguments (including file path and flags).

    Returns:
        str: The output string with counts of lines, words, characters, and file size, or an error message.
    """

    output_parts = []

    if not any([args.c, args.l, args.w, args.m]):
        args.c = args.l = args.w = True

    file_byte_code = get_byte_code_of_file(args.file)

    if file_byte_code is None:
        return NO_FILE_TEXT

    if args.l:
        lines_count = get_lines(file_byte_code)
        output_parts.append(str(lines_count))

    if args.w:
        words_count = get_words(file_byte_code)
        output_parts.append(str(words_count))

    if args.m:
        characters_count = get_characters(file_byte_code)
        output_parts.append(str(characters_count))

    if args.c:
        file_size = len(file_byte_code)
        output_parts.append(str(file_size))

    if args.file:
        output_parts.append(args.file)

    return " ".join(output_parts)


if __name__ == "__main__":
    main()
