# Exercise 1: Variables
name = "Parag"
experience = 5
print(name)
print(experience + 1)

# Exercise 2: Lists
skills = ["linux", "docker", "kubernetes"]
print(skills[0])
print(len(skills))
skills.append("ansible")
print(skills)

# Exercise 3: Dictionaries
model = {
    "name": "random_forest",
    "accuracy": 0.89,
    "trained": True
}
print(model["name"])
print(model["accuracy"])
model["speed"] = "fast"
print(model)

# Exercise 4: Loops
scores = [0.91, 0.87, 0.94, 0.76, 0.88]
for score in scores:
    if score > 0.90:
        print(score, "- excellent!")

# Exercise 5: Functions
def is_passing(score):
    if score >= 0.60:
        return True
    return False

print(is_passing(75))
print(is_passing(45))

# Exercise 6: Everything together
def is_passing_model(score):
    if score >= 0.60:
        return True
    return False

model_scores = [0.91, 0.45, 0.87, 0.55, 0.94]
for score in model_scores:
    print(score, is_passing_model(score))
