
detection_map = {"smile": "Happy Face", "wink": "Cool Face", "heart": "Love Face"}

detected_feature = input("Enter detected feature: ").lower()

if detected_feature in detection_map:
    print("Emoji recognized as:", detection_map[detected_feature])
else:
    print("No emoji detected.")