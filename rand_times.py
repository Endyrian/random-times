import random
import math

max_days = float(input('Please enter the maximum amount of days: '))
max_seconds = math.floor(max_days * 86400) #24*60*60=86400

times = [random.randint(1, max_seconds)]
while times[-1] > 1:
    times.append(random.randrange(times[-1]))

x = max(math.ceil(math.log10(times[0]/86400)), 1)
for seconds in times:
    minutes = seconds // 60
    hours = minutes // 60
    days = hours // 24
    print(str(days).zfill(x), "{:02d}".format(hours % 24), "{:02d}".format(minutes % 60), "{:02d}".format(seconds % 60), sep=':')
