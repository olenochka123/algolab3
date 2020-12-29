def wedding(N, people):
    print(N, people)
    if people:
        tribes = [set()]
        for first, second in people:
            tribe_is_exist = 0
            for tribe in tribes:
                tribe_is_exist = 0
                if not tribe:
                    tribe.add(first)
                    tribe.add(second)
                elif first in tribe:
                    tribe.add(second)
                elif second in tribe:
                    tribe.add(first)
                else:
                    tribe_is_exist = 1
                if not tribe_is_exist:
                    break
            if tribe_is_exist:
                tribes.append({first, second})
        result = find_pairs(tribes)
    else:
        result = 0
    return result


def find_pairs(tribes):
    boys = []
    girls = []
    for tribe in tribes:
        boys_in_tribe = []
        girls_in_tribe = []
        for every_person in tribe:
            if every_person % 2:
                boys_in_tribe.append(every_person)
            else:
                girls_in_tribe.append(every_person)
        boys.append(len(boys_in_tribe))
        girls.append(len(girls_in_tribe))

    return sum(boys) * sum(girls) - sum((b * g for b, g in new_zip(boys, girls)))

def new_zip(a, b):
    my_list = []
    for x in range(min(len(a), len(b))):
        for z in range(min(len(a), len(b))):
            w = {a[x], b[x]}
            my_list.append(w)
            break
    return my_list


print('Example 1:')
print(wedding(3, ((1, 2), (7, 4), (3, 5))), '\n')
print('Example 2:')
print(wedding(5, ((1, 2), (2, 4), (1, 3), (3, 5), (8, 10))), '\n')
print('My example:')
print(wedding(4, ((1, 2), (2, 4), (3, 5), (8, 10))), '\n')
print('My example 2 :')
print(wedding(0, ()))

in_N = int(input())
in_people = [tuple(map(int, input().split(' '))) for u in range(in_N)]
print(wedding(in_N, in_people, ))
if __name__ == 'main':
    print(wedding())
    template_list = [(1, 2), (2, 4), (3, 5), (2, 3), (2, 15), (10, 8), (15, 20)]
