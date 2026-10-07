import time
import copy

class RR:

    def __init__(self):
        self.time_slice = 3
        self.current_time = 0
        self.queue_processes = {
            "P0": {
                "arrival": 0,  # 프로세스가 대기열에 들어온 시간.
                "burst": 3,  # 프로세스가 작업을 끝내는데 필요한 총 CPU 시간.
                "remaining": 3,  # 실행되면서 줄어드는 남은 CPU 시간.
                "waiting": 0,  # 프로세스가 CPU를 쓰지 못하고 큐에서 기다린 총 시간.
                "turnaround": 0  # 도착해서 최종 완료될 때까지 걸린 총 시간.(완료 시각 - 도착 시각)
            },
            "P1": {
                "arrival": 0,
                "burst": 2,
                "remaining": 2,
                "waiting": 0,
                "turnaround": 0
            },
            "P2": {
                "arrival": 0,
                "burst": 7,
                "remaining": 7,
                "waiting": 0,
                "turnaround": 0
            },
            "P3": {
                "arrival": 0,
                "burst": 5,
                "remaining": 5,
                "waiting": 0,
                "turnaround": 0
            }
        }

    def test(self):

        order = 0
        queue_processes_copy = copy.deepcopy(self.queue_processes)

        while queue_processes_copy:

            current_key = list(queue_processes_copy.keys())[0]
            order = int(current_key[1:])
            time_stamp = 0

            for t in range(queue_processes_copy[f"P{order}"]["remaining"]):
                if self.time_slice > time_stamp and queue_processes_copy[f"P{order}"]["remaining"] > 0:
                    queue_processes_copy[f"P{order}"]["remaining"] -= 1
                    self.current_time += 1
                    time_stamp += 1
                    print(f"P{order} executing... {self.time_slice}/{time_stamp}({queue_processes_copy[f'P{order}']['remaining']})")
                    time.sleep(2)
                if self.time_slice >= time_stamp and queue_processes_copy[f"P{order}"]["remaining"] == 0:
                    queue_processes_copy[f"P{order}"]["turnaround"] = self.current_time - queue_processes_copy[f"P{order}"]["arrival"]
                    queue_processes_copy[f"P{order}"]["waiting"] = queue_processes_copy[f"P{order}"]["turnaround"] - queue_processes_copy[f"P{order}"]["burst"]
                    pop_data = queue_processes_copy.pop(f"P{order}")
                    self.queue_processes[f"P{order}"] = pop_data
                    print(f"P{order} fully executed.")
                    time.sleep(2)
                    break
                if self.time_slice == time_stamp and queue_processes_copy[f"P{order}"]["remaining"] > 0:
                    pop_data = queue_processes_copy.pop(f"P{order}")
                    queue_processes_copy[f"P{order}"] = pop_data
                    print(f"P{order} time slice expired, moved to back of queue.")
                    time.sleep(1)
                    break

        print()
        print("all process sucessfully executed!\n")

        for i in range(len(self.queue_processes)):
            print(f"P{i}: {self.queue_processes[f'P{i}']}\n")


if __name__ == "__main__":
    r = RR()
    r.test()