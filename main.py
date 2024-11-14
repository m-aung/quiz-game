import data

def run_quiz_game(questions):
  user_score = 0
  for question in questions:
    print(question['prompt'])
    for option in question['options']:
      print(option)
    answer = input('Enter your answer (A, B, C, or D):').upper()
    if answer == question['answer']:
      print('Correct, 😊\n')
      user_score += 1
    else:
      print('Wrong 🫢. The correct answer is', question['answer'], '\n')
  if user_score > 0:
    print(f'You got {user_score} out of {len(questions)} questions correct.👏')
  else:
    print(f'Sorry😞. None of your answers are correct.😢')



run_quiz_game(data.question_data)