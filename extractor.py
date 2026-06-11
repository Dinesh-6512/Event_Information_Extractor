from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

from langfuse import Langfuse
from langfuse.callback import CallbackHandler

from models import EventDetails
from prompt import SYSTEM_PROMPT

# ---------------------------
# Load Environment Variables
# ---------------------------

load_dotenv()

# ---------------------------
# Langfuse Setup
# ---------------------------

langfuse = Langfuse()

print("Langfuse Auth:", langfuse.auth_check())

langfuse_handler = CallbackHandler()

# ---------------------------
# Output Parser
# ---------------------------

parser = PydanticOutputParser(
    pydantic_object=EventDetails
)

# ---------------------------
# LLM
# ---------------------------

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

# ---------------------------
# Prompt Template
# ---------------------------

prompt = PromptTemplate(
    template="""
{system_prompt}

{format_instructions}

Event Description:
{text}
""",
    input_variables=["text"],
    partial_variables={
        "system_prompt": SYSTEM_PROMPT,
        "format_instructions": parser.get_format_instructions()
    }
)

# ---------------------------
# Chain
# ---------------------------

chain = prompt | llm | parser

# ---------------------------
# Main Function
# ---------------------------

def extract_event_details(text):

    try:
        print("Invoking Chain...")

        result = chain.invoke(
            {"text": text},
            config={
                "callbacks": [langfuse_handler],
                "run_name": "Event Information Extractor"
            }
        )

        # Force sending traces
        langfuse.flush()

        print("Trace flushed successfully")

        return result

    except Exception as e:
        print("Error:", e)
        raise e