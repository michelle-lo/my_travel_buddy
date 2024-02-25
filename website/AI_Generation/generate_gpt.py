import openai
# from openai import OpenAI

openai.api_key='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'

# Set up OpenAI API key

# Define trip data
trip = {
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
prompt = f"Generate 10 activity suggestions for a trip with estimated budget per activity:\nLocation: {trip['location']}\nBudget: {trip['budget']}\nDietary Restrictions: {trip['dietary_restrictions']}\nPreferences: {', '.join(trip['preferences'])}"

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