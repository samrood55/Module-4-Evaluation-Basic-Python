
# STEP 4: Word count insights
def count_word_in_feedbacks(word):
    """Count feedback entries containing the given whole word, case-insensitively."""
    target = word.lower().strip()
    return sum(1 for comment in feedback_data["Feedback"]
               if target in comment.split())

print("\nWORD COUNT INSIGHTS")
print('Feedbacks containing "good":', count_word_in_feedbacks("good"))
print('Feedbacks containing "poor":', count_word_in_feedbacks("poor"))
print('Feedbacks containing "excellent":', count_word_in_feedbacks("excellent"))

# STEP 5: Final summary and insights
print("\nFINAL CLEANED FEEDBACK DATA")
print(feedback_data)

average_rating = sum(feedback_data["Rating"]) / len(feedback_data["Rating"])
print(f"\nAverage rating: {average_rating:.2f}")

longest_index = max(
    range(len(feedback_data["Feedback"])),
    key=lambda index: len(feedback_data["Feedback"][index].split())
)
print("\nLONGEST FEEDBACK")
print("S_No:", feedback_data["S_No"][longest_index])
print("Name:", feedback_data["Name"][longest_index])
print("Feedback:", feedback_data["Feedback"][longest_index])
print("Word count:", len(feedback_data["Feedback"][longest_index].split()))

unique_words = set()
for comment in feedback_data["Feedback"]:
    unique_words.update(comment.split())
print("\nUNIQUE WORDS USED ACROSS ALL FEEDBACKS")
print(sorted(unique_words))

# Optional: Sort feedback entries by rating, highest to lowest
sorted_entries = sorted(
    zip(feedback_data["S_No"], feedback_data["Name"],
        feedback_data["Feedback"], feedback_data["Rating"]),
    key=lambda entry: entry[3],
    reverse=True
)
print("\nFEEDBACKS SORTED BY RATING (HIGHEST TO LOWEST)")
for serial_number, name, comment, rating in sorted_entries:
    print(f"S_No: {serial_number} | Name: {name} | Rating: {rating} | Feedback: {comment}")