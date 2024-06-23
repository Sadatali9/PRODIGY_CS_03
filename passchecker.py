import tkinter as tk
import re

def assess_password_strength(password):
    strength_criteria = {
        "length": len(password) >= 8,
        "uppercase": re.search(r'[A-Z]', password) is not None,
        "lowercase": re.search(r'[a-z]', password) is not None,
        "digit": re.search(r'[0-9]', password) is not None,
        "special": re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None,
    }
    
    score = sum(strength_criteria.values())
    strength = "Weak"
    
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    
    feedback = f"Password Strength: {strength}\n Score: {score/5*100}%\n\nCriteria:\n"
    feedback += "\n".join([f"{criterion.capitalize()}: {'✓' if passed else '✗'}" 
                           for criterion, passed in strength_criteria.items()])
    
    return feedback

def evaluate_password():
    password = password_entry.get()
    feedback = assess_password_strength(password)
    result_label.config(text=feedback)

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")

# Create and place the widgets
tk.Label(root, text="Enter Password:").grid(row=0, column=0, padx=10, pady=10)

password_entry = tk.Entry(root, show='*', width=30)
password_entry.grid(row=0, column=1, padx=10, pady=10)

check_button = tk.Button(root, text="Check Strength", command=evaluate_password)
check_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="", justify="left")
result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Start the main loop
root.mainloop()
