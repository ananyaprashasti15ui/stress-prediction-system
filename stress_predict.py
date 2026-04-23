# ==========================================
#  STRESSPREDICT: Intelligent Stress Analyzer
# ==========================================

import matplotlib.pyplot as plt


def get_user_input():
    print("\n🧠 Hello! Let's understand how you're feeling today.")
    print("Please answer honestly (0 = No, 1 = Sometimes, 2 = Often)\n")

    questions = [
        "1. Do you feel mentally overwhelmed?",
        "2. How would you rate your sleep quality?",
        "3. Do you feel anxious or restless?",
        "4. Are you dealing with heavy workload or pressure?",
        "5. Do you feel physically or mentally tired?",
        "6. Do you find it hard to concentrate?",
        "7. Do you feel emotionally drained?",
        "8. Do you take enough breaks or relaxation time?"
    ]

    answers = []

    for q in questions:
        while True:
            try:
                ans = int(input(q + " (0-2): "))
                if ans in [0, 1, 2]:
                    answers.append(ans)
                    break
                else:
                    print("Please enter 0, 1, or 2.")
            except:
                print("Invalid input. Try again.")

    return answers


def calculate_score(answers):
    # Weighted scoring (novelty)
    weights = [3, 4, 3, 4, 2, 2, 3, -2]  # breaks reduce stress

    score = 0
    for i in range(len(answers)):
        score += answers[i] * weights[i]

    return score


def classify_stress(score):
    if score <= 8:
        return "Low"
    elif score <= 18:
        return "Moderate"
    else:
        return "High"


def explain_stress(answers):
    reasons = []

    if answers[1] == 0:
        reasons.append("poor sleep quality")
    if answers[3] == 2:
        reasons.append("high workload pressure")
    if answers[2] == 2:
        reasons.append("increased anxiety levels")
    if answers[5] == 2:
        reasons.append("lack of concentration")
    if answers[6] == 2:
        reasons.append("emotional exhaustion")

    return reasons


def give_feedback(level, reasons):
    print("\n🧠 Analysis Result:\n")

    if level == "Low":
        print("You're doing quite well. Your stress levels appear to be low.")
    elif level == "Moderate":
        print("You are experiencing a moderate level of stress.")
    else:
        print("It seems like you're experiencing high stress.")

    if reasons:
        print("\n🔍 Key Factors:")
        for r in reasons:
            print("-", r)

    print("\n💡 Suggestions:")

    if level == "High":
        print("- Take proper rest")
        print("- Try meditation or breathing exercises")
        print("- Reduce workload")
        print("- Talk to someone you trust")
    elif level == "Moderate":
        print("- Take regular breaks")
        print("- Improve sleep schedule")
    else:
        print("- Maintain your current healthy routine")

    print("\n⚠️ This is not a medical diagnosis.\n")


def show_graph(answers):
    labels = [
        "Stress", "Sleep", "Anxiety", "Workload",
        "Fatigue", "Focus", "Emotion", "Breaks"
    ]

    colors = ['red' if x == 2 else 'orange' if x == 1 else 'green' for x in answers]

    plt.figure(figsize=(10, 5))
    plt.bar(labels, answers, color=colors)

    plt.title("Stress Factor Visualization")
    plt.xlabel("Factors")
    plt.ylabel("Intensity (0-2)")
    plt.xticks(rotation=30)

    plt.tight_layout()
    plt.show()


def main():
    answers = get_user_input()
    score = calculate_score(answers)
    level = classify_stress(score)
    reasons = explain_stress(answers)

    give_feedback(level, reasons)

    print(f"📊 Stress Score: {score}")
    print(f"📌 Stress Level: {level}")

    show_graph(answers)


main()
