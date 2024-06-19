def main(answer):
    normalized_answer = answer.lower().strip()
    normal_answer = ['42', 'forty-two', 'forty two']
    if normalized_answer == normal_answer:
      return 'yes'
    else:
       return 'no'


def check_question():
   question = input("What is the Great Question of life, the Universe, and everythin? ")
   result = main(check_question)
   print(result)


if __name__ == "__main_":
   main()

