# minor diffs from 1.10 of python cookbook
def duplicated(items):
    seen = set()
    for item in items:
        if item in seen:
            yield True
        else:
            seen.add(item)
            yield False

if __name__ == '__main__':
    l = [1,2,1,3]
    print(list(unique(l)))
