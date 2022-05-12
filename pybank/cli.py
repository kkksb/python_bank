"""Console script for pybank."""
import argparse
import sys
import pybank as pyb


def main():
    pybank = pyb.PyBank()
    
    """Console script for pybank."""
    parser = argparse.ArgumentParser(description="python practice")
    parser.add_argument('operate', help="python bank application")
    args = parser.parse_args()

    if args.operate == "operate":
        pybank.operate()

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
