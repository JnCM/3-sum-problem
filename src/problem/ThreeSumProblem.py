from utils.utils import generate_inputs

class ThreeSumProblem:
    def __init__(self, n):
        self.__n = n
        self.__inputs = generate_inputs(n)
    
    def get_inputs(self):
        return self.__inputs

    def solve_brute_force(self):
        triplets = []

        for i in range(self.__n):
            for j in range(self.__n):
                for k in range(self.__n):
                    if self.__inputs[i] + self.__inputs[j] + self.__inputs[k] == 0:
                        triplets.append((self.__inputs[i], self.__inputs[j], self.__inputs[k]))
        
        return triplets

    def solve_binary_search(self):
        pass

    def solve_best_algorithm(self):
        pass
