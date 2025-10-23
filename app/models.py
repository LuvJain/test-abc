from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any, Union

class PythonConcept(BaseModel):
    """Model for Python concept with name, description and examples"""
    name: str = Field(..., description="Name of the Python concept")
    description: str = Field(..., description="Description of the concept")
    examples: List[str] = Field(..., description="Examples of the concept in use")

class PythonVariable(BaseModel):
    """Model for Python variable types with explanations and examples"""
    type_name: str = Field(..., description="Name of the Python variable type")
    description: str = Field(..., description="Description of the variable type")
    examples: List[str] = Field(..., description="Examples of the variable type in use")

class CodeExecution(BaseModel):
    """Model for Python code execution request"""
    code: str = Field(..., description="Python code to execute")

class CodeExecutionResponse(BaseModel):
    """Model for Python code execution response"""
    code: str = Field(..., description="Original Python code")
    output: str = Field(..., description="Output of the executed code")
    success: bool = Field(..., description="Whether execution was successful")
    error: Optional[str] = Field(None, description="Error message if execution failed")

class UserInput(BaseModel):
    """Model for user input in Python learning exercises"""
    question_id: int = Field(..., description="ID of the question being answered")
    answer: str = Field(..., description="User's answer to the question")

class EvaluationResponse(BaseModel):
    """Model for evaluation response of user input"""
    question_id: int = Field(..., description="ID of the question that was answered")
    correct: bool = Field(..., description="Whether the answer was correct")
    explanation: str = Field(..., description="Explanation of the correct answer")
    next_steps: Optional[str] = Field(None, description="Suggested next steps for learning")