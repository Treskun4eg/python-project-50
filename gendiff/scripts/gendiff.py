#!/usr/bin/env python3
from gendiff.modules.generate_diff import generate_diff
import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='stylish',
                        choices=['stylish', 'plain', 'json'],
                        help='set format of output')
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, format=args.format))


if __name__ == '__main__':
    main()
