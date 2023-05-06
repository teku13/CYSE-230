import sys
import difflib
from PySide6 import QtWidgets

class WorkoutGenerator(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Workout Generator")

        # Create central widget and grid layout
        central_widget = QtWidgets.QWidget()
        grid_layout = QtWidgets.QGridLayout(central_widget)

        # Create string variables to hold the user's input for goal, level, and days
        self.goal_var = QtWidgets.QLineEdit()
        self.level_var = QtWidgets.QComboBox()
        self.level_var.addItems(["Beginner", "Intermediate", "Athlete"])
        self.days_var = QtWidgets.QSpinBox()

        # Create labels for the user to input their goal, level, and days
        label1 = QtWidgets.QLabel("What is your fitness goal?")
        label2 = QtWidgets.QLabel("What level are you?")
        label3 = QtWidgets.QLabel("How many days do you want to workout?")

        # Create a button that will generate the workout plan when clicked
        generate_button = QtWidgets.QPushButton("Generate workout plan")
        generate_button.clicked.connect(self.generate_workout)

        # Create a text box to display the generated workout plan
        self.workout_plan_display = QtWidgets.QTextEdit(self)
        

        # Add widgets to the grid layout
        grid_layout.addWidget(label1, 0, 0)
        grid_layout.addWidget(self.goal_var, 0, 1)
        grid_layout.addWidget(label2, 1, 0)
        grid_layout.addWidget(self.level_var, 1, 1)
        grid_layout.addWidget(label3, 2, 0)
        grid_layout.addWidget(self.days_var, 2, 1)
        grid_layout.addWidget(generate_button, 3, 0, 1, 2)
        grid_layout.addWidget(self.workout_plan_display, 4, 0, 1, 2)

        # Set the central widget of the main window
        self.setCentralWidget(central_widget)

    def get_workout_plan(self, goal, level, days):
        # Define a dictionary of workout plans for each goal and level
        workouts = {
            "Bodybuilding": {
                "Beginner": [
                    {"name": "Full Body A", "exercises": [
                        {"exercise": "Squat", "sets": 4, "reps": 8},
                        {"exercise": "Bench Press", "sets": 4, "reps": 8},
                        {"exercise": "Deadlift", "sets": 4, "reps": 6}
                    ]},
                    {"name": "Full Body B", "exercises": [
                        {"exercise": "Lunges", "sets": 3, "reps": 12},
                        {"exercise": "Pull-ups", "sets": 3, "reps": 8},
                        {"exercise": "Push-ups", "sets": 3, "reps": 12}
                    ]}
                ],
                "Intermediate": [
                    {"name": "Upper Body A", "exercises": [
                        {"exercise": "Bench Press", "sets": 4, "reps": 6},
                        {"exercise": "Bent Over Row", "sets": 4, "reps": 6},
                        {"exercise": "Shoulder Press", "sets": 3, "reps": 8}
                    ]},
                    {"name": "Lower Body A", "exercises": [
                        {"exercise": "Squat", "sets": 4, "reps": 6},
                        {"exercise": "Romanian Deadlift", "sets": 4, "reps": 6},
                        {"exercise": "Leg Curl", "sets": 3, "reps": 10}
                    ]}
                ],
                "Athlete": [
                    {"name": "Advanced Upper Body A", "exercises": [
                        {"exercise": "Incline Bench Press", "sets": 5, "reps": 5},
                        {"exercise": "Weighted Pull-ups", "sets": 5, "reps": 5},
                        {"exercise": "Arnold Press", "sets": 4, "reps": 8}
                    ]},
                    {"name": "Advanced Lower Body A", "exercises": [
                        {"exercise": "Front Squat", "sets": 5, "reps": 5},
                        {"exercise": "Snatch-Grip Deadlift", "sets": 5, "reps": 5},
                        {"exercise": "Glute-Ham Raise", "sets": 4, "reps": 8}
                    ]}
                ],
            },
            "Powerlifting": {
                "Beginner": [
                    {"name": "Powerlifting Full Body A", "exercises": [
                        {"exercise": "Squat", "sets": 5, "reps": 5},
                        {"exercise": "Bench Press", "sets": 5, "reps": 5},
                        {"exercise": "Deadlift", "sets": 1, "reps": 5}
                    ]},
                    {"name": "Powerlifting Full Body B", "exercises": [
                        {"exercise": "Squat", "sets": 5, "reps": 5},
                        {"exercise": "Overhead Press", "sets": 5, "reps": 5},
                        {"exercise": "Pendlay Row", "sets": 5, "reps": 5}
                    ]}
                ],
                "Intermediate": [
                    {"name": "Powerlifting Upper A", "exercises": [
                        {"exercise": "Bench Press", "sets": 5, "reps": 3},
                        {"exercise": "Close Grip Bench Press", "sets": 4, "reps": 6},
                        {"exercise": "Barbell Row", "sets": 4, "reps": 6}
                    ]},
                    {"name": "Powerlifting Lower A", "exercises": [
                        {"exercise": "Squat", "sets": 5, "reps": 3},
                        {"exercise": "Deadlift", "sets": 3, "reps": 3},
                        {"exercise": "Leg Press", "sets": 4, "reps": 8}
                    ]}
                ],
                "Athlete": [
                    {"name": "Powerlifting Upper B", "exercises": [
                        {"exercise": "Paused Bench Press", "sets": 6, "reps": 2},
                        {"exercise": "Weighted Chin-ups", "sets": 4, "reps": 4},
                        {"exercise": "Seated Military Press", "sets": 4, "reps": 6}
                    ]},
                    {"name": "Powerlifting Lower B", "exercises": [
                        {"exercise": "Paused Squat", "sets": 6, "reps": 2},
                        {"exercise": "Sumo Deadlift", "sets": 3, "reps": 3},
                        {"exercise": "Walking Lunges", "sets": 3, "reps": 10}
                    ]}
                ],
            },
            "CrossFit": {
                "Beginner": [
                    {"name": "CrossFit WOD A", "exercises": [
                        {"exercise": "Wall Balls", "sets": 4, "reps": 15},
                        {"exercise": "Kettlebell Swings", "sets": 4, "reps": 15},
                        {"exercise": "Box Jumps", "sets": 4, "reps": 15}
                    ]},
                    {"name": "CrossFit WOD B", "exercises": [
                        {"exercise": "Double-Unders", "sets": 5, "reps": 30},
                        {"exercise": "Push-ups", "sets": 5, "reps": 15},
                        {"exercise": "Sit-ups", "sets": 5, "reps": 15}
                    ]}
                ],
                "Intermediate": [
                    {"name": "CrossFit WOD C", "exercises": [
                        {"exercise": "Thrusters", "sets": 5, "reps": 10},
                        {"exercise": "Pull-ups", "sets": 5, "reps": 10},
                        {"exercise": "Burpees", "sets": 5, "reps": 10}
                    ]},
                    {"name": "CrossFit WOD D", "exercises": [
                        {"exercise": "Power Cleans", "sets": 5, "reps": 5},
                        {"exercise": "Handstand Push-ups", "sets": 5, "reps": 5},
                        {"exercise": "Toes-to-Bar", "sets": 5, "reps": 10}
                    ]}
                ],
                "Athlete": [
                    {"name": "CrossFit WOD E", "exercises": [
                        {"exercise": "Squat Snatch", "sets": 4, "reps": 4},
                        {"exercise": "Ring Muscle-ups", "sets": 4, "reps": 4},
                        {"exercise": "Pistols", "sets": 4, "reps": 8}
                    ]},
                    {"name": "CrossFit WOD F", "exercises": [
                        {"exercise": "Clean and Jerk", "sets": 5, "reps": 3},
                        {"exercise": "Bar Muscle-ups", "sets": 5, "reps": 3},
                        {"exercise": "GHD Sit-ups", "sets": 5, "reps": 10}
                    ]}
                ],
            }
        }            

        # Get the workout plan for the specified goal and level
        workout_schedule = workouts.get(goal, {}).get(level)
        if not workout_schedule:
            # Handle the case where the goal or level doesn't exist in the workouts dictionary
            return None

        # Repeat the workout plan for the specified number of days
        workout_plan = []
        for i in range(days):
            workout_plan.append(workout_schedule[i % len(workout_schedule)])

        return workout_plan

    def generate_workout(self):
    # Get the selected values from the dropdowns and spinbox
        days = self.days_var.value()
        goal = self.goal_var.text()
        level = self.level_var.currentText()
        
        # Clear previous output and display new output header
        self.workout_plan_display.setText("Your personalized workout plan is:\n")

        workout_plan = self.get_workout_plan(goal, level, days)
        for i, workout in enumerate(workout_plan, start=1):
            self.workout_plan_display.append(f"\nDay {i}: {workout['name']}\n")
            for exercise in workout['exercises']:
                self.workout_plan_display.append(f"  {exercise['exercise']}: {exercise['sets']} sets x {exercise['reps']} reps\n")

        return workout_plan
            
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    generator = WorkoutGenerator()
    generator.show()
    sys.exit(app.exec())
