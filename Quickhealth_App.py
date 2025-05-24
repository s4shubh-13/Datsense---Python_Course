import time

print("🩺 QuickHealth Pro Max - Python Project 2")
print("-" * 100)

# take personal inputs from user
user_name = input("What is your name: ").strip()
user_age = int(input("What is your age: "))
user_gender = input("What is your gender (Male/Female/other) : ").strip()
user_city = input("Which city do you live in : ").strip()

# take health inputs from user
main_symptom = input("Enter the symptoms you have. Choose from below : \nFever, Cough, Fatigue, Headache, Chest pain, Breathlessness : ").strip()
body_temp = int(input("What is your body temperature in Fahrenheit : "))
num_sick_days = int(input("From how many days are you sick : "))
smoking_habit = input("Do you smoke? (Yes/No) : ").strip()
sleep_hours = int(input("How many hours of sleep do you take : "))
pre_ex_condition = input("Do you have any Pre-existing conditions (yes/no) : ").strip()
mood = input("How is your mood now (calm , sad, anxious, irritable): ").strip()

print("Analysing your health score.....")
time.sleep(3)
print("-" * 100)
# risk scoring
points = 0
if body_temp >= 102 or num_sick_days > 3:
    points += 3
if user_age > 60 and  main_symptom == "Fever":
    points += 2
if num_sick_days >= 5 and main_symptom == "Cough":
    points += 2
if user_age > 30 and main_symptom == "Fatigue":
    points += 2
if body_temp > 100 and main_symptom == "Headache":
    points += 2
if main_symptom == "Chest pain":
    points += 3
if main_symptom == "Breathlessness":
    points += 4
if smoking_habit == "Yes":
    points += 2
if sleep_hours < 6:
    points += 1
if mood in ["anxious", "sad", "irritable"]:
    points += 1
if pre_ex_condition == "Yes":
    points += 2

# health risk result
health_risk = ''
if 0 <= points <= 3:
    health_risk = "🟢 Low Risk"
elif 4 <= points <= 6:
    health_risk = "🟠 Moderate Risk"
else:
    health_risk = "🔴 High Risk"

print(f"Your health is at : {health_risk}")
print("-" * 100)
# give user personalized Advice
if user_gender == "Female" and  user_age >= 45:
    print("You should get a health screening done.")
if user_gender == "Male" and smoking_habit == "Yes":
    print("You should quit smoking")
if sleep_hours < 6:
    print("Try to get at least 6-8 hours of sleep each night.")
if mood == "anxious":
    print("Practice relaxation or deep breathing exercises to reduce anxiety.")
if pre_ex_condition == "Yes":
    print("Please consult a medical professional regarding your pre-existing conditions.")

print(f'For any urgent concerns, visit the nearest urgent care center in {user_city}')
print("-" * 100)
# mental health tip
if mood == 'calm':
    print("Keep up the positivity! Staying calm helps your overall well-being.")
elif mood == 'sad':
    print("Consider talking to a friend or a mental health professional")
elif mood == 'anxious':
    print("Try box breathing: inhale for 4s, hold for 4s, exhale for 4s, hold again for 4s.")
elif mood == 'irritable':
    print("Take a short break or a walk")
print("-" * 100)