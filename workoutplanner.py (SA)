import tkinter as tk
from tkinter import ttk

def get_workout_plan(goal, level, days):
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
        },
    }
    # Get the workout plan for the specified goal and level
    workout_schedule = workouts[goal][level]
    # Repeat the workout plan for the specified number of days
    return [workout_schedule[i % len(workout_schedule)] for i in range(days)]

def generate_workout():
    # Get user input for goal, level, and days
    goal = goal_var.get()
    level = level_var.get().capitalize()  # Update from .lower() to .capitalize()
    days = int(days_var.get())
    # Get workout plan based on user input
    workout_plan = get_workout_plan(goal, level, days)
    
    # Clear previous output and display new output header
    output.delete(1.0, tk.END)
    output.insert(tk.END, "Your personalized workout plan is:\n")
    
    # Loop through workout plan and display each workout for each day
    for i, workout in enumerate(workout_plan, start=1):
        output.insert(tk.END, f"\nDay {i}: {workout['name']}\n")
        for exercise in workout['exercises']:
            output.insert(tk.END, f"  {exercise['exercise']}: {exercise['sets']} sets x {exercise['reps']} reps\n")

# Create the main window of the application
app = tk.Tk()
app.title("Workout Generator")

# Create string variables to hold the user's input for goal, level, and days
goal_var = tk.StringVar()
level_var = tk.StringVar()
days_var = tk.StringVar()

# Create four frames to organize the user interface elements
frame1 = ttk.Frame(app)
frame1.grid(row=0, column=0, sticky="W")

frame2 = ttk.Frame(app)
frame2.grid(row=1, column=0, sticky="W")

frame3 = ttk.Frame(app)
frame3.grid(row=2, column=0, sticky="W")

frame4 = ttk.Frame(app)
frame4.grid(row=3, column=0, sticky="W")

# Create labels and input fields for the user to input their goal, level, and days
label1 = ttk.Label(frame1, text="What is your fitness goal?")
label1.pack(side="left")

goal_entry = ttk.Combobox(frame1, textvariable=goal_var, values=("Bodybuilding", "Powerlifting", "CrossFit"))
goal_entry.pack(side="left")

label2 = ttk.Label(frame2, text="What level are you?")
label2.pack(side="left")

level_entry = ttk.Combobox(frame2, textvariable=level_var, values=("Beginner", "Intermediate", "Athlete"))
level_entry.pack(side="left")

label3 = ttk.Label(frame3, text="How many days do you want to workout?")
label3.pack(side="left")

days_entry = ttk.Entry(frame3, textvariable=days_var)
days_entry.pack(side="left")

# Create a button that will generate the workout plan when clicked
generate_button = ttk.Button(frame4, text="Generate workout plan", command=generate_workout)
generate_button.pack(side="left")

# Create a text box to display the generated workout plan
output = tk.Text(app, wrap="word", width=50, height=20)
output.grid(row=4, column=0, pady=10)

# Start the main loop of the application
app.mainloop()
