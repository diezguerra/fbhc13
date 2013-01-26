#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import Counter
import re


RANGE_OF_VALUES = range(1,27)
FILE_NAME = 'beautiful_strings_fb'

if __name__ == '__main__':
    """
    When John was a little kid he didn't have much to do. There was no
    internet, no Facebook, and no programs to hack on. So he did the only thing
    he could... he evaluated the beauty of strings in a quest to discover the
    most beautiful string in the world.

    Given a string s, little Johnny defined the beauty of the string as the sum
    of the beauty of the letters in it.

    The beauty of each letter is an integer between 1 and 26, inclusive, and no
    two letters have the same beauty. Johnny doesn't care about whether letters
    are uppercase or lowercase, so that doesn't affect the beauty of a letter.
    (Uppercase 'F' is exactly as beautiful as lowercase 'f', for example.)

    You're a student writing a report on the youth of this famous hacker. You
    found the string that Johnny considered most beautiful. What is the maximum
    possible beauty of this string?

    Input
    #####

    The input file consists of a single integer m followed by m lines.

    Output
    ######

    Your output should consist of, for each test case, a line containing the
    string "Case #x: y" where x is the case number (with 1 being the first case
    in the input file, 2 being the second, etc.) and y is the maximum beauty
    for that test case.

    Constraints
    ###########

    5 ≤ m ≤ 50
    2 ≤ length of s ≤ 500

    """
    result = []

    for line_nr, line in enumerate(open(FILE_NAME, 'r')):
        # Skips first line cause it's the one with the count

        if not line_nr:
            continue

        # We parse the line: only lowercase letters
        regex = re.compile(r'[a-z]+')
        line = "".join(regex.findall(line.lower()))

        # Bean counting time!
        counter = Counter(line)
        most_common = counter.most_common()

        beauty = 0
        for value in range(27 - len(most_common), 27)[::-1]:
            beauty += value * most_common[26 - value][1]

        result.append("Case #{}: {}".format(line_nr, beauty))

    with open(FILE_NAME + '_result', 'w') as result_file:
        result_file.write("\n".join(result))
