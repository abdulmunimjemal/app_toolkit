"""
*************************************************************************
* Function: A python program to remove duplicate lines from a textfile. *
* Usage: python remove_duplicate.py <filename> <output_filename>        *
* Author: Abdulmunim J Jemal                                            *
* Prepared as part of the Amharic Spell Checker Project                 *
* Course: Fundamentals of Software Engineering                          *
* Department/Campus:  Software Engineering/AAiT                         *
* Date:  27/10/2023 G.C                                                 *
*************************************************************************
"""

import argparse


def remove_duplicate(input_list: list) -> list:
    """
    Removes duplicate from a list
    """
    output_list = []
    for line in input_list:
        line = line.strip()  # remove leading and trailing whitespaces
        if line not in output_list:
            output_list.append(line)
    return output_list


def remove_duplicate_file(input_file: str, output_file: str) -> None:
    """
    Removes duplicate from a file
    """
    input_name = input_file.split('.')[0]
    output_name = output_file.split('.')[0]
    with open(input_file, 'r', encoding='utf-8') as input_file:
        input_list = input_file.readlines()
        output_list = remove_duplicate(input_list)
        with open(output_file, 'w', encoding='utf-8') as output_file:
            for line in output_list:
                output_file.write(line + '\n')
    print(
        f"Removed {len(input_list) - len(output_list)} duplicate lines from {input_name} and saved to {output_name}")


def main():
    """
    Main function
    """
    parser = argparse.ArgumentParser(
        description='Remove duplicate lines from a text file')
    parser.add_argument('input_file', type=str, help='input file')
    parser.add_argument('output_file', type=str, help='output file')
    args = parser.parse_args()
    remove_duplicate_file(args.input_file, args.output_file)


if __name__ == '__main__':
    main()
