def grep(filename, search_text):
    matching = []
    with open(filename) as f:
        for line in f:
            if search_text in line:
                matching.append(line)
    return matching
