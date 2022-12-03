#
# CTI-110
# P4HW1 - Score List
# McDonald, Andrew
# 11/14/2022
#
#
# PROMPT for amount of user scores to be entered
# STORE in list
# SET score count starting at 0
#
# WHILE loop until all scores are obtained
#     IF scores are less than 0 or greater than 100, scores are invalid
#         DISPLAY Invalid text, text for score must be 0 - 100
#         PROMPT to enter score again
#     ELSE valid scores APPEND to list
#
# COMPUTE score count as increment + 1 with valid score
# IF all scores entered are valid proceed
#
# COMPUTE min score
# Remove min score from list
# COMPUTE average score
#
# IF greater or equal to 90 then
#     SET letter grade A
# ELSE 
# IF greater or equal to 80
#     SET letter grade B
# ELSE
# IF greater or equal to 70
#     SET letter grade C
# ELSE
# IF greater or equal to 60
#     SET letter grade D
# ELSE
# IF
#     SET letter grade F
#
# DISPLAY min score, list after min score removed, average score, & letter grade
#
#
# BEGIN Score List Program
#

score_list = []
entered_scores = int(input("How many scores do you want to enter? ")) #numberOfScores
score_count = 0 #currentNumOfScores

while(True):
    
    while(score_count < entered_scores):
        scores = float(input('Enter score #{}: '.format(score_count+1)))

        while(True):
            if(scores < 0 or scores > 100):
                print("\nINVALID Score entered!!!!\nScore should be between 0 and 100")
                scores = float(input('Enter score #{} again: '.format(score_count+1)))
            else:
                score_list.append(scores)
                break
        
        score_count += 1 
        
    if(score_count == entered_scores):
        break

min_score = min(score_list)
score_list.remove(min(score_list))
avg_score = sum(score_list) / len(score_list)

if avg_score >= 90:
    letter_grade = 'A'
elif avg_score >= 80:
     letter_grade = 'B'
elif avg_score >= 70:
     letter_grade = 'C'
elif avg_score >= 60:
     letter_grade = 'D'
else:
    avg_score >= 50
    letter_grade = 'F'

print("--------------Results-----------")
print("Lowest Score  :",min_score)
print("Modified List :",score_list)
print("Scores Average:",avg_score)
print("Grade         :",letter_grade)
print("----------------------------------")

#
# END Score List Program

# corrected last elif to else as it should have been
# still would like to replace the use of break with condition statement
