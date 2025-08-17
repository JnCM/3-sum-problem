class Log:
    def __init__(self):
        self.__logs = {
            "Brute-Force": {
                "inputs": [],
                "triplets": [],
                "running-times": []
            },
            "Binary-Search": {
                "inputs": [],
                "triplets": [],
                "running-times": []
            },
            "Best-Algorithm": {
                "inputs": [],
                "triplets": [],
                "running-times": []
            }
        }
    
    def save_log(self, param, value_bf, value_bs, value_ba):
        self.__logs["Brute-Force"][param].append(value_bf)
        self.__logs["Binary-Search"][param].append(value_bs)
        self.__logs["Binary-Search"][param].append(value_ba)
    
    def export(self, r, n):
        for alg in self.__logs.keys():
            with open(f"results/{alg}_n{n}_r{r}.txt", "w") as file:
                file.write("----- 3-SUM Problem Solutions -----\n")
                file.write(f"Algorithm: {alg}\n")
                file.write(f"n = {n}\n")
                file.write(f"Number of executions: {r}\n")
                avg_running_time = sum(self.__logs[alg]["running-times"]) / len(self.__logs[alg]["running-times"])
                file.write(f"Average running time: {avg_running_time}\n\n")
                file.write("----- Detailed Solutions -----\n")
                for i in range(r):
                    file.write(f"Execution {i+1}\n")
                    file.write(f"Inputs: {self.__logs[alg]["inputs"][i]}\n")
                    file.write(f"Triplets: {self.__logs[alg]["triplets"][i]}\n")
                    file.write(f"Running time: {self.__logs[alg]["running-times"][i]}\n")
                    file.write("---------------\n")
        
        print("Results saved in `results` folder...")
