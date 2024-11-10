#!/usr/bin/env python
import os
from dotenv import load_dotenv
from crews.data_analysis_crew.data_analysis_crew import DataAnalysisCrew
from crews.recommendation_crew.recommendation_crew import RecommendationCrew
from chat.interface import ChatInterface

def setup_environment():
    """Setup environment variables and configurations"""
    load_dotenv()

    # Validate required environment variables
    required_vars = ["GROQ_API_KEY"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]

    if missing_vars:
        raise EnvironmentError(
            f"Missing required environment variables: {', '.join(missing_vars)}"
        )

def run():
    """Main entry point for the Energy Analysis Chatbot"""
    try:
        # Setup environment
        setup_environment()

        # Initialize chat interface
        chat_interface = ChatInterface()

        # Start chat interaction
        chat_interface.start()

    except Exception as e:
        print(f"An error occurred while starting the chatbot: {e}")
        raise

if __name__ == "__main__":
    run()