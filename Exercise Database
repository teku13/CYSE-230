class Exercise:
    def __init__(self, name, category, description, equipment, muscles_worked):
        self.name = name
        self.category = category
        self.description = description
        self.equipment = equipment
        self.muscles_worked = muscles_worked

class ExerciseDatabase:
    def __init__(self):
        self.exercises = []

    def add_exercise(self, exercise):
        self.exercises.append(exercise)

    def get_exercise_by_name(self, name):
        for exercise in self.exercises:
            if exercise.name == name:
                return exercise
        return None

# Crossfit exercises
crossfit_exercises = [
    Exercise(
        "Burpees",
        "Crossfit",
        "A full-body exercise that involves a squat, a jump, and a push-up.",
        "None",
        ["Legs", "Chest", "Arms"]
    ),
    Exercise(
        "Wall Ball Shots",
        "Crossfit",
        "A movement where you squat down and then throw a medicine ball up to a target on the wall.",
        "Medicine Ball",
        ["Legs", "Shoulders", "Core"]
    ),
    Exercise(
        "Box Jumps",
        "Crossfit",
        "A movement where you jump up onto a box.",
        "Box",
        ["Legs", "Core"]
    ),
    Exercise(
        "Double Unders",
        "Crossfit",
        "A jump rope exercise where the rope passes under your feet twice in one jump.",
        "Jump Rope",
        ["Legs", "Shoulders", "Arms"]
    )
]

# Bodybuilding exercises
bodybuilding_exercises = [
    Exercise(
        "Bench Press",
        "Bodybuilding",
        "A chest exercise where you lie on a bench and push a barbell up and down.",
        "Barbell",
        ["Chest", "Triceps", "Shoulders"]
    ),
    Exercise(
        "Bicep Curls",
        "Bodybuilding",
        "An arm exercise where you lift a dumbbell from your side up to your shoulder.",
        "Dumbbell",
        ["Biceps"]
    ),
    Exercise(
        "Leg Press",
        "Bodybuilding",
        "A leg exercise where you push a weight up and down with your legs.",
        "Leg Press Machine",
        ["Legs", "Glutes"]
    ),
    Exercise(
        "Seated Row",
        "Bodybuilding",
        "A back exercise where you pull a handle towards your chest while seated.",
        "Cable Machine",
        ["Back", "Biceps"]
    )
]

# Powerlifting exercises
powerlifting_exercises = [
    Exercise(
        "Squat",
        "Powerlifting",
        "A leg exercise where you lift a barbell on your shoulders and squat down and up.",
        "Barbell",
        ["Legs", "Glutes", "Core"]
    ),
    Exercise(
        "Deadlift",
        "Powerlifting",
        "A full-body exercise where you lift a barbell from the ground to standing position.",
        "Barbell",
        ["Legs", "Back", "Core"]
    ),
    Exercise(
        "Bench Press",
        "Powerlifting",
        "A chest exercise where you lie on a bench and push a barbell up and down.",
        "Barbell",
        ["Chest", "Triceps", "Shoulders"]
    ),
    Exercise(
        "Overhead Press",
