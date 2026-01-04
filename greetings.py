pose_map = {"person1": "Hello Mom!", "person2": "Hey bestie!", "person3": "Welcome home, Dad!"}

detected_pose = input("Who is in front of the camera? (person1/person2/person3): ").lower()

if detected_pose in pose_map:
    print("AI Sprite:", pose_map[detected_pose])
else:
    print("AI Sprite: Hello there!")