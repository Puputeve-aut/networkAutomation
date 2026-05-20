studentScores = [85, 92, 78, 90, 88]

# Calculate the total exam score using the built-in sum() function
totalExamScore = sum(studentScores)

# Calculate the total exam score using a for loop
sum = 0
for scores in studentScores:
    sum += scores

print("Total exam score: " + str(totalExamScore))
print("Total exam score using for loop: " + str(sum))

# Calculate the best score using the built-in max() function
bestScore = max(studentScores)

# Calculate the best score using a for loop
biggestScore = 0
for score in studentScores:
    if score > biggestScore:
        biggestScore = score

print("Best score: " + str(bestScore))
print("Best score using for loop: " + str(biggestScore))