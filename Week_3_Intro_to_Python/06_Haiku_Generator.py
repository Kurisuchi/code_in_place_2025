from ai import call_gpt

# Creates a haiku based on the inputs you provided using AI
def main():
    # Asks for your name
    name_input = input("Enter your name: ")

    # Asks for a topic
    topic_input = input("Enter a topic: ")

    # Indicates that your haiku is being generated
    print("Creating your haiku...\n")

    # Call AI to generate your haiku
    haiku_output = call_gpt("Can you create a haiku using the following inputs? " + name_input + " and " + topic_input)

    # Print out the haiku
    print(haiku_output)

if __name__ == "__main__":
    main()