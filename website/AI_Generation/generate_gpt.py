import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# import openai
# # from openai import OpenAI

# openai.api_key='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'

# # Set up OpenAI API key

# def gen_ai_plan(trip_id):

# # Define trip data
#     tripInfo = {
#         'email': 'lwz900@case.edu',
#         'location': 'Cleveland',
#         'birthday': '2008-07-01',
#         'budget': 1000,
#         'dietary_restrictions': 'Vegetarian',
#         'start_date': '2024-11-28',
#         'end_date': '2024-11-30',
#         'preferences': ['Creativity', 'Puzzles and Games']
#     }

#     # Create a prompt with the trip data
#     prompt = f"Generate 10 activity suggestions for a trip with estimated budget per activity:\nLocation: {tripInfo['location']}\nBudget: {tripInfo['budget']}\nDietary Restrictions: {tripInfo['dietary_restrictions']}\nPreferences: {', '.join(tripInfo['preferences'])}"

#     # Make a request to OpenAI GPT model
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",  # or use another available model
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {"role": "user", "content": prompt}
#         ]
#     )

#     # Get the generated suggestions
#     generated_suggestions = response['choices'][0]['message']['content']
#     print(generated_suggestions)
#     return generated_suggestions