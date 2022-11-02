
import psutil
p = psutil.Process()
with p.oneshot():
     print(p.name())  # execute internal routine once collecting multiple info
     print(p.cpu_times())  # return cached value
     print(p.cpu_percent())  # return cached value
     print(p.create_time())  # return cached value
     print(p.ppid())  # return cached value
     print(p.status())  # return cached value