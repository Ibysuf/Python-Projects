scores_Tekken = [34,42,93,23,90,12]
scores_SF = [55,24,39,85,32,98]

user_scores = [12,42,55,100,11,22]
highest = user_scores[0]

for score in user_scores:
    if score > highest:
        highest = score

print(f"Highest score: {highest}")
