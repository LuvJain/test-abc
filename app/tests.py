"""
Test script for Python Learning App
To run: python -m app.tests
"""

import unittest
import json
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

class TestPythonLearningApp(unittest.TestCase):

    def test_root(self):
        """Test that the root endpoint returns 200 OK"""
        response = client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Welcome to the Python Learning App", response.text)

    def test_concepts(self):
        """Test that the concepts endpoint returns a list of concepts"""
        response = client.get("/api/python/concepts")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(isinstance(data, list))
        self.assertTrue(len(data) > 0)

        # Check structure of first concept
        first_concept = data[0]
        self.assertIn("name", first_concept)
        self.assertIn("description", first_concept)
        self.assertIn("examples", first_concept)

    def test_variable_types(self):
        """Test that the variable types endpoint returns a list of types"""
        response = client.get("/api/python/variable-types")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(isinstance(data, list))
        self.assertTrue(len(data) > 0)

        # Check structure of first variable type
        first_type = data[0]
        self.assertIn("type_name", first_type)
        self.assertIn("description", first_type)
        self.assertIn("examples", first_type)

    def test_execute_code(self):
        """Test that the code execution endpoint works"""
        code_data = {"code": "x = 5\ny = 10\nprint(x + y)"}
        response = client.post("/api/python/execute", json=code_data)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["code"], code_data["code"])
        self.assertEqual(data["output"], "15\n")
        self.assertTrue(data["success"])
        self.assertIsNone(data["error"])

    def test_code_execution_with_error(self):
        """Test that code execution handles errors properly"""
        code_data = {"code": "print(undefined_variable)"}
        response = client.post("/api/python/execute", json=code_data)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["code"], code_data["code"])
        self.assertFalse(data["success"])
        self.assertIsNotNone(data["error"])

    def test_questions(self):
        """Test that the questions endpoint returns a list of questions"""
        response = client.get("/api/python/questions")
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(isinstance(data, list))
        self.assertTrue(len(data) > 0)

        # Check structure of first question
        first_question = data[0]
        self.assertIn("id", first_question)
        self.assertIn("question", first_question)

    def test_evaluate_answer(self):
        """Test that the evaluate answer endpoint works"""
        answer_data = {"question_id": 1, "answer": "15"}
        response = client.post("/api/python/evaluate", json=answer_data)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["question_id"], 1)
        self.assertTrue(data["correct"])
        self.assertIn("explanation", data)
        self.assertIn("next_steps", data)

    def test_evaluate_wrong_answer(self):
        """Test that the evaluate answer endpoint handles wrong answers"""
        answer_data = {"question_id": 1, "answer": "wrong answer"}
        response = client.post("/api/python/evaluate", json=answer_data)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(data["question_id"], 1)
        self.assertFalse(data["correct"])
        self.assertIn("explanation", data)
        self.assertIn("next_steps", data)

    def test_interactive_console_endpoint(self):
        """Test that the interactive console HTML endpoint works"""
        response = client.get("/api/python/interactive/console")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Interactive Python Console", response.text)

if __name__ == "__main__":
    unittest.main()