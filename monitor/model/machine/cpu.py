import psutil


class Cpu():
    def __init__(self):
        pass

    def info(self) -> dict:
        thread_count = psutil.cpu_count()
        core_count = psutil.cpu_count(logical=False)

        list_cpu_percent: list = psutil.cpu_percent(interval=1, percpu=True)

        sum = 0
        for value in list_cpu_percent:
            sum += value
        cpu_percent_mean = sum/thread_count

        result = {"core_count": core_count,
                  "thread_count": thread_count,
                  "percent_mean": cpu_percent_mean,
                  "percent_for_thread": list_cpu_percent}

        return result


if __name__ == "__main__":
    cp = Cpu()
    print(cp.info())
