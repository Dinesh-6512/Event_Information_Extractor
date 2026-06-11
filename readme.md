# Event Information Extractor

## Overview

Event Information Extractor is a Generative AI application that extracts structured event details from unstructured event descriptions. The application uses Large Language Models (LLMs), LangChain, and Pydantic Output Parser to identify important event information and present it in a structured format.

## Features

* Extracts event name
* Extracts event date
* Extracts event time
* Extracts event location
* Extracts event organizer details
* Validates extracted information using Pydantic models
* User-friendly Streamlit interface
* Supports tracing and monitoring with Langfuse

## Technologies Used

* Python
* LangChain
* Groq LLM
* Pydantic
* Streamlit
* Langfuse
* dotenv

## Project Structure

Event_Info_Extractor/

├── extractor.py

├── frnt.py

├── models.py

├── prompt.py

├── requirements.txt

├── README.md

└── .env

## Installation

1. Clone the repository:

git clone <repository_url>

2. Navigate to the project directory:

cd Event_Info_Extractor

3. Install dependencies:

pip install -r requirements.txt

4. Create a .env file and add your API keys.

## Running the Application

Run the Streamlit application using:

streamlit run frnt.py

## Sample Input

Conference on Artificial Intelligence will be held on September 20, 2026, at 10:00 AM in Bangalore. The event is organized by Tech Innovators Association.

## Sample Output

* Event Name: Artificial Intelligence Conference
* Date: September 20, 2026
* Time: 10:00 AM
* Location: Bangalore
* Organizer: Tech Innovators Association

## Future Enhancements

* Support multiple events in a single input
* Export extracted data to CSV or JSON
* Deploy on cloud platforms
* Add multilingual support

## Author

Dinesh Verma
