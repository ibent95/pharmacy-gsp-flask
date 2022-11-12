import logging
import multiprocessing as mp

from collections import Counter

from services.common import Common

logging.basicConfig(level=logging.DEBUG)

class GSP:

    """
        Thanks to Petr Lorenc
        https://github.com/petrLorenc/GeneralizedSequentialPatternPython

    """

    def __init__(self, transactions, minsup):
        self.transactions = transactions
        self.max_size = max([len(item) for item in transactions])
        self.freq_patterns = []
        self.minsup = minsup
        assert (0.0 < self.minsup) and (self.minsup <= 1.0)
        self.minsup = len(transactions) * self.minsup
        #print("Minsup: " + str(self.minsup))

    def _is_slice_in_list(self, s, l, w):
        """
        :param s: slice we are looking for
        :param l: list where we are looking
        :param w: windows where to look for patterns
        :return: true/false
        """
        assert (w >= 0)

        len_s = len(s)  # so we don't recompute length of s on every iteration
        for idx_l in range(len(l) - len_s + 1):
            is_slice_in_list = True
            for idx_s in range(len_s):
                if type(l[idx_l + idx_s]) == frozenset:
                    if s[idx_s] not in l[idx_l + idx_s]:
                        if w == 0:
                            is_slice_in_list = False
                            break
                        else:
                            w -= 1
                else:
                    if s[idx_s] is not l[idx_l + idx_s]:
                        if w == 0:
                            is_slice_in_list = False
                            break
                        else:
                            w -= 1
            if is_slice_in_list:
                return True

        return False

    def _calc_frequency(self, results, item, window, k):
        # The number of times the item appears in the transactions
        #frequency = len([t for t in self.transactions if self._is_slice_in_list(item, t, window)])
        len_s = len(item)  # so we don't recompute length of s on every iteration

        frequency = 0
        results

        frequencyRawArray = []

        if k > 1: # if item`s length more than 1
            frequency = len([t for t in self.transactions if self._is_slice_in_list(item, t, window)])

            if frequency >= 1:
                results[tuple(item)] = frequency

        else: # if item`s length below 2
            for transaction in self.transactions:
                if self._is_slice_in_list(item, transaction, window):
                    for idx_l in range(len(transaction) - len_s + 1):
                        for idx_s in range(len_s):

                            if type(transaction[idx_l + idx_s]) == frozenset:
                                if item[idx_s] in transaction[idx_l + idx_s]:
                                    frequencyRawArray.append(item[idx_s])
                            else:
                                if item[idx_s] is transaction[idx_l + idx_s]:
                                    frequencyRawArray.append(item[idx_s])

            frequency = len(frequencyRawArray)

            if frequency >= self.minsup:
                results[tuple(item)] = frequency

        return results

    def _support(self, items, window=0, k=1):
        '''
        The support count (or simply support) for a sequence is defined as
        the fraction of total data-sequences that "contain" this sequence.
        (Although the word "contains" is not strictly accurate once we
        incorporate taxonomies, it captures the spirt of when a data-sequence
        contributes to the support of a sequential pattern.)
        Parameters
                items: set of items that will be evaluated
                minsup: minimum support
                window: TODO implement
        '''
        # results = mp.Manager().dict()
        # pool = mp.Pool(processes=mp.cpu_count())
        #
        # for item in items:
        #     pool.apply_async(self._calc_frequency,
        #                      args=(results, item, window))
        # pool.close()
        # pool.join()
        results = {}
        for item in items:
            element = []

            for itemIndex in range(k):
                element.append(item[itemIndex])

            results = self._calc_frequency(results, tuple(element), window, k)

        return dict(results)

    def _generate_candidates(self):
        o = []
        for l in self.transactions:
            for x in l:
                if type(x) is frozenset:
                    for xx in x:
                        o.append(xx)
                else:
                    o.append(x)
        return [tuple([x]) for x in (set(o))]

    def _do_product(self, items):
        """
        Combining the two tuples based on GSP alg - remove the first and last item
        and then try to match the rest together
        for example (a, b, c) and (b, c, e) create (a, b, c, e)
        :param items:
        :return:
        """
        new_candidates = []
        if max([len(i) for i in items]) == 1:
            for x in items:
                for y in items:
                    new_candidates.append((x[0], y[0]))
        else:
            # mapping_rest_to_first = {i[1:]: i[0] for i in items}
            # mapping_rest_to_last = {i[:-1]: i[-1] for i in items}

            for head in items:
                for tail in items:
                    if head[1:] == tail[:-1]:
                        new_candidates.append(tuple(head) + tuple(tail[-1]))

        return list(set(new_candidates))

    def _duplicateCandidatesCheck(self, candidates):

        sets = set(candidates)

        results = len(sets) != len(candidates)

        return results

    def run_alg(self):

        # Initially, every item in DB is a candidate
        candidates = self._generate_candidates()
        #print(candidates)

        # Iterations counter
        k_items = 1

        # Scan transactions to collect support count for each candidate
        self.freq_patterns.append(self._support(candidates, 0, k_items))

        # repeat until no frequent sequence or no candidate can be found
        while len(self.freq_patterns[k_items - 1]) and (k_items + 1 <= self.max_size):
            k_items += 1

            # Generate candidate sets Ck (set of candidate k-sequences) -
            # generate new candidates from the last "best" candidates filtered
            # by minimum support
            #items = list(set(self.freq_patterns[k_items - 2].keys()))
            items = list(set(self.freq_patterns[k_items - 2].keys()))

            #candidates = list(self._do_product(items))
            candidates = list(candidate for candidate in self._do_product(items) if self._duplicateCandidatesCheck(list(candidate)) != True)
            #candidates = items

            # Candidate pruning - eliminates candidates who are not potentially
            # frequent (using support as threshold)
            self.freq_patterns.append(self._support(candidates, 0, k_items))

        Common.setLogger('info', 'GSP calculation test 2', {
            #'transactions': self.transactions,
            'freq_patterns': self.freq_patterns,
            'minsup': self.minsup,
        })

        if len(self.freq_patterns) == 1:
            return self.freq_patterns[-1]

        return self.freq_patterns


if __name__ == '__main__':
    ## 1
    transactions = [
        ["a", "b", "c", frozenset(["c", "d"]), "d"],
        ["a", "a", "b", frozenset(["c", "d"]), 'c'],
        ["a", "a"]
    ]

    ## 2
    transactions = [
        [
            frozenset({'sv'}),
            frozenset({'x'}),
            frozenset({'+', 'qo', 'sv'}),
            frozenset({'sv'}),
            frozenset({'x'}),
            frozenset({'sd', 'sv'}),
            frozenset({'%', 'sd', 'sv'}),
            frozenset({'b'}),
            frozenset({'+', 'sd'}),
            frozenset({'sv'}),
            frozenset({'+'}),
            frozenset({'b'}),
            frozenset({'sd'}),
            frozenset({'%', 'aa'}),
            frozenset({'+', 'sv'}),
            frozenset({'b'}),
            frozenset({'sv'}),
            frozenset({'b'}),
            frozenset({'+', 'sv(^q)'}),
            frozenset({'aa'}),
            frozenset({'+', '^q', 'qh'}),
            frozenset({'aa'}),
            frozenset({'sv'}),
            frozenset({'sv'}),
            frozenset({'+', 'sv'}),
            frozenset({'%', 'sd', 'sv', 'sv^r'}),
            frozenset({'^q', 'qh', 'sd', 'sv', 'sv(^q)'}),
            frozenset({'aa'}),
            frozenset({'+'}),
            frozenset({'aa', 'sv'}),
            frozenset({'sd'}),
            frozenset({'bf'}),
            frozenset({'aa', 'sd'}),
            frozenset({'b^m'}),
            frozenset({'+'}),
            frozenset({'b'}),
            frozenset({'%', 'o', 'qy'}),
            frozenset({'qr'}),
            frozenset({'b', 'sd'}),
            frozenset({'%'}),
            frozenset({'+'}),
            frozenset({'x'}),
            frozenset({'+', 'sd'}),
            frozenset({'^2'}),
            frozenset({'sd'}),
            frozenset({'%'}),
            frozenset({'+', 'sd'}),
            frozenset({'b'}),
            frozenset({'+'}),
            frozenset({'aa', 'sd', 'sv'}),
            frozenset({'aa', 'sd'}),
            frozenset({'b'}),
            frozenset({'^q', 'sd(^q)'}),
            frozenset({'b'}),
            frozenset({'sd'}),
            frozenset({'b', 'qw'}),
            frozenset({'sd'}),
            frozenset({'b', 'ba'}),
            frozenset({'aa', 'sd^t'}),
            frozenset({'x'}),
            frozenset({'+'}),
            frozenset({'x'}),
            frozenset({'+'}),
            frozenset({'b'}),
            frozenset({'+', 'sd^t'}),
            frozenset({'b'}),
            frozenset({'sd^t'}),
            frozenset({'bk'})
        ],
        [
            frozenset({'sd', 'sd^t'}),
            frozenset({'ba'}),
            frozenset({'b', 'sd^t'}),
            frozenset({'ba'}),
            frozenset({'sv^t'}),
            frozenset({'aa'}),
            frozenset({'ad'}),
            frozenset({'^h', 'aa'}),
            frozenset({'x'}),
            frozenset({'sd'}),
            frozenset({'aa', 'sv'}),
            frozenset({'sd'}),
            frozenset({'+'}),
            frozenset({'aa', 'sd'}),
            frozenset({'%'}),
            frozenset({'^h', 'sd'}),
            frozenset({'aa'}),
            frozenset({'+', '^h', 'sd', 't1'}),
            frozenset({'b'}),
            frozenset({'%'}),
            frozenset({'qy'}),
            frozenset({'sd'}),
            frozenset({'b', 'bf'}),
            frozenset({'qw', 'sd'}),
            frozenset({'sd'}),
            frozenset({'b'}),
            frozenset({'sd'}),
            frozenset({'b', 'b^r', 'sd'}),
            frozenset({'x'}),
            frozenset({'+'}),
            frozenset({'b'}),
            frozenset({'b'}),
            frozenset({'sd'}),
            frozenset({'sv'}),
            frozenset({'sd'}),
            frozenset({'sv'}),
            frozenset({'+'}),
            frozenset({'b', 'sd'}),
            frozenset({'sd'}),
            frozenset({'aa', 'aa^r', 'sv'}),
            frozenset({'sv'}),
            frozenset({'b', 'b^r'}),
            frozenset({'%', 'sd'}),
            frozenset({'ba', 'sv'}),
            frozenset({'%', 'b'}),
            frozenset({'%', 'qy'}),
            frozenset({'sd'}),
            frozenset({'b'}),
            frozenset({'sd'}),
            frozenset({'sd'}),
            frozenset({'sv'}),
            frozenset({'ba'}),
            frozenset({'+'}),
            frozenset({'qw'}),
            frozenset({'sd'}),
            frozenset({'%', 'b^m', 'bk', 'sd'}),
            frozenset({'b'}),
            frozenset({'%', '+'}),
            frozenset({'ad', 'b'}),
            frozenset({'aa', 'sd'}),
            frozenset({'sd', 'sv'}),
            frozenset({'+'}),
            frozenset({'+'}),
            frozenset({'b', 'b^r'}),
            frozenset({'sd'}),
            frozenset({'%', 'qy'}),
            frozenset({'%', 'sd'}),
            frozenset({'b', 'b^r', 'qo', 'sd'}),
            frozenset({'sd'}),
            frozenset({'%'}),
            frozenset({'sd', 'sv'}),
            frozenset({'%'}),
            frozenset({'sv'}),
            frozenset({'sd'}),
            frozenset({'sd'}),
            frozenset({'b', 'b^r'}),
            frozenset({'sd'}),
            frozenset({'b'}),
            frozenset({'sd'}),
            frozenset({'b', 'b^r'}),
            frozenset({'sd'}),
            frozenset({'sd'}),
            frozenset({'%'}),
            frozenset({'+', 'sd'}),
            frozenset({'b'}),
            frozenset({'+'}),
            frozenset({'b', 'sd'}),
            frozenset({'+'}),
            frozenset({'qy'}),
            frozenset({'+'}),
            frozenset({'+'}),
            frozenset({'sd'}),
            frozenset({'bh'}),
            frozenset({'sd'}),
            frozenset({'b', 'b^r'}),
            frozenset({'%', '+'}),
            frozenset({'b', 'qy^g'}),
            frozenset({'ny', 'ny^r'}),
            frozenset({'sv'}),
            frozenset({'qh', 'sv'}),
            frozenset({'aa', 'sv'}),
            frozenset({'%', 'b', 'b^r'}),
            frozenset({'sv'}),
            frozenset({'aa'}),
            frozenset({'sd'}),
            frozenset({'%', 'aa', 'sd'}),
            frozenset({'sv'}),
            frozenset({'aa'}),
            frozenset({'sv'}),
            frozenset({'sd'}),
            frozenset({'aa', 'qh', 'sv'}),
            frozenset({'aa'}),
            frozenset({'+'}),
            frozenset({'sd(^q)'}),
            frozenset({'+'}),
            frozenset({'+'}),
            frozenset({'%'}),
            frozenset({'sd'}),
            frozenset({'aa', 'sd', 'sv'}),
            frozenset({'b'}),
            frozenset({'+'}),
            frozenset({'ba'}),
            frozenset({'sd'}),
            frozenset({'x'}),
            frozenset({'%', 'sd'}),
            frozenset({'fe', 'qy'}),
            frozenset({'sd'}),
            frozenset({'%', '+'}),
            frozenset({'nn', 'sd^e'}),
            frozenset({'%', 'sd', 'x'}),
            frozenset({'sd'}),
            frozenset({'b'}),
            frozenset({'sd', 'sv'}),
            frozenset({'aa', 'sd'})
        ],
        [
            frozenset({'o', 'qrr', 'qw', 'sd', 'sv'}),
            frozenset({'sd'}),
            frozenset({'b'}),
            frozenset({'+'}),
            frozenset({'aa'}),
            frozenset({'sd'}),
            frozenset({'b', 'sd'}),
            frozenset({'b'}),
            frozenset({'sd', 'sd(^q)'}),
            frozenset({'x'}),
            frozenset({'%', 'sd'}),
            frozenset({'sv'}),
            frozenset({'aa', 'sd'}),
            frozenset({'b'}),
            frozenset({'h', 'sd'})
        ]
    ]

    #alg = GSP(transactions=transactions, minsup=0.5)
    #print(alg.run_alg()[-2])

    # alg = GSP(transactions=transactions, minsup=0.5)
    # print(alg.run_alg()[-2])
