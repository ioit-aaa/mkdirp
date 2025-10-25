import sys
from .mkdirp import mkdirp


def main():
    if len(sys.argv) < 2:
        print("Usage: mkdirp <directory>")
        sys.exit(1)
    
    path = sys.argv[1]
    created = mkdirp(path)
    print(f"Created: {created}")


if __name__ == "__main__":
    main()