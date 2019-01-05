import sys
from collections import defaultdict
from datetime import datetime

records = open(sys.argv[1],'r').readlines()
records = sorted(records, 
        key=lambda record: datetime.strptime(record.split('] ')[0],'[%Y-%m-%d %H:%M'))
times = [datetime.strptime(record.split('] ')[0], '[%Y-%m-%d %H:%M') for record in records]
records = [record.split() for record in records]

def get_guard_sleeping_schedule():
	i, n = 0, len(records)
	guards_schedule = defaultdict(list)
	curr_guard, curr_guard_minutes_asleep, last_sleep_time = None, None, None
	while i < n:
		if records[i][2].startswith('Guard'):
			if curr_guard:
				guards_schedule[curr_guard].append(curr_guard_minutes_asleep)
			curr_guard = records[i][3][1:]
			curr_guard_minutes_asleep = [0] * 60
		elif records[i][2].startswith('falls'):
			last_sleep_time = times[i].minute
		elif records[i][2].startswith('wakes'):
			for j in range(last_sleep_time, times[i].minute):
				curr_guard_minutes_asleep[j] = 1
		i += 1
	
	guards_schedule[curr_guard].append(curr_guard_minutes_asleep)
	return guards_schedule

def get_highest_sleeping_frequency(schedules, guard):
	highest_sleep_freq_at_minute = -1
	minute_with_highest_sleep_freq = -1

	for m in range(60):
		sleep_freq_at_minute = 0
		for schedule in schedules[guard]:
			sleep_freq_at_minute += schedule[m]
		if sleep_freq_at_minute > highest_sleep_freq_at_minute:
			highest_sleep_freq_at_minute = sleep_freq_at_minute
			minute_with_highest_sleep_freq = m

	return (highest_sleep_freq_at_minute, minute_with_highest_sleep_freq)

def part1():
	schedules = get_guard_sleeping_schedule()
	guard_asleep_longest, longest_time_asleep = None, 0
	
	for guard in schedules:
		total_minutes_asleep = 0
		for l in schedules[guard]:
			total_minutes_asleep += sum(l)
		if total_minutes_asleep > longest_time_asleep:
			longest_time_asleep, guard_asleep_longest = total_minutes_asleep, guard
		#print('Guard: {}, Total minutes asleep: {}'.format(guard, total_minutes_asleep)) 
	
	_, minute_with_highest_sleep_freq = get_highest_sleeping_frequency(schedules, guard_asleep_longest)
	return int(guard_asleep_longest) * minute_with_highest_sleep_freq

def part2():
	schedules = get_guard_sleeping_schedule()
	
	best_guard, best_guard_freq, best_minute = -1, -1, -1
	for guard in schedules:
		frequency, minute = get_highest_sleeping_frequency(schedules, guard)
		if frequency > best_guard_freq:
			best_guard_freq = frequency
			best_guard = guard
			best_minute = minute
			
	return int(best_guard) * best_minute

print(part1())
print(part2())
