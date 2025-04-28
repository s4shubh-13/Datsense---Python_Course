import time

print("🧠 Know Your Personality")  # heading
print("✨ Let's discover who you really are with some fun data magic!")  # caption
print("-" * 100)    # separator line

print("📝 Enter Your Details")

user_name = input("👤 Your Name : ")
user_age = input("🎂 Your Age : ")
user_city = input("🏙️ City You Live In :")
user_fav_food = input("🍕 Your Favorite Food : ")
user_fav_color = input("🎨 Your Favorite Color : ")
user_animal = input("🐾 Your Spirit Animal : ")
user_interest = input("🎮 One Thing You LOVE Doing : ")

print("-" * 100)    # separator line

# calculate personality code
personality_code = user_name[:2].upper() + user_age[-1] + user_animal[0].upper() + user_fav_color[0].lower()

# get age title
user_age = int(user_age)
if user_age < 18:
    age_title = "Young Explorer"
elif 18 <= user_age <= 30:
    age_title = "Adventurer"
else:
    age_title = "Wise Owl"
 

print("🔍 Scanning colors, foods, and animal energies...")
time.sleep(3)
print("💫 Calculating your personality type using complex non-scientific logic...")
time.sleep(3)
print(f"🎉 Hey {user_name}, here's your fun personality report!")

print("-" * 100)    # separator line

print(f"🌆 You're from {user_city}, a place of dreams!")
print(f"🍿 You love {user_fav_food} and enjoy doing {user_interest}.")
print(f"🎨 You vibe with the color {user_fav_color.upper()} and your spirit animal is the {user_animal}.")
print(f"📅 You've lived approximately {user_age * 12} months already.")
print(f"🧩 You belong to the '{age_title}' tribe.")
print(f"🔐 Your Secret Personality Code is: 💡 {personality_code}")

print("-" * 100)    # separator line

hobby_len = len(user_interest)
if hobby_len < 5:
    print("🎯 Short and sweet! Sometimes little things bring the most joy.")
    certification = "VIBES MASTER"
elif 5 <= hobby_len <= 10:
    print("🌟 That's a cool hobby! It sounds interesting and fun.")
    certification = "PASSION MAVERICK"
else:
    print("✨ You seem deeply passionate — that hobby says a lot about your vibe!")
    certification = "FUNKY AND FABULOUS"

print(f"🌈 You are officially certified as: {certification}")
