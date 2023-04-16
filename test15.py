import json

with open("questions.json", "r") as file:
  content = file.read()

data = json.loads(content)


for question in data:

  print(question["Question_text"])
  for index, alternative in enumerate(question["Alternatives"]):
    print(index +1, "-",  alternative)

  user_choice = int(input("Enter you answer..."))
  question["user_choice"] = user_choice

score = 0
for index,  question in enumerate(data):
  if question["user_choice"] == question["Correct_answer"]:
    score += 1
    result = "Correct Answer"
  else:
    result = "Wrong Answer"
  message =f" {result} {index + 1} - Your answer is: {question['user_choice']}, "\
            f"Correct answers is: {question['Correct_answer']}"
  print(message)

print(score, "/", len(data))

