bar_weight = 45
plate_sizes = [45, 35, 25, 10, 5, 2.5]
# plate_inventory = [10, 10, 10, 10, 10, 10]
percent_increments = [60, 80, 100]
dashes = "-----------------------------------"


def get_target():
    target_weight = float(input("Enter your target weight (lb): "))
    print(dashes)
    return target_weight


def get_arrangement(target, percent):
    adj_target = target * (percent / 100)
    remainder = adj_target - bar_weight
    plate_pairs = [0, 0, 0, 0, 0, 0]
    for index, amt in enumerate(plate_sizes):
        while (remainder // (2 * amt)) > 0:  # while you can still add 2 plates without going below zero
            plate_pairs[index] += 1  # add plates to the pair counter
            remainder -= (2 * amt)  # subtract weight of added pair from remainder

    print(str(percent) + "% of target", str(target), "lbs =", str(adj_target), # print percent of target wt
          "lbs (bar =", str(bar_weight), "lbs)\n")

    for index, amt in enumerate(plate_sizes): # print each plate count
        if plate_pairs[index] > 0:
            print(str(amt) + "lb plates:", str(plate_pairs[index]), "pair")

    if remainder > 0: # print remainder
        print("\n(Arrangement is ", str(remainder), "lbs ("+str("{0:.1f}".format(remainder/adj_target*100)) +"%)",
              "short of intended weight.)")
    print(dashes)

target = get_target()
for i in percent_increments:
    get_arrangement(target, i)
