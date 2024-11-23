import argparse


def get_args() -> argparse.Namespace:
    """
    Parses command-line arguments and returns them as an argparse.Namespace object.

    Returns:
        argparse.Namespace: The parsed arguments from the command line.
    """

    parser = argparse.ArgumentParser(
        prog="ccwc", description="This is a clone of the command wc from linux"
    )

    parser.add_argument(
        "-c", action="store_true", help="Argument -c return the number of bytes"
    )

    parser.add_argument(
        "-l", action="store_true", help="Argument -l return the number of lines"
    )

    parser.add_argument(
        "-w", action="store_true", help="Argument -w return the number of words"
    )

    parser.add_argument(
        "-m", action="store_true", help="Argument -m return the number of characters"
    )

    parser.add_argument(
        "file",
        type=str,
        nargs="?",
        help="The file to process",
    )

    return parser.parse_args()
