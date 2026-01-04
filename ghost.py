ghost_y = 0
sound = input("Sound detected (upward clap / downward clap): ").lower()

if sound == "upward clap":
    ghost_y += 10
    print("Ghost moves UP to:", ghost_y)
elif sound == "downward clap":
    ghost_y -= 10
    print("Ghost moves DOWN to:", ghost_y)