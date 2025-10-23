from fastapi import APIRouter, HTTPException, Body, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from typing import Dict, Any, Optional, List
import io
from contextlib import redirect_stdout, redirect_stderr
import traceback

router = APIRouter()

# Store user sessions with variables
user_sessions = {}

@router.post("/execute-input", response_model=Dict[str, Any])
async def execute_with_input(
    code: str = Body(..., embed=True),
    user_input: str = Body(None, embed=True),
    session_id: str = Body(..., embed=True)
):
    """
    Execute Python code that might require user input and return the output.
    Demonstrates advanced input/output handling in Python.
    """
    # Initialize session if it doesn't exist
    if session_id not in user_sessions:
        user_sessions[session_id] = {
            "variables": {},
            "history": []
        }

    # Prepare input function that will return the provided user input
    def mock_input(prompt=""):
        print(prompt, end="")
        return user_input

    # Prepare execution environment with custom input function and session variables
    exec_globals = {
        "input": mock_input,
        "__builtins__": __builtins__,
        **user_sessions[session_id]["variables"]
    }

    # Capture stdout and stderr
    captured_output = io.StringIO()
    captured_error = io.StringIO()

    try:
        # Execute the code
        with redirect_stdout(captured_output), redirect_stderr(captured_error):
            exec(code, exec_globals)

        # Update session variables
        for key, value in exec_globals.items():
            if key != "__builtins__" and key != "input" and not key.startswith("_"):
                user_sessions[session_id]["variables"][key] = value

        # Get the output
        output = captured_output.getvalue()

        # Add to history
        user_sessions[session_id]["history"].append({
            "code": code,
            "input": user_input,
            "output": output,
            "success": True
        })

        return {
            "output": output,
            "success": True,
            "error": None,
            "variables": {k: str(v) for k, v in user_sessions[session_id]["variables"].items()}
        }
    except Exception as e:
        error_message = captured_error.getvalue() or str(e)

        # Add to history
        user_sessions[session_id]["history"].append({
            "code": code,
            "input": user_input,
            "output": captured_output.getvalue(),
            "error": error_message,
            "success": False
        })

        return {
            "output": captured_output.getvalue(),
            "success": False,
            "error": error_message,
            "variables": {k: str(v) for k, v in user_sessions[session_id]["variables"].items()}
        }

@router.get("/session/{session_id}", response_model=Dict[str, Any])
async def get_session(session_id: str):
    """
    Get the current session state with variables and history.
    """
    if session_id not in user_sessions:
        raise HTTPException(status_code=404, detail=f"Session with ID {session_id} not found")

    return {
        "variables": {k: str(v) for k, v in user_sessions[session_id]["variables"].items()},
        "history": user_sessions[session_id]["history"]
    }

@router.delete("/session/{session_id}")
async def clear_session(session_id: str):
    """
    Clear a user's session.
    """
    if session_id not in user_sessions:
        raise HTTPException(status_code=404, detail=f"Session with ID {session_id} not found")

    user_sessions[session_id] = {
        "variables": {},
        "history": []
    }

    return {"message": f"Session {session_id} has been cleared"}

@router.get("/console", response_class=HTMLResponse)
async def interactive_console():
    """
    Provide an interactive console for learning Python with input/output.
    """
    return """
    <html>
        <head>
            <title>Interactive Python Console</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                }
                h1, h2 {
                    color: #2c3e50;
                }
                p {
                    color: #34495e;
                }
                .console {
                    background-color: #f8f9fa;
                    padding: 15px;
                    border-radius: 5px;
                    margin-bottom: 20px;
                }
                textarea {
                    width: 100%;
                    height: 150px;
                    padding: 10px;
                    border-radius: 5px;
                    border: 1px solid #ddd;
                    font-family: monospace;
                    margin-bottom: 10px;
                }
                input[type="text"] {
                    width: 100%;
                    padding: 10px;
                    border-radius: 5px;
                    border: 1px solid #ddd;
                    margin-bottom: 10px;
                }
                button {
                    background-color: #3498db;
                    color: white;
                    border: none;
                    padding: 10px 15px;
                    border-radius: 5px;
                    cursor: pointer;
                }
                button:hover {
                    background-color: #2980b9;
                }
                .output {
                    background-color: #2c3e50;
                    color: white;
                    padding: 15px;
                    border-radius: 5px;
                    font-family: monospace;
                    white-space: pre-wrap;
                    margin-top: 15px;
                }
                .error {
                    color: #e74c3c;
                }
                .variables {
                    background-color: #ecf0f1;
                    padding: 15px;
                    border-radius: 5px;
                    margin-top: 15px;
                }
                .examples {
                    margin-top: 30px;
                }
                .example {
                    background-color: #f1f1f1;
                    padding: 10px;
                    border-radius: 5px;
                    margin-bottom: 10px;
                    cursor: pointer;
                }
            </style>
        </head>
        <body>
            <h1>Interactive Python Console</h1>
            <p>Type your Python code below and see the results immediately. This console supports input() function calls.</p>

            <div class="console">
                <h2>Code Editor</h2>
                <textarea id="code-editor" placeholder="# Type your Python code here
print('Hello, world!')
name = input('Enter your name: ')
print(f'Hello, {name}!')"></textarea>

                <h2>Input (for input() function calls)</h2>
                <input type="text" id="user-input" placeholder="Your input for input() function calls">

                <button id="run-button">Run Code</button>
                <button id="clear-button">Clear Console</button>

                <div id="output" class="output" style="display: none;"></div>

                <div id="variables" class="variables" style="display: none;">
                    <h2>Variables</h2>
                    <pre id="variables-content"></pre>
                </div>
            </div>

            <div class="examples">
                <h2>Example Code Snippets</h2>
                <p>Click on an example to load it into the editor:</p>

                <div class="example" onclick="loadExample(this)">
                    <strong>Basic Input/Output</strong>
                    <pre>name = input('What is your name? ')
age = input('How old are you? ')
print(f'Hello, {name}! In 10 years, you will be {int(age) + 10} years old.')</pre>
                </div>

                <div class="example" onclick="loadExample(this)">
                    <strong>Working with Variables</strong>
                    <pre># Variables and data types
x = 10
y = 5
name = 'Python'

print(f'x = {x}, y = {y}, name = {name}')
print(f'x + y = {x + y}')
print(f'x - y = {x - y}')
print(f'x * y = {x * y}')
print(f'x / y = {x / y}')</pre>
                </div>

                <div class="example" onclick="loadExample(this)">
                    <strong>Conditional Logic</strong>
                    <pre>temperature = int(input('What is the temperature today? '))

if temperature > 30:
    print('It\'s hot outside!')
elif temperature > 20:
    print('It\'s a nice day.')
elif temperature > 10:
    print('It\'s a bit chilly.')
else:
    print('It\'s cold outside!')</pre>
                </div>

                <div class="example" onclick="loadExample(this)">
                    <strong>Loops</strong>
                    <pre>print('Counting with a for loop:')
for i in range(1, 6):
    print(f'Count: {i}')

print('\\nCounting with a while loop:')
count = 1
while count <= 5:
    print(f'Count: {count}')
    count += 1</pre>
                </div>

                <div class="example" onclick="loadExample(this)">
                    <strong>Lists and Iteration</strong>
                    <pre>fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

print('List of fruits:')
for i, fruit in enumerate(fruits):
    print(f'{i+1}. {fruit}')

favorite = input('\\nWhich fruit do you like best? (Enter name) ')
if favorite in fruits:
    print(f'Yes, {favorite} is in our list at position {fruits.index(favorite) + 1}!')
else:
    print(f'Sorry, {favorite} is not in our list.')</pre>
                </div>
            </div>

            <script>
                // Generate a random session ID
                const sessionId = Math.random().toString(36).substring(2, 15);
                let currentOutput = '';

                // Function to load an example into the editor
                function loadExample(element) {
                    const code = element.querySelector('pre').textContent;
                    document.getElementById('code-editor').value = code;
                }

                // Function to run the code
                document.getElementById('run-button').addEventListener('click', async () => {
                    const codeEditor = document.getElementById('code-editor');
                    const userInput = document.getElementById('user-input');
                    const outputDiv = document.getElementById('output');
                    const variablesDiv = document.getElementById('variables');
                    const variablesContent = document.getElementById('variables-content');

                    // Display the output div
                    outputDiv.style.display = 'block';
                    outputDiv.innerHTML = 'Running code...';

                    try {
                        const response = await fetch('/api/python/interactive/execute-input', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                            },
                            body: JSON.stringify({
                                code: codeEditor.value,
                                user_input: userInput.value,
                                session_id: sessionId
                            }),
                        });

                        const data = await response.json();

                        if (data.success) {
                            outputDiv.innerHTML = data.output || '(No output)';
                        } else {
                            outputDiv.innerHTML = `<div class="error">${data.error}</div>`;
                            if (data.output) {
                                outputDiv.innerHTML = data.output + outputDiv.innerHTML;
                            }
                        }

                        // Display variables
                        if (Object.keys(data.variables).length > 0) {
                            variablesDiv.style.display = 'block';
                            variablesContent.textContent = JSON.stringify(data.variables, null, 2);
                        } else {
                            variablesDiv.style.display = 'none';
                        }

                        currentOutput = data.output;
                    } catch (error) {
                        outputDiv.innerHTML = `<div class="error">Error: ${error.message}</div>`;
                    }
                });

                // Function to clear the console
                document.getElementById('clear-button').addEventListener('click', async () => {
                    const codeEditor = document.getElementById('code-editor');
                    const userInput = document.getElementById('user-input');
                    const outputDiv = document.getElementById('output');
                    const variablesDiv = document.getElementById('variables');

                    // Clear the editor and output
                    codeEditor.value = '';
                    userInput.value = '';
                    outputDiv.style.display = 'none';
                    variablesDiv.style.display = 'none';

                    try {
                        await fetch(`/api/python/interactive/session/${sessionId}`, {
                            method: 'DELETE'
                        });
                    } catch (error) {
                        console.error('Error clearing session:', error);
                    }
                });
            </script>
        </body>
    </html>
    """