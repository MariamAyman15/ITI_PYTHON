from transformers import pipeline, set_seed

# Set up GPT-3 model and tokenizer
model = pipeline('text-generation', 
                 model='EleutherAI/gpt-neo-1.3B', 
                 tokenizer='EleutherAI/gpt-neo-1.3B',
                 device=0) # Use GPU if available

# Set random seed for reproducibility
set_seed(42)

# Prompt user for input and generate responses
while True:
    # Get user input
    prompt = input("You: ")

    # Exit loop if user types "quit"
    if prompt == "quit":
        break

    # Generate response using GPT-3 model
    output = model(prompt, max_length=50, do_sample=True, temperature=0.7)

    # Print generated text
    print("Bot:", output[0]['generated_text'].strip())