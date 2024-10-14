import openai

# Set up OpenAI API key
openai.api_key = 'your_openai_api_key'

def generate_c_program(prompt):
    # Query OpenAI to generate C code based on the prompt
    response = openai.Completion.create(
        engine="text-davinci-003",  # GPT-4 or equivalent engine
        prompt=f"Write a C program that {prompt}",
        temperature=0.7,
        max_tokens=200,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

def chatbot():
    print("Welcome to the C Program Generator!")
    print("Tell me what kind of C program you need.")
    
    while True:
        user_input = input("You: ")

        if user_input.lower() in ['exit', 'quit', 'stop']:
            print("Goodbye!")
            break

        print("Generating C program...")
        c_program = generate_c_program(user_input)
        print("\nGenerated C Program:\n")
        print(c_program)
        print("\n---\n")

if __name__ == "__main__":
    chatbot()
