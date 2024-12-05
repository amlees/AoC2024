from collections import defaultdict

rule_list = []
update_list = []
with open("Day5/day5_input.txt", "r") as fptr:
    while current_line := fptr.readline().strip("\n"):
        # Runs until an empty line (Rules)
        a, b = current_line.split("|")
        rule_list.append((int(b), int(a))) # reverse to make part 2 easier

    while current_line := fptr.readline().strip("\n"):
        # Runs until an empty line (Updates)
        update_list.append([int(x) for x in current_line.split(",")])

rule_dict = defaultdict(set)
[rule_dict[key].add(value) for key, value in rule_list]

part_one_answer = 0
part_two_answer = 0
for update in update_list:
    number_incorrect = [len(list(rule_dict[update[ind]] & set(update[ind+1:]))) for ind in range(len(update))]
    if sum(number_incorrect) == 0:
        part_one_answer += update[len(update)//2]
    else:
        ind = 0
        while ind < len(update):
            if len(list(rule_dict[update[ind]] & set(update[ind+1:]))) > 0:
                update.append(update.pop(ind))
            else:
                ind += 1
        part_two_answer += update[len(update)//2]

print(f"Part One Answer: {part_one_answer}")
print(f"Part Two Answer: {part_two_answer}")