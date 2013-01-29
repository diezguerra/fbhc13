#!/usr/bin/python
# -*- coding: utf-8 -*-


from collections import Counter


FILE_NAME = '3_find_the_min'


def _random_gen(a, b, c, r, k):
    """

    Because the values of n and k can be very large, we use a pseudo-random
    number generator to calculate the first k values of m. Given positive
    integers a, b, c and r, the known values of m can be calculated as follows:
    m[0] = a
    m[i] = (b * m[i - 1] + c) % r, 0 < i < k

    """
    result = [0] * (2 * k)

    lastm = a

    for i in range(0, k):
        if not i:
            result[i] = a
        else:
            lastm = (b * lastm + c) % r
            result[i] = lastm

    return result


def _find_smallest(k_sortedlist):
    """Finds the smallest "hole" in the heap"""
    smallest_k = -1

    for index in range(0, len(k_sortedlist)):
        second_smallest_k = k_sortedlist[index]

        diff = second_smallest_k - smallest_k

        if diff > 1:
            break

        smallest_k = second_smallest_k

    return smallest_k + 1


if __name__ == '__main__':
    """
    After sending smileys, John decided to play with arrays. Did you know that
    hackers enjoy playing with arrays? John has a zero-based index array, m,
    which contains n non-negative integers. However, only the first k values of
    the array are known to him, and he wants to figure out the rest.

    John knows the following: for each index i, where k <= i < n, m[i] is the
    minimum non-negative integer which is *not* contained in the previous *k*
    values of m.

    For example, if k = 3, n = 4 and the known values of m are [2, 3, 0], he
    can figure out that m[3] = 1.

    John is very busy making the world more open and connected, as such, he
    doesn't have time to figure out the rest of the array. It is your task to
    help him.

    Given the first k values of m, calculate the nth value of this array.
    (i.e. m[n - 1]).

    Input
    #####

    The first line contains an integer T (T <= 20), the number of test cases.
    This is followed by T test cases, consisting of 2 lines each.
    The first line of each test case contains 2 space separated integers,
        n, k (1 <= k <= 105, k < n <= 109).
    The second line of each test case contains 4 space separated integers,
        a, b, c, r (0 <= a, b, c <= 109, 1 <= r <= 109).

    Output
    ######

    For each test case, output a single line containing the case number and
    the nth element of m.

    """

    result = []

    with open(FILE_NAME, 'r') as input:
        T = int(input.readline())

        for t_i in range(0, T):
            n, k = [int(number) for number in input.readline().split()]
            a, b, c, r = [int(number) for number in input.readline().split()]

            m = _random_gen(a, b, c, r, k)
            m_init = Counter(m[:k])
            k_nums = range(k + 1)

            for index in range(k, 2 * k):
                value = next(number for number in k_nums if not m_init[number])
                m[index] = value
                m_init[m[index - k]] -= 1
                k_nums.remove(value)

            result.append("Case #{}: {}".format(
                t_i + 1, m[k + (n - k - 1) % (k + 1)]))

    with open(FILE_NAME + '_result', 'w') as result_file:
        result_file.write("\n".join(result))
