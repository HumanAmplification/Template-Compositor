import sys, json
from os.path import join, exists, getmtime
from compositor import Compositor

def main():
    """
    Main entry point to the Compositor application.
    This method takes an optional single command line argument
    which represents the root directory of the template project.
    """
    # If no args, assume current directory and default config
    load_dir = "."
    # If no config, use default
    config_file = None
    if len(sys.argv) > 1:
        load_dir = sys.argv[1]
    if len(sys.argv) > 2:
        config_file = sys.argv[2]
    Compositor(load_dir, config_file).compile()

if __name__ == "__main__":
    main()
