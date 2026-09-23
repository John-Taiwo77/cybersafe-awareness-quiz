def ask_question(number, item):
    print(f"\nQuestion {number}: {item['question']}")
    print(f"Category: {item['category']}")
    for i, option in enumerate(item["options"], 1):
        print(f"{i}. {option}")
    while True:
        answer = input("Choose an option (1-4): ").strip()
        if answer in "1234" and len(answer) == 1:
            return int(answer) == item["correct"]
        print("Please enter 1, 2, 3, or 4.")

def feedback(score, total):
    percent = score / total * 100
    if percent == 100:
        return "Excellent! Every answer was correct."
    if percent >= 70:
        return "Great work! You have a strong foundation."
    if percent >= 50:
        return "Good effort. Review the questions you missed."
    return "Keep practicing and learning about cybersecurity."

def run_quiz():
    questions = [
        {"category":"Phishing","question":"What is safest when you receive a suspicious link?","options":["Open it","Share it","Verify the sender and avoid opening it","Enter your password"],"correct":3},
        {"category":"Passwords","question":"Which password is generally stronger?","options":["password123","John2008","12345678","A long, unique passphrase"],"correct":4},
        {"category":"Phishing","question":"What does phishing usually try to do?","options":["Improve speed","Trick people into sharing sensitive information","Repair a computer","Create a backup"],"correct":2},
        {"category":"Account Security","question":"What is one benefit of multi-factor authentication?","options":["It adds another verification step","It removes all passwords","It makes websites faster","It prevents every attack"],"correct":1},
        {"category":"Updates","question":"Why should software be updated?","options":["Change wallpaper","Increase adverts","Receive fixes and security improvements","Delete files"],"correct":3},
        {"category":"Privacy","question":"Which information should you avoid sharing publicly?","options":["Favorite color","Account password","General hobby","School subject"],"correct":2},
        {"category":"Backups","question":"Why are backups useful?","options":["They help recover important files","They stop every attack","They remove passwords","They automatically remove every virus"],"correct":1},
        {"category":"Social Engineering","question":"What is social engineering?","options":["Designing a logo","Using manipulation to trick people","Installing a printer","Improving Wi-Fi"],"correct":2},
    ]
    while True:
        score = 0
        print("\n=== CyberSafe Awareness Quiz ===")
        for number, item in enumerate(questions, 1):
            if ask_question(number, item):
                print("Correct!")
                score += 1
            else:
                print("Not quite. Keep learning!")
        total = len(questions)
        print(f"\nFinal score: {score}/{total} ({score/total*100:.0f}%)")
        print(feedback(score, total))
        if input("\nPlay again? (y/n): ").strip().lower() != "y":
            print("Thank you for using CyberSafe Quiz. Stay safe online!")
            break

if __name__ == "__main__":
    run_quiz()
