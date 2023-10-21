# gpt-dnd

GOAL: An application that leverages GPT as a dungeon master assistant.

## What is built

gpt-dnd is a python script that interacts with OpenAI's API. The script either takes in a file to use its contents as a prompt for the gpt API or asks for the user's query in the command line and uses that input as the prompt to query the API. It then takes the query and the response from gpt and records the prompt-response pair in a text file. Each prompt-response pair file represents an independent *thread*.

### Threads

To get to a notion of a thread, we need gpt to be able to access the information from previous relevant prompts sent to the API. Normally, when you prompt via the OpenAI API, gpt does not have the context from previous prompts, unless you provide this context in the prompt itself. So if you tell the gpt API your name in one prompt, and then ask what your name is in the next prompt, it will respond as if it doesn't know.

However, with gpt-dnd, for each query to the API, you must specify a prompt-response file. Moreover, for each new prompt using the same prompt-response file, gpt-dnd will append the contents of that prompt-response file as context for that new prompt. In this way, if you told gpt that "my name is Bob" in one prompt using `prompt-response-file.txt`, for example, as long as you were using `prompt-response-file.txt` for your next prompt, you could then ask what your name was in the new prompt 
and gpt would have the information available to answer via the appended context.

## Getting Started

First, clone the repo to your local workspace.

### Entering the Prompt without Using a File

Then, to enter the prompt without using a file as the prompt, enter the following specifying the name of the prompt-response file you want to use:

```bash
python3 openaiget.py <prompt-response-file> 
```

If the file you specify does not already exist, then the script will create it for you.

The script will then ask you for your prompt:

```bash
Enter your query:
```

After you enter your query via the command line, the script will take that text you entered as well as take the contents of the prompt-response file you specified as context, and create a prompt with the combined information to send to the gpt API. Of course, for the first prompt of a new thread, the specified prompt-response file will have no contents and thus add no context to add.

### Entering the Prompt Using a File

You do not need to type in your prompt via the command line. You can instead specify another file and the contents of that file will be used as the prompt. A prompt-response file must still be specified to define the thread:

```bash
python3 openaiget.py <path-to-prompt-response-file> <path-to-prompt-file>
```



