# Obsidian MD Question Formatter

This script formats multiple-choice questions and their corresponding answers into a markdown-friendly format specifically tailored for [Obsidian MD](https://obsidian.md). It uses collapsible callouts to hide answers and explanations until clicked.

## Features

- Parses questions from a file (e.g., `questions.md`).
- Matches them with answers and explanations from a second file (e.g., `answers.md`).
- Formats them into collapsible callouts for answers and explanations.
- Saves the output to a new markdown file for easy import into Obsidian or other markdown-based tools.

## File Format Requirements

### Questions File (e.g., `questions.md`)

- Each question starts with a number, followed by the question text and four options (A, B, C, D).
- Example:
  ```
  1. What is the capital of France?
     A. Berlin
     B. Paris
     C. Madrid
     D. Rome
  ```

### Answers File (e.g., `answers.md`)

- Each entry contains the question number, correct answer, and an explanation.
- Example:
  ```
  1. B. Paris is the capital of France.
  ```

## Usage

### 1. Prepare Your Files

Ensure you have:

- A file containing the questions (e.g., `questions.md`).
- A file containing the answers and explanations (e.g., `answers.md`).

### 2. Run the Script

1. Place the script and the input files in the same directory.
2. Open the script and update these variables:
   ```python
   input_question_file = "questions.md"
   input_answer_file = "answers.md"
   output_markdown_file = "formatted.md"
   ```
3. Run the script:
   ```bash
   python obsidian_formatter.py
   ```

### 3. Check the Output

The formatted markdown file (e.g., `formatted.md`) will be generated in the same directory.

### Output Example

```markdown
### Question 1:

What is the capital of France?

-**A.** Berlin -**B.** Paris -**C.** Madrid -**D.** Rome

> [!faq]- Answer  
> **Correct Answer:** B  
> **Explanation:** Paris is the capital of France.
```

## Customization

If you have multiple files to process or want additional features, modify the script or let me know for further assistance.

## License

This script is provided as-is, free for personal and educational use. Contributions and improvements are welcome!
