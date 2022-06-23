
words = open('sgb-words.txt').read().strip()
words = set(words.split())

known_pos = {2: 'i'}
wrong_pos = {'k': [0], 'n': [1, 4]}
must_nothaves = set('p e t y a d m f e '.split())
must_haves = list(wrong_pos.keys())

passed = []
for w in words:
    matched = True
    for l in w:
        if l in must_nothaves:
            matched = False
            break


    for p, l in known_pos.items():
        if w[p] != l:
            matched = False
            break

    for l in must_haves:
        if l not in w:
            matched = False
            break

    for p, ls in wrong_pos.items():
        for l in ls:
            if w[l] == p:
                matched = False
                break
        if matched == False:
            break

    if matched:
        passed.append(w)

print(sorted(passed))


