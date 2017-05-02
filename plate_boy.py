bar_weight = 45
plate_sizes = [45,35,25,10,5,2.5]
plate_inventory = [10,10,10,10,10,10]
percent_increments = [60,80,100]

def get_target():
    target_weight = float(input("Enter your target weight (lb): "))
    return target_weight

def get_arrangement(target, percent):
    remainder = ((target * (100 / percent)) - bar_weight
    plate_pairs = [0,0,0,0,0,0]
    for i in plate_sizes:
        while (remainder // (2 * i)) > 0: # while you can still add 2 plates without going below zero
            plate_pairs[i] += 1 # add a pair of plates to the counter
            remainder -= (2 * i) # subtract weight of added plate pair from remainder
    
    print("To get", percent + "% of target", target + "lbs")
    print("with bar weight of", bar_weight, "lbs:")
    for i in plate_sizes:
        print(i, "plates:", plate_pairs[i],"pairs"
    if remainder > 0:
        print("Error: Arrangement is ", remainder, "lbs short of target weight."
    

target = get_target()
for i in percent_increments:
    get_arrangement(target, i)
