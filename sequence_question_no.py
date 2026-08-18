# app.py

import re
from pathlib import Path


def renumber_questions(markdown: str) -> str:
    """
    Renumber Markdown question headings sequentially.

    Supported formats:

        ## Q1. What is RAG?
        ## Q2. What is Reranking?
        ## Q. What is a Cross Encoder?
        ## Q What is Redis?

    Output:

        ## Q1. What is RAG?
        ## Q2. What is Reranking?
        ## Q3. What is a Cross Encoder?
        ## Q4. What is Redis?
    """

    question_number = 0

    pattern = re.compile(
        r"^(#{1,6}\s+Q(?:\d+)?(?:\.)?(?:\s+|$))(.*)$",
        re.IGNORECASE,
    )

    updated_lines = []

    for line in markdown.splitlines():
        match = pattern.match(line)

        if match:
            question_number += 1

            heading = match.group(1)
            question_text = match.group(2).strip()

            # Preserve the original heading level.
            heading_level = re.match(r"^#{1,6}", heading).group(0)

            new_line = f"{heading_level} Q{question_number}."

            if question_text:
                new_line += f" {question_text}"

            updated_lines.append(new_line)

        else:
            updated_lines.append(line)

    return "\n".join(updated_lines)


def process_markdown_file(file_path: str) -> None:
    """
    Read the Markdown file, renumber the questions,
    and save the updated content directly to the same file.
    """

    path = Path(file_path)

    if not path.exists():
        print(f"❌ File not found: {path}")
        return

    if path.suffix.lower() != ".md":
        print("❌ Please provide a Markdown (.md) file.")
        return

    # Read original file
    content = path.read_text(encoding="utf-8")

    # Renumber questions
    updated_content = renumber_questions(content)

    # Save directly to the original file
    path.write_text(updated_content, encoding="utf-8")

    print(f"✅ Questions renumbered successfully.")
    print(f"📄 File updated: {path}")


if __name__ == "__main__":

    # ========================================================
    # CHANGE THIS PATH TO YOUR MARKDOWN FILE
    # ========================================================

    file_path = r"C:\Users\Khushbu.Kushvaha\Desktop\Kk\Notes_for_interviews\05_react.md"

    process_markdown_file(file_path)