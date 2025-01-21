import re


def clean_text(text):
    """Cleans up text by stripping extra spaces and normalizing."""
    return re.sub(r"\s+", " ", text.strip())


def parse_questions(content):
    """Parses questions from the input text."""
    questions = []
    question_pattern = r"(\d+)\.\s+(.*?)\n\s+A\.\s+(.*?)\n\s+B\.\s+(.*?)\n\s+C\.\s+(.*?)\n\s+D\.\s+(.*?)\n"
    matches = re.findall(question_pattern, content, re.DOTALL)

    for match in matches:
        question_number, question_text, opt_a, opt_b, opt_c, opt_d = match
        questions.append(
            {
                "number": int(question_number),
                "text": clean_text(question_text),
                "options": {
                    "A": clean_text(opt_a),
                    "B": clean_text(opt_b),
                    "C": clean_text(opt_c),
                    "D": clean_text(opt_d),
                },
            }
        )
    return questions


def parse_answers_multiline(content):
    """Parses answers and multiline explanations from the input text."""
    answers = {}
    # Match each block of "question number, correct answer, and explanation"
    answer_pattern = r"(\d+)\.\s+([A-D])\.\s+(.*?)(?=\n\d+\.\s+[A-D]\.|$)"
    matches = re.findall(answer_pattern, content, re.DOTALL)

    for match in matches:
        question_number, correct_option, explanation = match
        answers[int(question_number)] = {
            "correct_option": correct_option.strip(),
            "explanation": clean_text(explanation),
        }
    return answers


def format_questions_for_obsidian(questions, answers):
    """Formats questions and answers into Obsidian MD with callouts."""
    formatted_questions = []
    for question in questions:
        q_number = question["number"]
        if q_number in answers:
            formatted_questions.append(
                f"""
### Question {q_number}
{question['text']}

- **A.** {question['options']['A']}
- **B.** {question['options']['B']}
- **C.** {question['options']['C']}
- **D.** {question['options']['D']}

> [!faq]- Answer  
> **Correct Answer:** {answers[q_number]["correct_option"]}  
> **Explanation:** {answers[q_number]["explanation"]}
""".strip()
            )
    return "\n\n---\n\n".join(formatted_questions)


def process_files(questions_file, answers_file, output_file):
    """Processes the input files and writes the formatted output."""
    # Read files
    with open(questions_file, "r") as q_file:
        questions_content = q_file.read()
    with open(answers_file, "r") as a_file:
        answers_content = a_file.read()

    # Parse questions and multiline answers
    questions = parse_questions(questions_content)
    answers = parse_answers_multiline(answers_content)

    # Format the content
    formatted_content = format_questions_for_obsidian(questions, answers)

    # Write to output file
    with open(output_file, "w") as output:
        output.write(formatted_content)
    print(f"Formatted questions written to: {output_file}")


# Example usage
if __name__ == "__main__":
    # Replace these with your actual file paths
    input_question_file = "questions.md"
    input_answer_file = "answers.md"
    output_markdown_file = "formatted.md"

    process_files(input_question_file, input_answer_file, output_markdown_file)
