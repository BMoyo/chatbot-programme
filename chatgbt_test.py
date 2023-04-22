# A program to simulate a chat with the chatGBT bot using the ChatGBT API and python.
import sys
import openai
import key

# Validating the unique APIkey given by ChatGPT, to allow access to use the API.
openai.api_key = key.api_key

# Setting up the model behavior for conversation
messages = [{
    "role": "system",
    "content": "You are a helpful Assistant"
}]

while True:
    # getting instruction from the user
    content = input("User : ")

    # if message exists and is not exit program instruction then open message and pass message as content for the
    # user role.
    if content != 'StopProg':
        messages.append({
            "role": "user",
            "content": content
        })

        # creating the chat object and determining the chatbot variables to be used.
        completion = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=messages
        )
    else:
        # Code to close the program if exit program instruction is given
        print("!!!!!!!!!\t PROGRAM HAS BEEN STOPPED \t!!!!!!!!!")
        sys.exit()

    # Storing the response from the program and printing it out
    response = completion.choices[0].message.content
    print(f'ChatGPT: {response}')

    # Storing the response within the assistant role so chatGPT can temporally store its responses.
    messages.append({"role": "assistant", 'content': response})
