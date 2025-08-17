from random import sample

def generate_inputs(n):
    min_value = -100*n
    max_value = 100*n
    return sample(range(min_value, max_value), n)
