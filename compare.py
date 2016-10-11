#!/usr/bin/python
import math


def get_changed_value_and_rest(line):
    """ Return the first value of the line as float, remainder as string.

    This is as we expect the first value to change, but the rest to be
    identical, if only the precision changes.
    """
    # We want the first value of the line, and remove the + or -.
    split_line = line.split(',', 1)
    changed_value = float(split_line[0][1:])
    rest = split_line[1:]
    return changed_value, rest


def main():
    """ Check diff of databaker CSV output between Python 2 and 3.

    We expect the only difference to be the precision change of CSV output
    (which is acceptable) otherwise something unexpected has happened.
    """
    # The assumption is that only the first value in the line has changed,
    # based on looking at the diff. The remainder of the line should be
    # identical.
    value_removed, rest_removed = None, None
    value_added, rest_added = None, None

    # Diff generated with git diff --word-diff=porcelain -U0 > py23diff after
    # running process.sh and storing all CSVs in one output directory.
    # NB: may separate these into Python 2 and 3 output directories in future.
    with open('py23diff', 'r') as f:
        for line in f:
            if "csv_out" in line:
                continue

            if line.startswith('-'):
                value_removed, rest_removed = get_changed_value_and_rest(line)

            if line.startswith('+'):
                assert value_removed is not None

                value_added, rest_added = get_changed_value_and_rest(line)
                print("{:14} {}".format(value_removed, value_added))
                # isclose in Python 3.5 and up only.
                # rel_tol=1e-11 passes as of commit
                # 138339be2a320376d906116c44ab42b56661794e.
                assert math.isclose(value_added, value_removed,
                                    rel_tol=1e-11)
                assert rest_removed == rest_added
                value_removed, rest_removed = None, None
                value_added, rest_added = None, None


if __name__ == '__main__':
    main()
