# OpenAIPOC

Here is a README file for your project.

OpenAI LLM Quickstart 🚀
This is a simple Python proof-of-concept (POC) that demonstrates how to authenticate with the OpenAI API using environment variables and make synchronous calls to two different LLM models (gpt-4.1-nano and gpt-4.1-mini) within a single function.

Features
Secure API Key Loading: Loads the OPENAI_API_KEY from a .env file using the python-dotenv library.

Simple Function Call: Executes a synchronous API call to the OpenAI Chat Completion endpoint.

Two-Model Example: Demonstrates chaining two prompts using different models for different tasks:

A basic calculation (gpt-4.1-nano).

An IQ question generation (gpt-4.1-mini).

⚙️ Setup and Installation
Follow these steps to set up the project locally.

1. Clone the Repository
Bash

git clone https://github.com/sanskritiut/agenticAI.git
cd agenticAI
2. Create a Virtual Environment (Recommended)
Bash

python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
Install the required Python packages:

Bash

pip install openai python-dotenv
4. Configure Environment Variables
Create a file named .env in the root directory of your project and paste your OpenAI API key into it:

.env

# Replace YOUR_OPENAI_API_KEY_HERE with your actual key
OPENAI_API_KEY="YOUR_OPENAI_API_KEY_HERE"
▶️ How to Run the Code
Execute the main Python script:

Bash

python3 your_script_name.py
(Note: Replace your_script_name.py with the actual name of your file containing the provided code.)

Expected Output
The script will first confirm your API key status and then print the result of the two chained LLM calls:

OpenAI API Key exists
45600
In a system where 'N' represents the number of unique prime factors of an integer 'x', and 'P' represents the set of all divisors of 'x', determine the maximum number of consecutive composite integers that can be generated if the only constraint on 'x' is that 2^N must equal the cardinality of P (i.e., |P|).
🧩 Code Details
The core logic is contained in the callOpenAILLM function:
