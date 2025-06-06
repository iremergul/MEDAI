import datetime
import random


class HealthAssistant:
    def __init__(self, name):
        self.name = name
        self.health_data = {
            "heart_rate": [],
            "blood_pressure": [],
            "weight": [],
            "height": [],
            "exercise": [],
            "medications": {},
        }

    def record_health_data(self, data_type, value):
        if data_type in self.health_data:
            self.health_data[data_type].append((datetime.datetime.now(), value))
            print(f"{data_type} data successfully recorded.")
            if data_type == "heart_rate":
                self.heart_rate_alert(float(value))
            elif data_type == "blood_pressure":
                self.blood_pressure_alert(value)
            elif data_type == "weight":
                self.weight(value)
            elif data_type == "height":
                self.height(value)
            elif data_type == "exercise":
                self.exercise_and_diet_recommendation()
            else:
                print("Invalid health data type.")

    def heart_rate_alert(self, heart_rate):
        if heart_rate < 60:
            print(
                "Attention! Your heart rate is below normal. Try to exercise regularly."
            )
        elif 60 < heart_rate <= 100:
            print("Your heart rate is at a normal level.")
        else:
            print(
                "Attention! Your heart rate is above normal. Try to rest and reduce stress."
            )

    def weight(self, weight):
        self.health_data["weight"].append((datetime.datetime.now(), weight))
        print(f"{weight} weight successfully recorded.")

    def height(self, height):
        self.health_data["height"].append((datetime.datetime.now(), height))
        print(f"{height} height successfully recorded.")

    def exercise_and_diet_recommendation(self):
        if "weight" not in self.health_data or "height" not in self.health_data:
            print(
                "Exercise and diet recommendation couldn't be calculated: Height and weight information is missing."
            )
            return

        if not self.health_data["weight"] or not self.health_data["height"]:
            print(
                "Exercise and diet recommendation couldn't be calculated: Height or weight information is missing."
            )
            return

        weight = float(self.health_data["weight"][-1][1])
        height = float(self.health_data["height"][-1][1])
        body_mass_index = weight / ((height / 100) ** 2)

        if body_mass_index < 18.5:
            print(
                "Attention! Your body mass index is below normal. Review your diet for more carbohydrates and protein intake."
            )
            print(
                "Exercise recommendation: Increase muscle mass by doing weight training and resistance exercises."
            )
        elif body_mass_index >= 25:
            print(
                "Attention! Your body mass index is above normal. Consume more fruits, vegetables, and high-fiber foods."
            )
            print(
                "Exercise recommendation: Increase calorie burn by doing cardio activities (running, walking, cycling)."
            )
        else:
            print(
                "Great! Your body mass index is within the normal range. Keep up with healthy eating and regular exercise."
            )

    def blood_pressure_alert(self, blood_pressure):
        blood_pressure_values = blood_pressure.split("/")
        systolic = int(blood_pressure_values[0])
        diastolic = int(blood_pressure_values[1])
        if systolic < 90 or diastolic < 60:
            print(
                "Attention! Your blood pressure is below normal. Be careful to drink plenty of water and increase salt intake."
            )
        elif systolic > 140 or diastolic > 90:
            print(
                "Attention! Your blood pressure is above normal. Follow a low-sodium and low-fat diet."
            )

    def add_medication(self, medication_name, dosage, frequency):
        self.health_data["medications"][medication_name] = {
            "dosage": dosage,
            "frequency": frequency,
        }
        print(f"{medication_name} medication successfully added.")

    def medication_reminder(self):
        current_time = datetime.datetime.now().time()
        for medication, info in self.health_data["medications"].items():
            dosage, frequency = info["dosage"], info["frequency"]
            if current_time.hour % frequency == 0 and current_time.minute == 0:
                print(f"{dosage} dose {medication} is due!")
        print("Medication reminder updated.")

    def create_diet_plan(self, target_weight):
        diet_plan = {
            "Breakfast": ["Egg", "Whole wheat bread", "Tomato", "Green tea"],
            "Mid-morning snack": ["Yogurt", "Fruit", "Almonds"],
            "Lunch": ["Grilled chicken", "Brown rice", "Broccoli", "Water"],
            "Afternoon snack": ["Carrot", "Fruit slices", "Bulgur pilav"],
            "Dinner": ["Fish", "Salad", "Bulgur with olive oil", "Water"],
        }
        print("Your diet plan has been successfully created.")
        return diet_plan


# Example Usage:
name = input("Please enter your name: ")
assistant = HealthAssistant(name)

# Record health data
print("\n--- Health Data ---")
for data in ["heart_rate", "blood_pressure", "weight", "height", "exercise"]:
    value = input(f"Enter {data}: ")
    assistant.record_health_data(data, value)


class Food:
    def __init__(self, name, calorie, protein, carbohydrate, fat):
        self.name = name
        self.calorie = calorie
        self.protein = protein
        self.carbohydrate = carbohydrate
        self.fat = fat


def average_individual_protein_sources():
    return [
        Food("lentils", 116, 25, 60, 2),
        Food("chicken breast", 200, 30, 0, 5),
        Food("yogurt", 150, 4, 5, 4),
        Food("egg", 150, 6, 0.6, 5),
        Food("salmon", 206, 24, 0, 14),
    ]


def average_individual_carbohydrate_sources():
    return [
        Food("whole wheat bread", 70, 3, 15, 0.5),
        Food("rice", 130, 2, 28, 0.2),
        Food("pasta", 130, 10, 25, 1),
        Food("potato", 70, 1, 15, 0),
        Food("bulgur", 350, 12, 70, 1),
    ]


def average_individual_fat_sources():
    return [
        Food("coconut", 354, 3, 15, 34),
        Food("avocado", 160, 2, 9, 15),
        Food("almond", 580, 21, 22, 50),
        Food("walnut", 650, 15, 14, 65),
        Food("chia seeds", 490, 17, 42, 31),
    ]


def average_individual_vegetable_sources():
    return [
        Food("broccoli", 34, 2.8, 6.6, 0.4),
        Food("carrot", 41, 1, 10, 0.2),
        Food("spinach", 23, 3, 3.6, 0.4),
        Food("cucumber", 15, 0.6, 4, 0.2),
        Food("pepper", 31, 1, 6, 0.3),
    ]


def average_individual_fruit_sources():
    return [
        Food("apple", 52, 0.3, 14, 0.2),
        Food("banana", 89, 1, 23, 0.3),
        Food("orange", 47, 1, 12, 0.1),
        Food("strawberry", 32, 0.7, 7.7, 0.3),
        Food("melon", 28, 0.6, 6, 0.2),
    ]


def calculate_total_calories(food_list):
    total_calories = sum(food.calorie for food in food_list)
    return total_calories


def create_nutrition_plan(gender, desired_calories):
    if gender.lower() == "female":
        min_calories, max_calories = 1500, 2000
    elif gender.lower() == "male":
        min_calories, max_calories = 2000, 2500
    else:
        print("Invalid gender input! Please enter 'male' or 'female'.")
        return None

    if desired_calories < min_calories or desired_calories > max_calories:
        print(
            f"Daily calorie requirement should be between {min_calories} and {max_calories}."
        )
        return None

    protein_sources = average_individual_protein_sources()
    carbohydrate_sources = average_individual_carbohydrate_sources()
    fat_sources = average_individual_fat_sources()
    vegetable_sources = average_individual_vegetable_sources()
    fruit_sources = average_individual_fruit_sources()

    breakfast = (
        random.sample(protein_sources, 1)
        + random.sample(carbohydrate_sources, 1)
        + random.sample(fat_sources, 1)
        + random.sample(vegetable_sources, 1)
        + random.sample(fruit_sources, 1)
    )

    lunch = (
        random.sample(protein_sources, 1)
        + random.sample(carbohydrate_sources, 1)
        + random.sample(fat_sources, 1)
        + random.sample(vegetable_sources, 1)
        + random.sample(fruit_sources, 1)
    )

    dinner = (
        random.sample(protein_sources, 1)
        + random.sample(carbohydrate_sources, 1)
        + random.sample(fat_sources, 1)
        + random.sample(vegetable_sources, 1)
        + random.sample(fruit_sources, 1)
    )

    return breakfast, lunch, dinner


print("Program is starting...")

gender = input("Enter your gender (Male/Female): ").lower()
desired_calories = float(input("Enter your desired daily calorie amount: "))

breakfast, lunch, dinner = create_nutrition_plan(gender, desired_calories)

print("\nYour Daily Nutrition Plan:")
print("\nBreakfast:")
for food in breakfast:
    print(f"{food.name}: {food.calorie} calories")

print("\nLunch:")
for food in lunch:
    print(f"{food.name}: {food.calorie} calories")

print("\nDinner:")
for food in dinner:
    print(f"{food.name}: {food.calorie} calories")
