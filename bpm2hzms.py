"""
BPM to Hz / ms Calculator
Developed by Icaro Ferre
06/30/2016
"""

# ========= FUNCTIONS / MULT LIST ================

# List of Multiplications / Divisions

multvalues = [32, 16, 8, 4, 2, 1, 0.5, 0.25, 0.125, 0.0625, .03125]
multnames = ["32 bars", "16 bars", "8 bars", "4 bars", "2 bars", "1 bar", "1/2 beat", "1/4 beat", "1/8 beat", "1/16 beat", "1/32 beat"]


# Round number to 3 decimal points - Returns string!
def roundNum(n):
	n = round(n, 4)
	return n

# Hz Conversion
def hz(bpm):
	for i in range(len(multvalues)):
		calculatedValue = (bpm/60.0) * 0.25 / multvalues[i] 
		print multnames[i] + ": %sHz" % roundNum(calculatedValue)


# ms Conversion
def ms(bpm):
	for i in range(len(multvalues)):
		calculatedValue = (60.0/bpm) * multvalues[i] * 4
		print multnames[i] + ": %sms" % roundNum(calculatedValue)

#Validates BPM value
def validateBPM(bpm):
	valid = False
	while not valid:
		try:
			bpm = float(bpm)
			return bpm
			valid = True
		except ValueError:
			print "Invalid BPM"
			bpm = raw_input("Enter valid BPM: ")
			valid = False

#Validates Mode value
def validateMode(mode):
	while mode != "hz" and mode != "ms":
		print "Mode Invalid."
		mode = raw_input("Enter valid output mode (hz/ms):")
	else:
		return mode

# ============= INITIAL PRINT =================

print 
print "BPM to Hz / ms Calculator"
print "Created by Icaro Ferre"
print 

# ============== ASK FOR VALUES ===============

bpm = raw_input("Enter valid BPM: ")
bpm = validateBPM(bpm)

mode = raw_input("Enter output mode (hz/ms): ")
mode = validateMode(mode)
 

# ========= RETURN FINAL VALUES ==============

print 

if mode == "hz":
	hz(bpm)
elif mode == "ms":
	ms(bpm)

print 


