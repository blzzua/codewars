# https://www.codewars.com/kata/55eec0ee00ae4a8fa0000075

import gmpy2

# copypaste instead of from more_itertools import distinct_permutations
def distinct_permutations(iterable, r=None):
    # Algorithm: https://w.wiki/Qai
    def _full(A):
        while True:
            # Yield the permutation we have
            yield tuple(A)

            # Find the largest index i such that A[i] < A[i + 1]
            for i in range(size - 2, -1, -1):
                if A[i] < A[i + 1]:
                    break
            #  If no such index exists, this permutation is the last one
            else:
                return

            # Find the largest index j greater than j such that A[i] < A[j]
            for j in range(size - 1, i, -1):
                if A[i] < A[j]:
                    break

            # Swap the value of A[i] with that of A[j], then reverse the
            # sequence from A[i + 1] to form the new permutation
            A[i], A[j] = A[j], A[i]
            A[i + 1 :] = A[: i - size : -1]  # A[i + 1:][::-1]

    # Algorithm: modified from the above
    def _partial(A, r):
        # Split A into the first r items and the last r items
        head, tail = A[:r], A[r:]
        right_head_indexes = range(r - 1, -1, -1)
        left_tail_indexes = range(len(tail))

        while True:
            # Yield the permutation we have
            yield tuple(head)

            # Starting from the right, find the first index of the head with
            # value smaller than the maximum value of the tail - call it i.
            pivot = tail[-1]
            for i in right_head_indexes:
                if head[i] < pivot:
                    break
                pivot = head[i]
            else:
                return

            # Starting from the left, find the first value of the tail
            # with a value greater than head[i] and swap.
            for j in left_tail_indexes:
                if tail[j] > head[i]:
                    head[i], tail[j] = tail[j], head[i]
                    break
            # If we didn't find one, start from the right and find the first
            # index of the head with a value greater than head[i] and swap.
            else:
                for j in right_head_indexes:
                    if head[j] > head[i]:
                        head[i], head[j] = head[j], head[i]
                        break

            # Reverse head[i + 1:] and swap it with tail[:r - (i + 1)]
            tail += head[: i - r : -1]  # head[i + 1:][::-1]
            i += 1
            head[i:], tail[:] = tail[: r - i], tail[r - i :]

    items = list(iterable)

    try:
        items.sort()
        sortable = True
    except TypeError:
        sortable = False

        indices_dict = defaultdict(list)

        for item in items:
            indices_dict[items.index(item)].append(item)

        indices = [items.index(item) for item in items]
        indices.sort()

        equivalent_items = {k: cycle(v) for k, v in indices_dict.items()}

        def permuted_items(permuted_indices):
            return tuple(
                next(equivalent_items[index]) for index in permuted_indices
            )

    size = len(items)
    if r is None:
        r = size

    # functools.partial(_partial, ... )
    algorithm = _full if (r == size) else partial(_partial, r=r)

    if 0 < r <= size:
        if sortable:
            return algorithm(items)
        else:
            return (
                permuted_items(permuted_indices)
                for permuted_indices in algorithm(indices)
            )

    return iter(() if r else ((),))

groups = [] # precalculated
def prepare():
    primes = []
    prime, prev_prime = 11, 7
    while prev_prime < 50000:
        prime = int(gmpy2.next_prime(prev_prime))
        primes.append(prime)
        prev_prime = prime

    primes_set = set(primes)
    seen = set()
    for prime in primes:
        if prime in seen:
            continue
        group = set()
        for s in distinct_permutations(str(prime)):
            s_num = ''.join(s)
            if s_num[0] == '0':
                continue
            num = int(s_num)
            if num in primes_set:
                group.add(num)
                seen.add(num)
        if len(group) > 1:
            groups.append(sorted(group))
prepare()

def permutational_primes(n_max, k_perms):
    suitable_group_count = 0
    suitable_groups = []
    min_n, max_n = 0, 0
    for group in groups:
        sg = [d for d in group if d <= n_max]
        if len(sg) == k_perms + 1:
            suitable_groups.append(sg)
            suitable_group_count+=1
    if suitable_groups == []:
        return [0, 0, 0]
    min_n = suitable_groups[0][0]
    max_n = suitable_groups[-1][0]
    return [suitable_group_count, min_n, max_n]
