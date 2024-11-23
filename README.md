# CCWC tool

This is my version of the Linux command line tool `wc`, the `ccwc`.
This code is part of the [Coding Challenges](https://codingchallenges.fyi/challenges/challenge-wc) from [John Cricket](https://github.com/johncrickett).

## How to run (Linux and Mac)

1. Clone this repository.
2. Install `ccwc` on your local machine using the following command:

```bash
make install
```

3. To run `ccwc`, simply pass some text or a text file:

```bash
ccwc test.txt
```

Have fun ❤️

## How to run with Python (Windows, Linux and Mac)

1. Clone this repository.
2. To run `ccwc`, simply execute the `ccwc.py` file with python, passing some text or a text file:

```bash
python ccwc.py test.txt
```

Have fun ❤️

## Supported options

The following options are supported:

1. `-c` Returns the number of bytes;
2. `-l` Returns the number of lines;
3. `-w` Returns the number of words;
4. `-m` Returns the number of characters;

To use, simply pass the desired option to `ccwc`:

```bash
ccwc -c test.txt
```

`ccwc` also supports multiple options:

```bash
ccwc -c -m test.txt
```

## Uninstall CCWC

If you have installed `ccwc` on your local machine and want to uninstall it, simply run the command:

```bash
make uninstall
```

## Test

You can run the test with the following command:

```bash
make test
```

If you want to run with `python`, you can follow this command:

```bash
python tests.py
```
