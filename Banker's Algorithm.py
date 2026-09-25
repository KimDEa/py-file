#Banker's Algorithm

import time
import copy

class Banker:
    def __init__(self):
        self.num_processes = 3
        self.num_resources = [3, 3, 2]
        self.max_need = [[7, 5, 3], [3, 2, 2], [9, 0, 2]]
        #Unsafe.
        self.allocation_unsafe = [[0, 1, 0], [2, 0, 0], [3, 0, 2]]
        self.need_unsafe = [[1, 2, 2], [1, 2, 2], [6, 0, 0]]
        #Passed.
        self.allocation_safe = [[0, 1, 0], [2, 0, 0], [3, 0, 2]]
        self.need_safe = [[1, 2, 2], [1, 2, 2], [5, 0, 0]]
        #Failed.
        self.allocation_failed = [[0, 1, 0]]
        self.need_failed = []

    def inspect(self):
        t_allocation = copy.deepcopy(self.allocation_safe)
        t_need = copy.deepcopy(self.need_safe)
        t_resources = self.num_resources.copy()

        count_total = self.num_processes
        count = 2
        fail_count = 0
        n = 0
        m = 0

        while count_total != 0:
            self.num_processes = len(t_need)
            if len(t_need) == 0 and count_total != 0:
                print("results: Failed.")
                return
            
            if fail_count == count_total:
                print("results: Unsafe.")
                return
            
            tt_allocation = t_allocation[n]
            tt_need = t_need[n]

            if t_resources[m] >= tt_need[m]:
                count -= 1
                m += 1
                print(
                    f"system available: {t_resources}\n",
                    f"P{n}: needs - {tt_need}, allocation - {tt_allocation}"
                )
                time.sleep(2)
                if m == len(t_resources):
                    count_total -= 1
                    for i in range(len(t_resources)):
                        t_resources[i] += tt_allocation[i]
                    t_need.pop(0)
                    t_allocation.pop(0)
                    fail_count = 0
                    n = 0
                    m = 0
                    print(
                        f"system resources: {t_resources}\n",
                        f"P{m}: need - {tt_need}, allocation - {tt_allocation}, status - Passed."
                    )
                    time.sleep(2)
                    continue
                else:
                    continue
            else:
                t_allocation.append(t_allocation.pop(0))
                t_need.append(t_need.pop(0))
                count = 2
                fail_count += 1
                n = 0
                m = 0
                print(
                    f"system resources: {t_resources}\n",
                    f"P{n}: need - {tt_need}, allocation - {tt_allocation}"
                )
                time.sleep(2)
                continue

        print("results: Safe.")

if __name__ == "__main__":
    b = Banker()
    b.inspect()