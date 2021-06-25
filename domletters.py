#!/usr/bin/env python3
import re
import sys
import argparse
from collections import Counter
#######################################################
__author__='Asante Grey-Johnson'
#
# This program shows an implementation
# that counts dominant letters in alphabetic words
# of an ASCII text read from standard input, printing
# the total count on standard output.
#######################################################
DEBUG = 1


class Analyzer(object):
    def __init__(self):
        self.fname = ''

    def run(self):
        '''
            function analyzes for alphabetic words [a-zA-Z]
            Calculates the dominant letter count of each word
            encountered
        :return: prints to console the total count
        '''
        def read_file():
            '''
                function reads in user input file
            :return: input as string
            '''
            read_in = ''
            read_in = self.fname.read().replace('\n',' ')
            if DEBUG:
               print(f'[-D-] {read_in}')
            return read_in
        print('[-i-] Processing...')
        lines = read_file().split()
        actual_words = [word.lower() for word in lines if bool(re.match(r'\s*([a-zA-Z]+$)', word))]
        if DEBUG:
            print(f'[-D-] Actual words: {actual_words}')
        total_cnt = 0
        for word in actual_words:
            cnt_dict = Counter()
            for ch in word:
                cnt_dict[ch] += 1
            # return key with max value
            key = max(cnt_dict,key=cnt_dict.get)
            if DEBUG:
                print(f'[-D-] {cnt_dict}')
            print(f'[-i-] word count: {key} = {cnt_dict[key]}')
            total_cnt += cnt_dict[key]
        print(f'[-i-] Total Count: {total_cnt}')


def parse_options():
    '''
        Function collects parses user ArgumentParser
    :return: Namespace args
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('infile',
                       default=sys.stdin,
                       type=argparse.FileType('r'),
                       nargs='?')
    args = parser.parse_args()
    return args


def main():
    print('[-i-] DomLetters Analyzer Started...')
    analyzer = Analyzer()
    options = parse_options()
    analyzer.fname = options.infile
    analyzer.run()


if __name__ == '__main__':
    main()
