bar_weight = 45
plate_sizes = [45, 35, 25, 10, 5, 2.5]
# plate_inventory = [10, 10, 10, 10, 10, 10]
percent_increments = [60, 80, 100]
divider_length = 48
dashes = "-" * divider_length
equals = '=' * divider_length

def get_exercise_names():
    names = []
    names.append(str(input('Enter the name of your first exercise: ')))
    while True:
        additional = ""
        additional = str(input('Enter another excercise, or leave [blank] to continue: '))
        if additional == "":
            break
        else:
            names.append(additional)
    return names

def add_target_weights(names):
    target_weights = {}
    for name in names:
        tgt = float(input("Enter your target weight for %s: " % (name)))
        target_weights[name] = tgt
    return target_weights

def get_ps():
    choice = str(input('Print or Save? [p,s] '))
    choice = choice.lower()
    print(dashes)
    return choice

def pair(x):
    return 2 * x

def print_or_save(content):
    if ps == 'p':
        print(content)
    elif ps == 's':
        with open("output.txt", "a") as myfile:
            myfile.write(content + '\n')

def make_header(name):
    print_or_save(equals)
    output = ('Excercise Calculations for ' + name)
    print_or_save(output)
    print_or_save(equals)

def exercise_output(name, target):
    make_header(name)
    for percent in percent_increments:
        arrangement_output(get_arrangement(name, target, percent))
        if percent < 100:
            print_or_save(dashes)
    print_or_save("")

def get_arrangement(name, target, percent):
    adj_target = target * (percent / 100)
    remainder = adj_target - bar_weight
    plate_pairs = [0] * len(plate_sizes) # make a list of zeroes to count plate quantities on
    arrangement = {'name':name, 'target':target, 'percent':percent}

    for index, size in enumerate(plate_sizes):
        while (remainder // (pair(size))) > 0:  # while you can still subtract a pair without going below zero
            plate_pairs[index] += 1  # add a pair to the pair counter
            remainder -= (pair(size)) # subtract weight of added pair from remainder
        arrangement[size] = plate_pairs[index] # add size:qty entry to output dictionary
    arrangement["remainder"] = remainder # add remaining weight to last dictionary entry

    return arrangement

def arrangement_output(arrangement):
    target = arrangement['target']
    percent = arrangement['percent']
    adj_target = target * (percent / 100)

    output = (str(percent) + "% of target " + str(target) + " lbs = " + str(adj_target) + " lbs")
    print_or_save(output)
    print_or_save("")
    for size, qty in arrangement.items():
        if size in {'name', 'target', 'percent'}:
            pass
        elif size != 'remainder':
            if qty > 0:
                output = ("%s lb plates: %s pair" % (size, qty))
                print_or_save(output)
        else:  # print remainder
            if qty != 0:
                output = ("(Arrangement is " + str(qty) + " lbs (" + str("{0:.1f}".format(qty/adj_target*100)) + "%) short)")
                print_or_save("")
                print_or_save(output)

names = get_exercise_names()
exercises = add_target_weights(names)
ps = get_ps()

for name, target in exercises.items():
    exercise_output(name, target)
