import pathlib
import textwrap, markdown

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown



GOOGLE_API_KEY='AIzaSyBav2Nu9GG7MF9S-nkbwM3qENRIAs-7BcY'

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')

def gen_ai_plan(budget, location, prefs, birthday):
    #Define trip data
    tripInfo = {
        'location': location,
        'birthday': '2008-07-01',
        'budget': budget,
        'preferences': prefs,
        'birthday': birthday
    }

    # Create a prompt with the trip data
    prompt = f"Generate 10 activity suggestions for a trip with estimated budget per activity:\n People born on this date:{tripInfo['birthday']} \nLocation: {tripInfo['location']}\nBudget: {tripInfo['budget']}\nPreferences: {', '.join(tripInfo['preferences'])}"

    response = model.generate_content(prompt)

    text = ""
    for candidate in response.candidates:
        for part in candidate.content.parts:
            text += part.text + "\n"

    return text



import openai
# from openai import OpenAI

openai.api_key='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'

# Set up OpenAI API key

def gen_ai_plan(trip_id):

# Define trip data
    tripInfo = {
        'email': 'lwz900@case.edu',
        'location': 'Cleveland',
        'birthday': '2008-07-01',
        'budget': 1000,
        'dietary_restrictions': 'Vegetarian',
        'start_date': '2024-11-28',
        'end_date': '2024-11-30',
        'preferences': ['Creativity', 'Puzzles and Games']
    }

    # Create a prompt with the trip data
    prompt = f"Generate 10 activity suggestions for a trip with estimated budget per activity:\nLocation: {tripInfo['location']}\nBudget: {tripInfo['budget']}\nDietary Restrictions: {tripInfo['dietary_restrictions']}\nPreferences: {', '.join(tripInfo['preferences'])}"

    # Make a request to OpenAI GPT model
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or use another available model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    # Get the generated suggestions
    generated_suggestions = response['choices'][0]['message']['content']
    print(generated_suggestions)
    return generated_suggestions