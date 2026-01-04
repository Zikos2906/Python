heart_rate = int(input("Enter Heartbeat (BPM): "))

breath_rate = heart_rate / 4

print("Estimated Breath Rate:", breath_rate)

if breath_rate > 20:
    print("Breathing fast")
elif breath_rate < 12:
    print("Breathing slow")
else:
    print("Normal breathing")