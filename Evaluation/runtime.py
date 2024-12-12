import time # Imports the 'time' module, which provides various time-related functions
import openai  # Imports the OpenAI library for interacting with OpenAI's APIs
from dotenv import load_dotenv  # Imports the 'load_dotenv' function to load environment variables from a .env file
import os  # Imports the 'os' module to interact with the operating system (used here for fetching environment variables)

#Load API key and organization ID from .env file
load_dotenv(dotenv_path='.env')

# Set API credentials
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPENAI_ORG_ID")

# The following programs ask the model a question, output its question, and calculate the run-time of the program.

start = time.time() # Records the current time (in seconds since the epoch) and stores it in the 'start' variable.
response = openai.ChatCompletion.create( # opens a call to the openai API
    model="gpt-3.5-turbo",  # Chat-based model
    messages=[
        {"role": "user", "content": "If a train traveling at 60 miles per hour departs from City A at 3:00 PM, \
        and another train traveling at 80 miles per hour departs from City B at 3:30 PM toward City A, \
        and the distance between the cities is 240 miles, at what time will the two trains meet? \
        Your answer should be no more than five sentences."},
    ],
    # Prompts the model to answer a difficult mathematical word problem
    max_tokens=300,  # Limits the response length
    temperature=0,  # Adjusts temperature, which controls randomness, to be vert deterministic (as are the LMQl queries)
)
# Prints the response
print(response['choices'][0]['message']['content'].strip())
stop = time.time()  # Records the current time after the code execution and stores it in the 'stop' variable.
print(stop - start)  # Calculates and prints the elapsed time by subtracting the start time from the stop time.


start1 = time.time() # Records the current time (in seconds since the epoch) and stores it in the 'start' variable.
response1 = openai.ChatCompletion.create( # opens a call to the openai API
    model="gpt-3.5-turbo",  # Chat-based model
    messages=[
        {"role": "user", "content": "Summarize 1984 by George Orwell. \
        Your answer should be no more than five sentences."},
    ],
    # Prompts the model to answer a difficult mathematical word problem
    max_tokens=300,  # Limits the response length
    temperature=0,  # Adjusts temperature, which controls randomness, to be vert deterministic (as are the LMQl queries)
)
# Prints the response
print(response1['choices'][0]['message']['content'].strip())
stop1 = time.time()  # Records the current time after the code execution and stores it in the 'stop' variable.
print(stop1 - start1)  # Calculates and prints the elapsed time by subtracting the start time from the stop time.


start2 = time.time() # Records the current time (in seconds since the epoch) and stores it in the 'start' variable.
response2 = openai.ChatCompletion.create( # opens a call to the openai API
    model="gpt-3.5-turbo",  # Chat-based model
    messages=[
        {"role": "user", "content": "How did the Treaty of Versailles contribute to the rise of World War II, \
        particularly in terms of its impact on Germany's economy and political climate? \
        Your answer should be no more than five sentences. \n\n"},
    ],
    # Prompts the model to answer a difficult mathematical word problem
    max_tokens=300,  # Limits the response length
    temperature=0,  # Adjusts temperature, which controls randomness, to be vert deterministic (as are the LMQl queries)
)
# Prints the response
print(response2['choices'][0]['message']['content'].strip())
stop2 = time.time()  # Records the current time after the code execution and stores it in the 'stop' variable.
print(stop2 - start2)  # Calculates and prints the elapsed time by subtracting the start time from the stop time.


start3 = time.time() # Records the current time (in seconds since the epoch) and stores it in the 'start' variable.
response3 = openai.ChatCompletion.create( # opens a call to the openai API
    model="gpt-3.5-turbo",  # Chat-based model
    messages=[
        {"role": "user", "content": "Write a short story about a man who can fly. \
        Your answer should be no more than five sentences. \n\n"},
    ],
    # Prompts the model to answer a difficult mathematical word problem
    max_tokens=300,  # Limits the response length
    temperature=0,  # Adjusts temperature, which controls randomness, to be vert deterministic (as are the LMQl queries)
)
# Prints the response
print(response3['choices'][0]['message']['content'].strip())
stop3 = time.time()  # Records the current time after the code execution and stores it in the 'stop' variable.
print(stop3 - start3)  # Calculates and prints the elapsed time by subtracting the start time from the stop time.


start4 = time.time() # Records the current time (in seconds since the epoch) and stores it in the 'start' variable.
response4 = openai.ChatCompletion.create( # opens a call to the openai API
    model="gpt-3.5-turbo",  # Chat-based model
    messages=[
        {"role": "user", "content": "Analyse why Donald Trump won the 2024 election. \
        Your answer should be no more than five sentences. \n\n"},
    ],
    # Prompts the model to answer a difficult mathematical word problem
    max_tokens=300,  # Limits the response length
    temperature=0,  # Adjusts temperature, which controls randomness, to be vert deterministic (as are the LMQl queries)
)
# Prints the response
print(response4['choices'][0]['message']['content'].strip())
stop4 = time.time()  # Records the current time after the code execution and stores it in the 'stop' variable.
print(stop4 - start4)  # Calculates and prints the elapsed time by subtracting the start time from the stop time.


start5 = time.time() # Records the current time (in seconds since the epoch) and stores it in the 'start' variable.
response5 = openai.ChatCompletion.create( # opens a call to the openai API
    model="gpt-3.5-turbo",  # Chat-based model
    messages=[
        {"role": "user", "content": "Imagine a future where quantum computing has revolutionized information security, medicine, and climate modeling. \
        Describe the possible social, economic, and ethical impacts of this technology. Your answer should be no more than five sentences. \n\n"},
    ],
    # Prompts the model to answer a difficult mathematical word problem
    max_tokens=300,  # Limits the response length
    temperature=0,  # Adjusts temperature, which controls randomness, to be vert deterministic (as are the LMQl queries)
)
# Prints the response
print(response5['choices'][0]['message']['content'].strip())
stop5 = time.time()  # Records the current time after the code execution and stores it in the 'stop' variable.
print(stop5 - start5)  # Calculates and prints the elapsed time by subtracting the start time from the stop time.


start6 = time.time() # Records the current time (in seconds since the epoch) and stores it in the 'start' variable.
response6 = openai.ChatCompletion.create( # opens a call to the openai API
    model="gpt-3.5-turbo",  # Chat-based model
    messages=[
        {"role": "user", "content": "A car rental company charges a fixed fee of $50 per day plus $0.20 per mile driven. \
      If a customer rents a car for 5 days and drives a total of 300 miles, \
      how much will the customer pay in total for the rental? \
      Your answer should be no more than five sentences. \n\n"},
    ],
    # Prompts the model to answer a difficult mathematical word problem
    max_tokens=300,  # Limits the response length
    temperature=0,  # Adjusts temperature, which controls randomness, to be vert deterministic (as are the LMQl queries)
)
# Prints the response
print(response6['choices'][0]['message']['content'].strip())
stop6 = time.time()  # Records the current time after the code execution and stores it in the 'stop' variable.
print(stop6 - start6)  # Calculates and prints the elapsed time by subtracting the start time from the stop time.


start7 = time.time() # Records the current time (in seconds since the epoch) and stores it in the 'start' variable.
response7 = openai.ChatCompletion.create( # opens a call to the openai API
    model="gpt-3.5-turbo",  # Chat-based model
    messages=[
        {"role": "user", "content": "A factory produces Type A and Type B products. \
        Each Type A requires 3 hours of labor and 2 units of material \
        while each Type B requires 5 hours of labor and 4 units of material. \
        The factory has 240 hours of labor and 180 units of material. \
        If the profit from each Type A is $30 and each Type B is $50, \
        how many of each product should the factory make to maximize its profit? \
        You answers should be no longer than five sentences "},
    ],
    # Prompts the model to answer a difficult mathematical word problem
    max_tokens=300,  # Limits the response length
    temperature=0,  # Adjusts temperature, which controls randomness, to be vert deterministic (as are the LMQl queries)
)
# Prints the response
print(response7['choices'][0]['message']['content'].strip())
stop7 = time.time()  # Records the current time after the code execution and stores it in the 'stop' variable.
print(stop7 - start7)  # Calculates and prints the elapsed time by subtracting the start time from the stop time.


start8 = time.time() # Records the current time (in seconds since the epoch) and stores it in the 'start' variable.
response8 = openai.ChatCompletion.create( # opens a call to the openai API
    model="gpt-3.5-turbo",  # Chat-based model
    messages=[
        {"role": "user", "content": "A pizza place sells two sizes of pizzas: small and large. \
        A small pizza costs $8 and a large pizza costs $12. \
        If a customer buys 3 small pizzas and 2 large pizzas, how much will the total cost be? \
        Your answer should be no more than five sentences.\n\n"},
    ],
    # Prompts the model to answer a difficult mathematical word problem
    max_tokens=300,  # Limits the response length
    temperature=0,  # Adjusts temperature, which controls randomness, to be vert deterministic (as are the LMQl queries)
)
# Prints the response
print(response8['choices'][0]['message']['content'].strip())
stop8 = time.time()  # Records the current time after the code execution and stores it in the 'stop' variable.
print(stop8 - start8)  # Calculates and prints the elapsed time by subtracting the start time from the stop time.


start9 = time.time() # Records the current time (in seconds since the epoch) and stores it in the 'start' variable.
response9 = openai.ChatCompletion.create( # opens a call to the openai API
    model="gpt-3.5-turbo",  # Chat-based model
    messages=[
        {"role": "user", "content": "A train travels at 60 miles per hour for the first 3 hours, \
        then reduces its speed to 45 miles per hour for the next 2 hours. \
        How long will it take the train to travel a total of 225 miles?\
        Your answer should be no more than five sentences."},
    ],
    # Prompts the model to answer a difficult mathematical word problem
    max_tokens=300,  # Limits the response length
    temperature=0,  # Adjusts temperature, which controls randomness, to be vert deterministic (as are the LMQl queries)
)
# Prints the response
print(response9['choices'][0]['message']['content'].strip())
stop9 = time.time()  # Records the current time after the code execution and stores it in the 'stop' variable.
print(stop9 - start9)  # Calculates and prints the elapsed time by subtracting the start time from the stop time.


