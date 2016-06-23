def main():
    test_cards = [
        [1,0,0,0],
        [1,0,1,1],
        [1,2,2,2],
        [1,0,2,2]
    ]

    solution = solve(test_cards)

    print "the cards are %s" % test_cards

    if solution:
        print "the cards at indices %s comprise a set" % solution
    else:
        print "there is no set in these cards"


def solve(cards):
    solutions = []
    
    # set up a loop to pick every pair of cards
    for i in range(len(cards)):
        for j in range(len(cards)):

            # don't pick the same card twice
            if (i == j):
                continue

            # determine the card needed to complete the set from the two we've picked
            desired = getDesiredCardForCards(cards[i], cards[j])

            # find that card from the visible cards
            # we also could do this with `if desired in cards`, but this way we will get the index of the desired card
            for k in range(len(cards)):

                # don't pick the same card twice
                if i == k or j == k:
                    continue

                # if it's a match
                if cards[k] == desired:
                    # log indices of the cards
                    sets = [i,j,k]

                    # don't add duplicates (i.e. [0,1,4] and [4,1,0] are the same set)
                    sets.sort()

                    if not sets in solutions:
                        solutions.append(sets)

    return solutions


def getDesiredCardForCards(card_a, card_b):
    desired = [0,0,0,0]

    # check every property of the pair of cards to build a third card that would complete a set
    for i in range(4):
        desired[i] = getDesiredProperty(card_a[i], card_b[i])

    return desired

def getDesiredProperty(a, b):
    # all the same value
    if a == b:
        return a

    # or the missing unique value. return 0, 1, or 2, whichever one isn't a or b
    need = set([0,1,2]) - set([a,b])

    return list(need)[0]
            
if __name__ == '__main__':
    main()
