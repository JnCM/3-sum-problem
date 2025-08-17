import sys
import time
from problem.ThreeSumProblem import ThreeSumProblem
from utils.Log import Log

if __name__ == "__main__":
    try:
        n = int(sys.argv[1])
        r = int(sys.argv[2])
    except Exception as e:
        print(f"Error in trying to fetch `n` and `r`, check the params! Error description: {e}")
        sys.exit(1)
    
    logs = Log()

    for i in range(r):
        problem = ThreeSumProblem(n)
        
        inputs = problem.get_inputs()
        logs.save_log("inputs", inputs, inputs, inputs)
        
        start_time_bf = time.perf_counter()
        result_bf = problem.solve_brute_force()
        end_time_bf = time.perf_counter()

        start_time_bs = time.perf_counter()
        result_bs = problem.solve_binary_search()
        end_time_bs = time.perf_counter()

        start_time_ba = time.perf_counter()
        result_ba = problem.solve_best_algorithm()
        end_time_ba = time.perf_counter()

        logs.save_log("triplets", result_bf, result_bs, result_ba)
        
        running_time_bf = end_time_bf - start_time_bf
        running_time_bs = end_time_bs - start_time_bs
        running_time_ba = end_time_ba - start_time_ba
        
        logs.save_log("running-times", running_time_bf, running_time_bs, running_time_ba)

    logs.export(r, n)
