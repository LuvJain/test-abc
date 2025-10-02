"""
Document Parser - Main entry point
"""
import uvicorn
import logging

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting Document Parser API")
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)