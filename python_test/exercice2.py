import numpy as np

def game(n_balls, n_output):
    if n_output > n_balls:
        raise Error(f"n_output {n_output} should be inferior to n_balls {n_balls}")

    container = [i for i in range(1, n_balls + 1)]
    winning_list = []
    for i in range (0, n_output):
        container_size = len(container)
        random_index = np.random.randint(container_size)
        winning_number = container.pop(random_index)
        winning_list.append(winning_number)
    
    winning_list.sort()
    return winning_list

n_balls = 50
n_output = 10
winning_list = game(n_balls, n_output)
print(f"winning_list is {winning_list}")

# as for unit tests, we could test serveral things:
#     - test the case when n_balls < n_output
#     - the length of the output
#     - make sure that there is no duplicate via difference
#     - make sure that all numbers are < 50 ?
#     - make sure of the randomness via covariance ?