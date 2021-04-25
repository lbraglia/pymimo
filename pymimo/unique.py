def unique(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

if __name__ == '__main__':
    l = [1,2,1,3]
    print(list(unique(l)))
