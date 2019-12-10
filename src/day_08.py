def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def part1(source):
    size = 25 * 6
    layers = list(chunks(source, size))
    minimum = 1000000000
    min_layer = 0
    for layer in layers:
        if layer.count("0") < minimum:
            minimum = layer.count("0")
            min_layer = layer
    return min_layer.count("1") * min_layer.count("2")


def part2(source):
    size = 25 * 6
    layers = list(chunks(source, size))
    img = layers[0]
    for layer in layers[1:]:
        img = [layer[p] if img[p] == "2" else img[p] for p in range(size)]
    print()
    for r in range(6):
        print("".join(img[r * 25 : (r + 1) * 25]).replace("0", " ").replace("1", "x"))
