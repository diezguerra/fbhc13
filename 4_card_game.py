#!/usr/bin/python
# -*- coding: utf-8 -*-


from scipy.misc import comb


FILE_NAME = '4_card_game_fb'


if __name__ == '__main__':
    """
    = Card Game =

    John is playing a game with his friends. The game's rules are as follows:
    There is deck of N cards from which each person is dealt a hand of K cards.
    Each card has an integer value representing its strength. A hand's strength
    is determined by the value of the highest card in the hand. The person with
    the strongest hand wins the round. Bets are placed before each player
    reveals the strength of their hand.

    John needs your help to decide when to bet. He decides he wants to bet when
    the strength of his hand is higher than the average hand strength. Hence
    John wants to calculate the average strength of ALL possible sets of hands.
    John is very good at division, but he needs your help in calculating the
    sum of the strengths of all possible hands.

    == Problem ==
    You are given an array a with N ≤ 10 000 different integer numbers and a
    number, K, where 1 ≤ K ≤ N. For all possible subsets of a of size K find
    the sum of their maximal elements modulo 1 000 000 007.

    == Input ==
    The first line contains the number of test cases T, where 1 ≤ T ≤ 25

    Each case begins with a line containing integers N and K. The next line
    contains N space-separated numbers 0 ≤ a [i] ≤ 2 000 000 000, which
    describe the array a.

    == Output ==
    For test case i, numbered from 1 to T, output "Case #i: ", followed by a
    single integer, the sum of maximal elements for all subsets of size K
    modulo 1 000 000 007.

    == Example ==
    For a = [3, 6, 2, 8] and N = 4 and K = 3, the maximal numbers among all
    triples are 6, 8, 8, 8 and the sum is 30.

    """

    result = []

    with open(FILE_NAME, 'r') as input:
        T = int(input.readline().strip())

        for t_i in range(1, T + 1):
            N, K = [int(number) for number in input.readline().split() \
                    if number != '']
            numbers = [int(number) for number in input.readline().split()]
            numbers.sort(reverse=True)

            value = 0
            for index, number in enumerate(numbers[:N - K + 1]):
                value += number * (
                    comb(N - (index + 1), K - 1, True) % 1000000007)

            result.append("Case #{}: {}".format(t_i, value % 1000000007))

    print "\n".join(result)

    with open(FILE_NAME + '_result', 'w') as result_file:
        result_file.write("\n".join(result))
