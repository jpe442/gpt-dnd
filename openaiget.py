import openai
import os
import sys

openai.api_key = os.environ.get('OPENAI_API_KEY')
if not openai.api_key:
    raise ValueError("Please set the OPENAI_API_KEY environment variable.")

def ask_gpt(context, query):
    prompt = context + "\n" + query
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

def save_to_txt(query, response, filename="query_response.txt"):
    with open(filename, 'a') as f:
        f.write(f"Query: {query}\n")
        f.write(f"Response: {response}\n")
        f.write("="*50 + "\n")

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <thread_file> [query_file]")
        sys.exit(1)
    
    thread_file = sys.argv[1]

    context = ""
    if os.path.exists(thread_file):
        try:
            with open(thread_file, 'r') as file:
                context = file.read().strip()
        except Exception as e:
            print(f"Error reading thread file: {e}")
            sys.exit(1)

    if len(sys.argv) >= 3:
        query_file = sys.argv[2]
        try:
            with open(query_file, 'r') as file:
                query = file.read().strip()
        except Exception as e:
            print(f"Error reading query file: {e}")
            sys.exit(1)
    else:
        query = input("Enter your query: ")
    
    response = ask_gpt(context, query)
    print(f"Response: {response}")
    save_to_txt(query, response, thread_file)

if __name__ == "__main__":
    main()
