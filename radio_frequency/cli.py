"""Console script for radio_frequency."""
from __future__ import print_function
import argparse
import sys
from radio_frequency import radio_frequency


def main():
    """Console script for radio_frequency."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args()

    result = radio_frequency.frequency_info(args._[0])
    print(' ')
    for key, value in result.items():
        print('%s: %s' % (key.upper(), value))
    print(' ')
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
