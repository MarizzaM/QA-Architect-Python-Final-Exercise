def average_calculate(*args):
    grades_sum = 0
    for x in args:
        grades_sum = grades_sum + x

    return grades_sum/len(args)


def bonus_add(*args):
    new_list = []
    for x in args:
        x = x + 5
        new_list.append(x)

    return new_list


def result_get(args):
    if args == 100:
        return 'Excellent'
    elif args >= 80:
        return 'Very Good'
    elif args >= 70:
        return 'Good'
    elif args >= 60:
        return 'Pass'
    else:
        return 'Fail'
