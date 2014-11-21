import argparse


def init_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="Input music directory")
    parser.add_argument("-u", "--update", action='store_true', help="Run database update")
    return parser.parse_args()

