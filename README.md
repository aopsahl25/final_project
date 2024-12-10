<div align="center">
  <h1>LMQL Tutorial</h1>
  <h4>By Amelia Opsahl </h4>
  <img src="https://lmql.ai/assets/lmql.6950db7a.svg" alt="Alt text" width="300">
  <h2> Exploring an emerging programming language for large language models </h2>
</div>

The Language Model Query Language, or LMQL, is a programming language that was designed with the express purpose of language model interaction. LMQL was developed by the SRI Lab at ETH Zürich and aims to make interactions between the user and language models smoother and more efficient. LMQL is unique in that it combines traditional programming with the ability to call large lanuage models (LLMs) in a user's code, allowing for the integration of LLM interaction natively at the level of program code. 

> <span style="color:gray; opacity:0.7;">For more information on LMQL from its developpers, users can visit the [LMQL website](https://lmql.ai/) or the SRI Lab's [GitHub repository](https://github.com/eth-sri/lmql) on LMQL.</span>

This tutorial gives a more detailed overview of LMQL works, walks through how to get started with LMQL, explores its main features, and evaluates the efectiveness and efficiency of those features in comparison to those of an LLM used without LMQL. For follow-up questions about the tutorial or suggestions for improvement, please contact the author, [Amelia Opsahl](mailto:aopsahl25@cmc.edu).

## Understanding LMQL

An LMQL query is formatted very similary to a standard Python program. However, in an LMQL query top-level strings are interpreted as query strings that are passed to an LLM. For example:
```
@lmql.query
def example():
    '''lmql 
    "Q:How tall is the empire state building?"
    "A: [ANSWER]"
    return ANSWER
    '''
print(example())
```
Program Output: 
```
The Empire State Building is 1,454 feet (443.2 meters) tall.
```
This scenario shows how an LMQL query containing both traditional algorithmic logic and LLM calls can be used to automatically complete template variables like `ANSWER`. Moreover, LMQL queries can leverage natural language prompting to allow for more personalzied outputs to program variables and enhanced model reasoning capabilities. For example:
```
@lmql.query
def example1():
    '''lmql 
    "Q:How tall is the empire state building? Give me just the height in feet without any other informaiton."
    "A: [ANSWER]"
    return ANSWER
    '''
print(example())
```
Program Output: 
```
1,454 feet.
```
Here, we see how algorithmic logic, LLM behavior, and prompt engineering can all come together in LMQL programs to fine-tune program output and efficiently handle complex queries.


## Getting started - LMQL Installation

LMQL can be installed locally on a user's personal computer. This tutorial will walk through example LMQL queries that are run locally from within Python. 

> <span style="color:gray; opacity:0.7;">**Note:** LMQL can also be used via a local instance of a playground IDE. Using the playground instance requires the installation of Node.js, which can be done by following the instructions on the [Node.js](https://nodejs.org/en/download/package-manage) website.</span>

To use LMQL in Python, users can import the `lmql` package, run query code with `lmql.run`, or use a decorator `@lmql.query` for LMQL query functions. This tutorial will use the `@lmql.query` decorator for Pyton integration. The `lmql.run` function is favorable in that it allows users to directly run a string of LMQL code without having to define a function, but this tutorial uses the decorator because of its included support for accessing the surrounding Python environment.

As seen earlier, the `@lmql.query` decorator uses a piece of LMQL code as a Python function, which can then be called from a user's existing code:
```
@lmql.query
def example2(): 
    '''lmql
    "Q: What is the sum of 2+5?"
    "A: [SUM]"
    return SUM
    '''
print(example2())
```
Program Output: 
```
7
```
In terms of query configuration, users can further control query execution by setting the model, decoder, logging parameters, etc. for the query. For example, the following code would override the model and decoder specified in the query program and communicate whether to print verbose logging outputs during execution (e.g., LLM inference parameters). 
```
@lmql.query(model = lmql.model("chatgpt"), decoder = "argmax", verbose=False)
def example3(): 
    '''lmql
    "Q: Name five bird species."
    "A: [SUM]"
    return SUM
    '''
print(example3())
```
Program Output:
```
1. Robin
2. Blue Jay
3. Bald Eagle
4. Hummingbird
5. Pigeon
```

## Prompt Construction

### Basic Features

LMQL uses string interpolation (a technique in which variables are embedded directly into a string) and expressive Python control flows (e.g., loops, conditions, and function calls) to facilitate dynamic prompting and allow for increased structure in the model's output. 

For example:
```
@lmql.query
def scripted_prompting(event):
    '''lmql
    "Q: Output a list of things to bring to an {event}. Each 'thing' should be only one word. \n"
    list = []
    for i in range(5):
        "[THING]" where STOPS_AT(THING, "\n") 
        list.append(THING.strip())
    return list
    '''
print(scripted_prompting("school"))
```
Program output:
```
['Backpack', 'Pencil', 'Notebook', 'Lunch', 'Water bottle']
```
The above program defines an LMQL query template using the `@lmql.query` decorator. The program then uses a Python control flow with a for loop to control for list length. The program also uses string interpolation to allow the user to decide the event for which the packing list is being made. In doing so, the program's prompting process is more interactive and its output increases in structure.

### Multi-Part Prompting

LMQL also uses multi-part prompt programs to enable enhanced controls over the LLM reasoning process and improve the accuracy of the LLM's output.

For example: 
```
@lmql.query
def chain_of_thought(question): 
    '''lmql
    # Q&A prompt template
    "Q: {question}\n"
    "A: Let's find the answer by thinking step by step.\n"
    "[REASONED_ANSWER]"
    return REASONED_ANSWER
    '''
print(chain_of_thought("How many tennis balls fit in the Empire State Building?"))
```
Program output: 
```
First, we need to determine the volume of the Empire State Building.
According to the building's official website, the volume is approximately 37 million cubic feet. 
Next, we need to determine the volume of a standard tennis ball.
According to the International Tennis Federation, the volume of a tennis ball is approximately 2.5 cubic inches. 
Finally, we can calculate the number of tennis balls that can fit in the Empire State Building.
We do this by dividing the volume of the building by the volume of a tennis ball. 
This gives us an estimated answer of 5.9 billion tennis balls.
```
The above program takes a question as an input and outputs both the answer and the reasoning behind it. The model arrives at its answer by using a step-by-step reasoning process as instructed in the internal prompt statement. This chain-of-thought prompting guides the LLM to think more logically about its answer and, in doing so, output a reasoned response based on existing data. 

There are many other ways to encourage the model to follow an intentional reasoning process within the LMQL query. For example, users could modify the internal prompt statement to ask for an answer then ask for the reasoning behind it. Similarly, a user could prompt the model to explain why it arrived at its answer, which would also motivate the model to reevaluate its initial answer and its accuracy.  

## Constrained Text Generation

LMQL allows users to specify a wide range of constraints on the model output. This feature enables advanced output formatting and ensures consistent, predictable responses to scripted prompting (prompts that have a predefined, structured input template). LMQL constraints are high-level and operate on a text, not token, level. This means that LMQL programs automatically translate text-level constraints to token masks to guide the model during generation and output text in the desired format with one generation call only. LMQL constraints are also evaluated eagerly to maximize efficiency. The given constraints are satisfied immiediately during generation, and if it is not possible to satisfy the constraints, valdiation fails early to avoid the cost of producing an invalid output. 

As mentioned, there are various constraints that can be applied to LMQL query outputs. 

### Stopping Phrases

Stopping phrases, which are especially important for scripted prompts, ensure that the model stops decoding once a certain word or symbol has been reached. LMQL executes stopping phrases with the `STOPS_AT` and `STOPS_BEFORE` constraints. These constraints takes two arguments; the name of the variable to which the model output is assigned, and the phrase at which the variable should stop. 

For example: 
```
@lmql.query
def stops_before():
    '''lmql 
    "Tell me a story. It should be 3 setences and include the phrases 'Once upon a time' and 'The end'"
    "[STORY]" where STOPS_BEFORE(STORY, " The end.")
    return STORY
    '''
#print(stops_before())
```
Program Output: 
```
Once upon a time, in a faraway kingdom, there lived a brave knight named Sir William.
He embarked on a quest to defeat a fire-breathing dragon and save the kingdom from destruction.
After a fierce battle, Sir William emerged victorious and the kingdom was saved.
```

The above program outputs a story that ends with 'The End.' However, with the `STOPS_BEFORE` constraint, the text comes to a close right before this closing line.

Simiarly:
```
@lmql.query
def stops_before():
    '''lmql 
    "Tell me a story. It should be 3 setences and include the phrases 'Once upon a time' and 'The end'"
    "[STORY]" where STOPS_AT(STORY, " The end.")
    return STORY
    '''
#print(stops_before())
```
Program Output: 
```
Once upon a time, in a faraway kingdom, there lived a brave knight named Sir William.
He embarked on a quest to defeat a fire-breathing dragon and save the kingdom from destruction.
After a fierce battle, Sir William emerged victorious and the kingdom was saved. The end.
```

The above program outputs an identical story, but this story concludes with the phrase 'The End' because the `STOPS_AT` constraint still includes the second argument that is passed. While both contraints lead to slightly different outputs, they both ensure that the output stops at a certain point - in this case, the very end of a story. 

> <span style="color:gray; opacity:0.7;">**Note:** If multple variables in the query have the same name, the constraint is applied to all of them.</span>

### Number Type Constraints

LMQL also supports number type constraints, which restrict the data type of a generated variable with the `INT` constraint. This guarantees that numbers stay within a valid range and can be used for further calculations in the program.

For example: 
```
@lmql.query()
def num_constraints():
    '''lmql
    "Q: Give me a number between 1 and 100:\n"
    "[N]" where INT(N)
    return N, type(N)
    '''
print(num_constraints())
```
Program Output: 
```
47, <class 'int'>
```
The above program enforces that the model cannot generate tokens that are not an integer, outputting the integer `47` and validating that it is indeed an integer with the `type()` function. 

> <span style="color:gray; opacity:0.7;">**Note:** LMQL currently only supports integer constraints. However, the developpers have announced that support for floating point numbers and other types is planned for future releases.</span>

### Choice From Set

LMQL allows users to restrict a variable to be a choice from specified a set of possible values. This allows for increased user control and interaction with the model, as well as error reduction by giving the model specific, valid options from which to choose.

For example: 
```
@lmql.query
def choice_from_set():
    '''lmql
    "My packing list for the trip:"
    list = []
    for i in range(4):
        "-[THING]" where THING in set(["Volleyball", "Sunscreen", "Bathing Suit", "Book", "Towel"])
        list.append(THING.strip())
    return list
    '''
print(choice_from_set())
```
Program Output:
```
['Sunscreen', 'Bathing Suit', 'Towel', 'Towel']
```
The above program creates a packing list for a trip based on a given set of possible values with the `set` constraint.

### Character Length

Just as in Python, the `len` function can be used in an LMQL query to add constraints on the length of a variable at the character or token level. This ensures that an output is not any longer or shorter than desired, and can also help to guide the model to be more succinct or elaborative in its response. 

For example:
```
@lmql.query
def constrained_length():
    '''lmql 
    "Tell me just a joke, do not tell me the punchline:\n"
    "[JOKE]\n" where len(TOKENS(JOKE)) < 10
    "Now tell me the punchline.\n"
    "A:[PUNCHLINE]\n" where len(TOKENS(PUNCHLINE)) > 1
    return JOKE, PUNCHLINE
    '''
print(constrained_length())
```
Program Output:
```
Why couldn't the bicycle stand up by itself?, Because it was two-tired.
```

The above program uses the `len` function to restrict the length of the joke to be less than ten words and ensure that the punchline for the joke is more than one word. A similar program could be executed at the character level to restrict the amount of charcaters included in the output by removing `TOKENS` as an argument in the `len` function. 

> <span style="color:gray; opacity:0.7;">**Note:** Token length constraints are cheaper to enforce than character length constraints. This is because character length constraints require detokenization and masking, so their character level-length checks are more expesnive than simple length checks on tokenized outputs.</span>

### Regex Constraints

LMQL queries support `REGEX` constraints to allow users to enforce regular expressions during variable generation. This enables LMQL to harness all of the benefits of regular expressions in its programs and outputs, including advanced formatting, style consistency, and text extraction.

For example:
```
@lmql.query()
def regex_constraints():
    '''lmql
    "Today is Christmas in 2024. What is the date?\n"
    "[DATE1]" where REGEX(DATE1, r"[0-9]{2}/[0-9]{2}")
    "What will the date be on new year's day?\n"
    "[DATE2]" where REGEX(DATE2, r"[0-9]{2}/[0-9]{2}")
    return DATE1, DATE2
    '''
print(regex_constraints())
```
Program Output:
```
25/12, 01/01
```
This program outputs dates in DD/MM format without the user needing to explain to the model in an internal prompt what this format means and all of the nuances of its structure.

## Model Measuring

In addition to features involving the prompting and output of queries, LMQL also allows users to derive classification results and confidence scores from program responses. These capabilities helps to improve model decision making by guiding the program to set unstructured text in the context of structured categories, and also plays a part in evaluating the model's accuracy. 

### Classification Results

Classification results can provide a variety of different categorizations, from classifying career types to food groups to geographical regions. One common use case is employing classification results in sentiment analysis. 

For example: 
```
@lmql.query
def results_class():
    '''lmql
    "Generate a two-sentence review for a hotel that you recently stayed at.\n\n"
    "[REVIEW]"
    "Q: What is the underlying sentiment of REVIEW \n"
    "A:[SENTIMENT]" where SENTIMENT in set(["Good", "Bad", "Neutral"])
    "Why did you choose that sentiment?\n"
    "[REASONING]"
    return REVIEW, SENTIMENT, REASONING
    '''
print(results_class())
```
Program Output: 
```
REVIEW: I recently stayed at the Grand Hyatt in New York City and was blown away by the luxurious accommodations and impeccable service.
From the stunning views of the city to the comfortable beds and delicious dining options, this hotel exceeded all of my expectations.
SENTIMENT: Good
REASONING: I chose the sentiment of "good" because the review highlights positive aspects of the hotel and overall had a positive experience.
```

The above program not only generates a review, but it is also able to use this information to identify the response's underlying sentiment and give a reasoned explanation for this interpretation. 

### Confidence Scores

In a more quantitative direction, LMQL queries can output specific measures on how sure they are about their answer. 

For example: 
```
@lmql.query
def confidence_percent(question):
    '''lmql
    "Q: {question}?\n"
    "A: [ANSWER]"
    "What percent confident are you in that answer?\n"
    "[CONFIDENCE]" where INT(CONFIDENCE)
    return ANSWER, f"I am {CONFIDENCE}% certain."
    '''
print(confidence_percent("What is the most populous country in the world?"))
```
Program Output:
```
ANSWER: As of 2021, the most populous country in the world is China, with a population of over 1.4 billion people.
CONFIDENCE: I am 95% certain about my answer.
```

In this program, the model answers a given question and outputs what percent confident it is in its response. While this is not a statistical, evidence-based measure of accuracy compelted by user, it is still a start in guaging how reliable the response may be (e.g., users can feel more confident in an answer with a score of 95% than a score of 2%).

## Tool Augmentation

As mentioned, LMQL can be run locally from within Python and is a superset of the language. This means that LMQL adds new features to Python's functionality, while also maintaining the compatabilities of standard Python code. Thus, LMQL queries can incorporate arbitrary Python constructs to extend LMQL's capabilities and boost query program efficiency.  

### Methods and Functions

One of the simplest ways to include Python constructs in LMQL queries is through the implementation of Python methods (functions associated with an object, that can be called on that object, and that can retrieve information from the object). 

For example: 
```
@lmql.query 
def counting(letter): 
    '''lmql 
    "Give me a sentence with as many words including {letter} as possible.\n"
    "[SENTENCE]"  
    COUNT = SENTENCE.count(letter)  
    return SENTENCE, COUNT  
    '''
print(counting("x"))
```
Program Output: 
```
SENTENCE: The xylophone player expertly executed a complex melody, showcasing their exceptional dexterity and musicality.
COUNT: 6
```

In the above program, the LMQL query uses Python's `count()` method to count how many times a given letter appears in the generated sentence. The ability to implement the `count()` method saves time for users because it allows them to bypass writing a prompt to ask the model to do so. Moreover, it improves the accuracy of the count, as LLMs have been known to struggle with counting [how many times a given letter appears in a word](https://techcrunch.com/2024/08/27/why-ai-cant-spell-strawberry/). 

LMQL's incorporation of Python constructs can also include function calls. 

For example:
```
@lmql.query 
def function_call(): 
    '''lmql 
    "Output a simple math expression for addition. Use real numbers, not variables. \n\n"  
    "[MATH]" where STOPS_BEFORE(MATH, "=")   
    EVAL = eval(MATH)  
    return MATH, EVAL 
    '''
print(function_call())
```
Program Output: 
```
MATH: 2 + 3
eval(MATH): 5
```

In the above program, the LMQL query leverages Python's `eval() ` function to calculate the generated expression in just one call. This increases efficiency as the function eliminates the need to write additional prompting to solve the expression. Compared to the model's output, it is also more certain that the `eval()` function will be able to solve the expression correctly, especially if the expression were more complicated.

### Key-Value Stores

LMQL can also access the surrounding Python interpreter. A practical application of this capability is to use functions defined outside of the LMQL query.

For example: 
```
storage = {}
def assign(key, value): 
    storage[key] = value; return f'{{{key}: "{value}"}}'
def get(key): 
    return storage.get(key)

@lmql.query
def keyvalcomplex(key):
    '''lmql
    "Let's store information about a young professional using the assign and get functions.\
    First, make up information to store information in the assign function\n"
    "[INFO]"
    "Return all of the stored keys and values. Return output in this form: KEYS: key1, key2, key3, VALUES: value1, value2, value3.\
    Only return these words, do not return any information that explains how to get to these words \
    (e.g., do not output any functions)\n"
    "[KEYSANDVALUES]"
    "Return just the {key} of the person in the format of {key}: Value. \
    Only return these words, do not return any information that explains how to get to these words \
    (e.g., do not output any functions)\n"
    "[KEYVAL]"
    return KEYSANDVALUES, KEYVAL
    '''
print(keyvalcomplex("age"))
```
Program Output:
```
KEYSANDVALUES:
KEYS: name, age, occupation, company, salary, education, years_of_experience, skills
VALUES: Sarah Smith, 25, Marketing Manager, XYZ Corporation, $60,000, Bachelor's degree in Marketing, 3, Social media marketing, market research, project management
KEYVAL: Age: 25
```
In the above program, the LMQL query uses the assign() and get() functions, which exist in the surrounding Python interpreter, to guide the model to generate and store information about a hypothetical "young professional" (e.g., their name, age, occupation, etc.). The model is then capable of outputting the stored information, both in the form of all the keys and values, as well a given key-value pair which is decided based on user input of a given key. 

### Text Retrieval

Text retrieval using LMQL's `async` and `await` syntax can also be used to augment the reasoning capabilities of the model queried in LMQL programs and guide the model to extract information from specific data sets. This can be accomplished by incorporating the `asyncio` [library](https://docs.python.org/3/library/asyncio.html) into LMQL queries to run Python coroutines that enable the program to pause execution at certain points and allow other tasks to run in the meantime. In the context of text retrieval, this capability can be used to extract information from high-level API URLs and run LMQL queries specifically on that information.  

For example: 
```
async def fetch_data(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()

async def wikipedia(q):
    try:
        # Clean up the query string
        q = q.strip("\n '.")
        # Wikipedia API URL
        url = f"https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles={q}&origin=*"
        response = await fetch_data(url)
        pages = response.get("query", {}).get("pages", {})
        if pages:
            return list(pages.values())[0].get("extract", "No extract available")[:280]
        else:
            return "No results"
    except Exception as e:
        return f"An error occurred: {str(e)}"

@lmql.query
async def main():
    '''lmql
    "Use wikipedia to summarize the following topic in three sentences:"
    topic = "Python (programming language)"
    summary = await wikipedia(topic)
    print(summary)
    '''
await main()
```
Program Output:
```
Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation.
```
As is clear, the above program uses the `aynscio` library with `async` and `await` syntax to construct a Wikipedia API URL, asynchronously fetch data from Wikipedia using the `fetch_data()` function, process the extract, and pass the result from Wikipedia into the LMQL query engine to condense the extract into a two-sentence summary on the chosen topic. This process enables LMQLs programs to incorporate API URLs and high-level text retrieval and then run queries on the extracted information.


## Evaluation

idea - show how chain of thought makes the prompt more accurate, how other ways of illiciting reasoning do not work as well

increased accuracy - strawberry

## References
















