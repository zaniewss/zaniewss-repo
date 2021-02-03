import sys, time

def delay_print(s):
	# Print one character at a time
	for c in s:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.05)


def storyNoble():
	delay_print('\nYou continue onto the path ahead.')