import recombee_api_client
from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.api_requests import *


clienct = RecombeeClient('my-travel-buddy-dev', 'ucIdhtB7kLeuPRgrw7DUg8TAJLkgrkD3acfd2FDGInMm3x8PWGW1dyd3OaPvnoxh')

client = recombee_api_client.Client('ucIdhtB7kLeuPRgrw7DUg8TAJLkgrkD3acfd2FDGInMm3x8PWGW1dyd3OaPvnoxh', 'my-travel-buddy-dev')

trip_data = []
# soemehow get the user profule values in the arrayL trips
trip = ['email' = lwz9@case.edu, 'location' = Cleveland, 'birthday' = 2004-7-01, 'budget' = 1000, 'dietary_restrictions' = 'Vegetarian', 'start_date' = 2024-11-28, 'end_date' = 2024-11-30, 'preferences' = ['Creativity', 'Puzzles and Games']]

r = AddPurchase(email = trip['email'], location = trip['location'], birthday = trip['birthday'], 
    budget = trip['budget'], dietary_restrictions = trip['dietary_restrictions'], end_date = trip['end_date'], 
    start_date = trip['start_date'], preferences = trip['preferences'], cascade_create = True)
br = batch(r)
client.send(br)



# # This is run per trip
# for trip in trips:
#     r = AddPurchase(email = interaction[email], location = interaction[location], age = interaction[age], 
#     budget = interaction[budget], dietary_restrictions = interaction[dietary_restrictions], end_date = interaction[end_date], 
#     start_date = interaction[start_date, preferences = interaction[preferences], cascade_create = True)
#     trip_data.append(r)

# br = Batch(requests)






# # Set user values
# client.send(recombee_api_client.requests.SetUserValues(user_id, user_profile))

# # Simulate user interactions (e.g., views)
# client.send(recombee_api_client.requests.AddDetailView(user_id, 'activity1'))
# client.send(recombee_api_client.requests.AddDetailView(user_id, 'activity2'))

# # Request recommendations
# recommendations = client.send(recombee_api_client.requests.RecommendItemsToUser(user_id, 5))

# # Display recommended activities
# print("Recommended activities:", recommendations)