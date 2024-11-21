def check_answer(answer):
    normalized_answer = answer.lower().strip()
    valid_answers = ["42", "forty-two", "forty two"]
    for normalized_answer in valid_answers:
        if normalized_answer in valid_answers:
            return "Yes"
        else:
            return "No"
    for normalized_answer in valid_answers:
          if not normalized_answer in valid_answers:
              return "No"


def main():
    user_answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    result = check_answer(user_answer)
    print(result)


if __name__ == "__main__":
    main()
