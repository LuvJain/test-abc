from fastapi import APIRouter, HTTPException, Body, Query, Path
from typing import List, Dict, Any, Optional
import sys
import io
from contextlib import redirect_stdout, redirect_stderr
import traceback

from app.models import (
    PythonConcept,
    PythonVariable,
    CodeExecution,
    CodeExecutionResponse,
    UserInput,
    EvaluationResponse
)

router = APIRouter()

# Sample data for Python concepts
PYTHON_CONCEPTS = [
    {
        "name": "Variables",
        "description": "Variables are used to store data values. In Python, variables are created when a value is assigned to them.",
        "examples": ["x = 5", "name = 'John'", "is_valid = True"]
    },
    {
        "name": "Data Types",
        "description": "Python has various built-in data types like strings, numbers, and booleans.",
        "examples": ["# String\ntext = 'Hello'", "# Integer\nage = 25", "# Boolean\nis_active = False"]
    },
    {
        "name": "Conditionals",
        "description": "Conditionals allow you to execute certain blocks of code based on whether a condition is true or false.",
        "examples": [
            """
if age >= 18:
    print("Adult")
else:
    print("Minor")
            """,
            """
x = 10
if x < 5:
    print("Less than 5")
elif x < 15:
    print("Between 5 and 15")
else:
    print("Greater than or equal to 15")
            """
        ]
    },
    {
        "name": "Loops",
        "description": "Loops are used to iterate over a sequence or execute a block of code repeatedly.",
        "examples": [
            """
# For loop
for i in range(5):
    print(i)  # Prints 0, 1, 2, 3, 4
            """,
            """
# While loop
count = 0
while count < 5:
    print(count)
    count += 1  # Prints 0, 1, 2, 3, 4
            """
        ]
    },
    {
        "name": "Functions",
        "description": "Functions are blocks of reusable code that perform a specific task.",
        "examples": [
            """
# Define a function
def greet(name):
    return f"Hello, {name}!"

# Call the function
message = greet("Alice")
print(message)  # Prints: Hello, Alice!
            """
        ]
    }
]

# Sample data for Python variable types
PYTHON_VARIABLE_TYPES = [
    {
        "type_name": "Strings",
        "description": "Strings are sequences of characters enclosed in quotes.",
        "examples": ["name = 'Alice'", "message = \"Hello, world!\"", "multi_line = '''This is a\nmulti-line string'''"]
    },
    {
        "type_name": "Integers",
        "description": "Integers are whole numbers without a decimal point.",
        "examples": ["age = 25", "count = -10", "zero = 0"]
    },
    {
        "type_name": "Floats",
        "description": "Floats are numbers with a decimal point.",
        "examples": ["price = 19.99", "pi = 3.14159", "negative = -0.5"]
    },
    {
        "type_name": "Booleans",
        "description": "Booleans represent one of two values: True or False.",
        "examples": ["is_valid = True", "has_permission = False"]
    },
    {
        "type_name": "Lists",
        "description": "Lists are ordered collections of items that can be changed.",
        "examples": ["numbers = [1, 2, 3, 4, 5]", "names = ['Alice', 'Bob', 'Charlie']", "mixed = [1, 'Hello', True, 3.14]"]
    },
    {
        "type_name": "Tuples",
        "description": "Tuples are ordered collections that cannot be changed after creation.",
        "examples": ["coordinates = (10, 20)", "person = ('Alice', 30, 'Engineer')", "singleton = (1,)"]
    },
    {
        "type_name": "Dictionaries",
        "description": "Dictionaries store key-value pairs.",
        "examples": ["person = {'name': 'Alice', 'age': 30}", "scores = {'math': 90, 'science': 85, 'history': 95}"]
    }
]

# Sample questions for Python learning exercises
PYTHON_QUESTIONS = [
    {
        "id": 1,
        "question": "What will be the output of the following code?\n\nx = 5\ny = 10\nprint(x + y)",
        "correct_answer": "15",
        "explanation": "The code adds the variables x (5) and y (10), resulting in 15, which is then printed."
    },
    {
        "id": 2,
        "question": "What data type is the value in the following variable?\n\nmessage = 'Hello, Python!'",
        "correct_answer": "string",
        "explanation": "The value 'Hello, Python!' is enclosed in quotes, making it a string data type in Python."
    },
    {
        "id": 3,
        "question": "What will be the output of the following code?\n\nfor i in range(3):\n    print(i)",
        "correct_answer": "0\n1\n2",
        "explanation": "The range(3) function generates values from 0 to 2 (but not including 3). The for loop prints each value on a new line."
    }
]

@router.get("/concepts", response_model=List[PythonConcept])
async def get_python_concepts():
    """
    Get a list of basic Python concepts with descriptions and examples.
    """
    return PYTHON_CONCEPTS

@router.get("/concepts/{concept_name}", response_model=PythonConcept)
async def get_specific_concept(concept_name: str):
    """
    Get detailed information about a specific Python concept.
    """
    for concept in PYTHON_CONCEPTS:
        if concept["name"].lower() == concept_name.lower():
            return concept
    raise HTTPException(status_code=404, detail=f"Concept '{concept_name}' not found")

@router.get("/variable-types", response_model=List[PythonVariable])
async def get_variable_types():
    """
    Get information about Python variable types.
    """
    return PYTHON_VARIABLE_TYPES

@router.get("/variable-types/{type_name}", response_model=PythonVariable)
async def get_specific_variable_type(type_name: str):
    """
    Get detailed information about a specific Python variable type.
    """
    for var_type in PYTHON_VARIABLE_TYPES:
        if var_type["type_name"].lower() == type_name.lower():
            return var_type
    raise HTTPException(status_code=404, detail=f"Variable type '{type_name}' not found")

@router.post("/execute", response_model=CodeExecutionResponse)
async def execute_python_code(code_execution: CodeExecution):
    """
    Execute Python code and return the output.
    Demonstrates input/output in Python programming.
    """
    code = code_execution.code

    # Security measures
    if "import os" in code or "import subprocess" in code or "import sys" in code:
        return CodeExecutionResponse(
            code=code,
            output="",
            success=False,
            error="For security reasons, importing os, subprocess, or sys modules is not allowed."
        )

    # Capture stdout and stderr
    captured_output = io.StringIO()
    captured_error = io.StringIO()

    try:
        with redirect_stdout(captured_output), redirect_stderr(captured_error):
            exec(code, {"__builtins__": __builtins__}, {})

        output = captured_output.getvalue()
        return CodeExecutionResponse(
            code=code,
            output=output,
            success=True,
            error=None
        )
    except Exception as e:
        error_message = captured_error.getvalue() or str(e)
        return CodeExecutionResponse(
            code=code,
            output=captured_output.getvalue(),
            success=False,
            error=error_message
        )

@router.get("/questions", response_model=List[Dict[str, Any]])
async def get_questions():
    """
    Get a list of Python learning questions.
    """
    return [{"id": q["id"], "question": q["question"]} for q in PYTHON_QUESTIONS]

@router.get("/questions/{question_id}", response_model=Dict[str, Any])
async def get_specific_question(question_id: int = Path(..., ge=1)):
    """
    Get a specific Python learning question.
    """
    for question in PYTHON_QUESTIONS:
        if question["id"] == question_id:
            return {"id": question["id"], "question": question["question"]}
    raise HTTPException(status_code=404, detail=f"Question with ID {question_id} not found")

@router.post("/evaluate", response_model=EvaluationResponse)
async def evaluate_answer(user_input: UserInput):
    """
    Evaluate the user's answer to a Python question.
    Demonstrates input/output in Python learning.
    """
    question_id = user_input.question_id
    user_answer = user_input.answer

    # Find the question
    question = None
    for q in PYTHON_QUESTIONS:
        if q["id"] == question_id:
            question = q
            break

    if not question:
        raise HTTPException(status_code=404, detail=f"Question with ID {question_id} not found")

    # Check if the answer is correct
    is_correct = user_answer.strip().lower() == question["correct_answer"].strip().lower()

    # Determine next steps based on correctness
    next_steps = None
    if is_correct:
        if question_id < len(PYTHON_QUESTIONS):
            next_steps = f"Great job! Try question {question_id + 1} next."
        else:
            next_steps = "Congratulations! You've completed all the questions. Try the code execution endpoint to practice more."
    else:
        next_steps = "Review the explanation and try again."

    return EvaluationResponse(
        question_id=question_id,
        correct=is_correct,
        explanation=question["explanation"],
        next_steps=next_steps
    )