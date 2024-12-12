import openai  # Imports the OpenAI library for interacting with OpenAI's APIs
from dotenv import load_dotenv  # Imports the 'load_dotenv' function to load environment variables from a .env file
import os  # Imports the 'os' module to interact with the operating system (used here for fetching environment variables)

#Load API key and organization ID from .env file
load_dotenv(dotenv_path='.env')

# Set API credentials
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPENAI_ORG_ID")

# The following program uses an openai API key to prompt openai's gpt-3.5-turbo model (the same used
# in the LMQL queries), to solve a difficult mathematical word problem.
# Within this prompt, the model is also intructed to use chain-of-thought reasoning to solve the problem,
# The program output is the model's answer, as well as what percent confident the model is in that answer.

# Example output:
# ANSWER: First, calculate the head start the first train has by multiplying its speed by the time it departed early 
# (60 mph * 0.5 hours = 30 miles). 
# Next, subtract the head start from the total distance to find the remaining distance the second train needs to travel 
# (240 miles - 30 miles = 210 miles). 
# Then, calculate the combined speed of both trains (60 mph + 80 mph = 140 mph). 
# Finally, divide the remaining distance by the combined speed to find the time it will take for the two trains to meet 
# (210 miles / 140 mph = 1.5 hours). The two trains will meet at 5:00 PM. 
# CONFIDENCE: I am 90% confident in my answer.

response2 = openai.ChatCompletion.create( # opens a call to the openai API
    model="gpt-3.5-turbo",  # Chat-based model
    messages=[
        {"role": "user", "content": "If a train traveling at 60 miles per hour departs from City A at 3:00 PM, \
        and another train traveling at 80 miles per hour departs from City B at 3:30 PM toward City A, \
        and the distance between the cities is 240 miles, at what time will the two trains meet? \
        Your answer should be no more than four sentences.\
        Think step-by-step to solve this problem. \
        Finally, output what percent confident you are in your answer."},
    ],
    # Prompts the model to answer a difficult mathematical word problem
    max_tokens=300,  # Limits the response length
    temperature=0,  # Adjusts temperature, which controls randomness, to be vert deterministic (as are the LMQl queries)
)

# Prints the response
print(response2['choices'][0]['message']['content'].strip())


# The following program uses an openai API key to prompt openai's gpt-3.5-turbo model (the same used
# in the LMQL queries), to solve a difficult mathematical word problem.
# There is not extra prompting to guide the model in how to reason through the problem.
# The program output is the model's answer, as well as what percent confident the model is in that answer.

# Example Output: 
# ANSWER: The first train will have a 30-minute head start on the second train. 
# In that time, the first train will have traveled 30 miles. 
# This means the remaining distance for the second train to cover is 210 miles. 
# The combined speed of the two trains is 140 miles per hour, so they will meet in 1.5 hours, or at 5:00 PM. 
# CONFIDENCE: I am 95% confident in my answer.


response = openai.ChatCompletion.create( # opens a call to the openai API
    model="gpt-3.5-turbo",  # Chat-based model
    messages=[
        {"role": "user", "content": "If a train traveling at 60 miles per hour departs from City A at 3:00 PM, \
        and another train traveling at 80 miles per hour departs from City B at 3:30 PM toward City A, \
        and the distance between the cities is 240 miles, at what time will the two trains meet? \
        Your answer should be no more than four sentences.\
        Finally, output what percent confident you are in your answer."},
    ],
    # Prompts the model to answer a difficult mathematical word problem
    max_tokens=300,  # Limits the response length
    temperature=0,  # Adjusts temperature, which controls randomness, to be vert deterministic (as are the LMQl queries)
)
# Prints the response
print(response['choices'][0]['message']['content'].strip())
