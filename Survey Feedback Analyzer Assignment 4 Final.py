# Module End Assignment 4: Survey Feedback Analyzer

# Step 1: Preloaded feedback data
feedback_data = {
    "S_No": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Name": ["Ravi", "Meera", "Sam", "Anu", "Raj", "Divya", "Arjun", "Kiran", "Leela", "Nisha"],
    "Feedback": [
        "   Very GOOD Service!!!", "poor support,        not happy   ",
        "GREAT experience! will come again.", "okay     okay...",
        "   not    BAD", "Excellent care, excellent staff!",
        "good food and good ambience!", "Poor response and poor handling of issue",
        "Satisfied. But could be better.", "Good support... quick service."
    ],
    "Rating": [5, 2, 5, 3, 2, 5, 4, 1, 3, 4]
}

# Step 2: Add more feedbacks
def get_integer_input(prompt, minimum=None, maximum=None):
    while True:
        try:
            value = int(input(prompt))
            if minimum is not None and value < minimum:
                print(f"Enter a value of at least {minimum}.")
                continue
            if maximum is not None and value > maximum:
                print(f"Enter a value no greater than {maximum}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Enter a whole number.")

additional_count = get_integer_input("How many more feedbacks would you like to add? ", 0)
for _ in range(additional_count):
    print("\nEnter new feedback details:")
    name = input("Name: ").strip()
    while not name:
        print("Name cannot be empty.")
        name = input("Name: ").strip()
    comment = input("Written Feedback: ")
    rating = get_integer_input("Rating (1-5): ", 1, 5)

    feedback_data["S_No"].append(len(feedback_data["S_No"]) + 1)
    feedback_data["Name"].append(name)
    feedback_data["Feedback"].append(comment)
    feedback_data["Rating"].append(rating)

# Step 3: Clean feedback text
def clean_feedback(comment):
    for mark in [".", ",", "!", "?"]:
        comment = comment.replace(mark, "")
    return " ".join(comment.split()).strip().lower()

feedback_data["Feedback"] = [clean_feedback(x) for x in feedback_data["Feedback"]]

# Step 4: Count feedback entries containing a whole word
def count_word_in_feedbacks(word):
    target = word.lower().strip()
    total = 0
    for comment in feedback_data["Feedback"]:
        if target in comment.split():
            total += 1
    return total

print("\nSTEP 4: WORD COUNT INSIGHTS")
print('Number of feedbacks containing "good":', count_word_in_feedbacks("good"))
print('Number of feedbacks containing "poor":', count_word_in_feedbacks("poor"))
print('Number of feedbacks containing "excellent":', count_word_in_feedbacks("excellent"))

# Step 5: Final summary and insights
print("\nSTEP 5: FINAL CLEANED FEEDBACK DATA")
print(feedback_data)

average_rating = sum(feedback_data["Rating"]) / len(feedback_data["Rating"])
print(f"Average rating: {average_rating:.2f}")

longest_index = max(range(len(feedback_data["Feedback"])),
                    key=lambda i: len(feedback_data["Feedback"][i].split()))
longest_comment = feedback_data["Feedback"][longest_index]
print("\nLongest feedback:")
print("S_No:", feedback_data["S_No"][longest_index])
print("Name:", feedback_data["Name"][longest_index])
print("Feedback:", longest_comment)
print("Word count:", len(longest_comment.split()))

unique_words = set()
for comment in feedback_data["Feedback"]:
    unique_words.update(comment.split())
print("\nUnique words used across all feedbacks:")
print(sorted(unique_words))

# Optional: Sort feedbacks from highest rating to lowest
sorted_feedbacks = sorted(
    zip(feedback_data["S_No"], feedback_data["Name"],
        feedback_data["Feedback"], feedback_data["Rating"]),
    key=lambda item: item[3], reverse=True
)
print("\nOPTIONAL: FEEDBACKS SORTED BY RATING (HIGH TO LOW)")
for s_no, name, comment, rating in sorted_feedbacks:
    print(f"S_No: {s_no} | Name: {name} | Rating: {rating} | Feedback: {comment}")
