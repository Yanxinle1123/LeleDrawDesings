from LeleDrawDesigns.die import Die


def dice_analysis(num_sides=6, dice_count=1000):
    die = Die(num_sides)

    list_results = []
    for _ in range(dice_count):
        result = die.roll()
        list_results.append(result)

    frequencies = []
    poss_results = range(1, die.num_sides + 1)
    for value in poss_results:
        frequency = list_results.count(value)
        frequencies.append(frequency)

    return poss_results, frequencies
