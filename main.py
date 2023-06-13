import random, time
import tabulate


def qsort(a, pivot_fn):
    if len(a) == 0:
        return a
    else:
        pivot = pivot_fn(a)
        less = list(filter(lambda x: x < pivot, a))
        equal = list(filter(lambda x: x == pivot, a))
        more = list(filter(lambda x: x > pivot, a))

        p1 = qsort(less, pivot_fn)
        p2 = qsort(more, pivot_fn)

        return p1 + equal + p2


def ssort(L):
    for i in range(len(L)):
        m = L.index(min(L[i:]))
        L[i], L[m] = L[m], L[i]
    return L


def choose_fixed_pivot(a):
    return a[0]


def choose_random_pivot(a):
    return random.choice(a)


def time_search(sort_fn, mylist):
    start = time.time()
    sort_fn(mylist)
    return (time.time() - start) * 1000


def time_search2(sort_fn, pivot_fn, mylist):
    start = time.time()
    sort_fn(mylist, pivot_fn)
    return (time.time() - start) * 1000


def compare_sort(sizes=[100, 200, 300, 400, 500, 600, 700, 800, 900, 1000], shuffle=True):
    result = []
    for size in sizes:
        mylist = list(range(size))
        if shuffle:
            random.shuffle(mylist)
        result.append([
            len(mylist),
            time_search2(qsort, choose_fixed_pivot, mylist),
            time_search2(qsort, choose_random_pivot, mylist),
            time_search(ssort, mylist)
        ])
    return result


def print_results(results):
    headers = ['n', 'qsort-fixed-pivot', 'qsort-random-pivot', 'selection-sort']
    print(tabulate.tabulate(results, headers=headers, floatfmt=".3f", tablefmt="github"))


random.seed()

print("Random Permutations:")
results_random = compare_sort()
print_results(results_random)
