# api.py
import openai
import os


def get_latex_equation(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a machine that provides LaTeX representations for mathematical equations "
                        "and descriptions. Respond with LaTeX code for equations, encapsulated in dollar signs. "
                        "Provide explanations as LaTeX comments. Avoid any non-LaTeX text. For unclear prompts, request clarification."
                    )
                },
                {
                    "role": "user",
                    "content": "Convert to LaTeX: " + prompt.strip()
                }
            ]

        )

        # Extract the LaTeX equation from the response
        latex_equation = response.choices[0].message["content"]
        return latex_equation

    except openai.error.OpenAIError as e:
        return f"An error occurred: {e}"
