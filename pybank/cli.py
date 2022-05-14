"""Console script for pybank."""
import argparse
import sys
import pybank as pyb


def main():
    """Console script for pybank."""
    parser = argparse.ArgumentParser(description="python practice")

    parser.add_argument('operate', help="python bank start command[operate]")
    parser.add_argument('filename', help="input passbook filename in resouces")

    args = parser.parse_args()

    if args.operate == "operate" and args.filename is not None:
        pybank = pyb.PyBank(args.filename)
        pybank.operate()

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
