def sum_avg(*args):
    result = (sum(args), sum(args)/len(args))
    return result

print(sum_avg(1,2,3,4,5))