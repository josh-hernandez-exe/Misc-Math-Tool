#!/usr/bin/python
from collections import Counter
import math
import argparse

parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description="\n".join([
        "This program will take in input to define the dice pool, and calculate the distrobution of the possible sums when all the dice are rolled.",
        "Please note that this program assumes that the dice are *distigishable*."
    ])
)

parser.add_argument(
    "dice",
    nargs="*",
    help= "\n".join([
        "The dice used to calculate the distrobution.",
        "(Format: \"[num_dice] d[num_sides]\" or \"[num_sides]\" for only one of that die. )",
        "This can be repeated for any number of sided dice you wish to be part of the distrobution.",
        "Example: ./dice_distrobution.py d4 2 d6 d4"
    ])
)

parser.add_argument(
    "--bars",
    type=int,
    default=4*12,
    help= "\n".join([
        "The maximum number of bars printed for the distrobution.",
        "Making the max number of bars having multiple divisors will allow for more visual distinction.",
        "Note: 12 or any multiple of 12 has many small divisors."
    ])
)


def main():
    args = parser.parse_args()

    if not args.dice:
        print "Please enter in what dice you would like to calculate a distrobution for."
        return

    dice_list = []

    num_dice = None
    for value in args.dice:
        if isinstance(value, str):
            if value.isdigit():
                num_dice = int(value)

            elif value.lower().startswith("d"):

                if num_dice is None:
                    num_dice = 1

                num_sides = int(value[1:])

                dice_list.extend( num_sides for _ in range(num_dice) )

                num_dice = None

    print_curent_dice(dice_list)
    print ""
    sum_distrobution = calc_distrobution(dice_list)
    print_distrobution(sum_distrobution,max_bars=args.bars)


def print_curent_dice(dice_list,delimiter="  "):
    if not dice_list:
        return None
    
    count_dice = Counter()

    for num_sides in dice_list:
        count_dice[num_sides]+=1

    print "Input Dice"

    print_format = "{num_dice}:D{num_sides}"

    output_list = []

    for key in sorted(count_dice.keys()):
        num_dice = count_dice[key]
        output_list.append(print_format.format(
            num_dice=count_dice[key],
            num_sides=key,
        ))

    print delimiter.join(output_list)

def calc_distrobution(dice_list):

    if not dice_list:
        return None

    sum_distrobution = Counter()
    calc_distrobution_helper(0,0,dice_list,sum_distrobution )
    return sum_distrobution


def calc_distrobution_helper(cur_total,cur_index,dice_side_list,sum_counter):

    if cur_index >= len(dice_side_list):
        sum_counter[cur_total]+=1

    else:
        for value in range(1,dice_side_list[cur_index]+1):
            calc_distrobution_helper(cur_total+value,cur_index+1,dice_side_list,sum_counter)


def print_distrobution(sum_distrobution,max_bars=4*12,bar_char="-"):
    """
    Max bars is a multiple of 12, since it has many divisors.
    """
    num_sum_digits = max( len(str(value)) for value in sum_distrobution )
    num_count_digits = max(len(str(value)) for value in sum_distrobution.itervalues())

    sum_title = "SUM"
    count_title = "COUNT"

    num_sum_digits = max(num_sum_digits,len(sum_title))
    num_count_digits = max(num_count_digits,len(count_title))

    print_format = "{{sum_value:{num_sum_digits}d}}|{{count:{num_count_digits}d}}|{{bar}}".format(
        num_sum_digits=num_sum_digits,
        num_count_digits=num_count_digits,
    )

    print_header_format = "{{sum_title:{num_sum_digits}s}}|{{count_title:{num_count_digits}s}}|".format(
        num_sum_digits=num_sum_digits,
        num_count_digits=num_count_digits,
    )

    print "Distrobution"
    print print_header_format.format(
        sum_title=sum_title,
        count_title=count_title,
    )

    max_value = max(value for value in sum_distrobution.itervalues())

    for key in sorted(sum_distrobution.keys()):
        count_value = sum_distrobution[key]
        percent_of_max = float(count_value)/max_value
        num_bars = int(math.ceil(max_bars*percent_of_max))
        print print_format.format(
            sum_value=key,
            count=count_value,
            bar=bar_char*num_bars,
        )


if __name__ == '__main__':
    main()
