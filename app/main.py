from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

# Import routers
from app.routers import python_basics, interactive_console

# Create FastAPI app
app = FastAPI(
    title="Python Learning App",
    description="A simple application to learn Python basics",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(python_basics.router, prefix="/api/python", tags=["Python Basics"])
app.include_router(interactive_console.router, prefix="/api/python/interactive", tags=["Interactive Console"])

# Root endpoint
@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <html>
        <head>
            <title>Python Learning App</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                }
                h1 {
                    color: #2c3e50;
                }
                p {
                    color: #34495e;
                }
                .endpoint {
                    background-color: #f8f9fa;
                    padding: 10px;
                    border-radius: 5px;
                    margin-bottom: 10px;
                }
                a {
                    color: #3498db;
                    text-decoration: none;
                }
                a:hover {
                    text-decoration: underline;
                }
                .feature {
                    margin: 20px 0;
                    padding: 15px;
                    background-color: #e1f5fe;
                    border-radius: 5px;
                    border-left: 5px solid #03a9f4;
                }
            </style>
        </head>
        <body>
            <h1>Welcome to the Python Learning App</h1>
            <p>This application is designed to help you learn Python basics through interactive API endpoints.</p>

            <div class="feature">
                <h2>🚀 Interactive Python Console</h2>
                <p>Our most powerful feature! Try Python code directly in your browser with input/output support.</p>
                <p><a href="/api/python/interactive/console" target="_blank">Launch Interactive Console</a></p>
            </div>

            <h2>Available Endpoints:</h2>
            <div class="endpoint">
                <h3>Python Basics</h3>
                <p><a href="/api/python/concepts">/api/python/concepts</a> - Get a list of Python basic concepts</p>
                <p><a href="/api/python/variable-types">/api/python/variable-types</a> - Learn about Python variable types</p>
                <p><a href="/api/python/questions">/api/python/questions</a> - Practice Python questions</p>
                <p><a href="/docs">/docs</a> - Interactive API documentation</p>
            </div>

            <h2>How to Use This App:</h2>
            <ol>
                <li>Browse Python concepts and variable types to learn the basics</li>
                <li>Try the interactive console to write and run Python code</li>
                <li>Answer practice questions to test your knowledge</li>
                <li>Use the API documentation to explore all features</li>
            </ol>

            <p>Start exploring the API to learn more about Python!</p>
        </body>
    </html>
    """

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)