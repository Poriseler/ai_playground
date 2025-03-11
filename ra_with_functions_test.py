from openai_module import generate_text_basic
from prompts import react_system_prompt
from sample_functions import get_weather
from json_helpers import extract_json


# Available actions are:
available_functions = {
    "get_weather": get_weather
}

prompt = """
Should I take an umbrella when going out today in Arizona?"""

response = generate_text_basic(
    prompt, model="gpt-4", system_prompt=react_system_prompt)

json_function = extract_json(response)

print(json_function)
