# Promptflow Workshop
<img width="621" alt="Screenshot 2024-05-16 at 16 17 11" src="https://github.com/mariia-ascent/promptflow_workshop/assets/148238788/bef1c569-79b9-4c49-b432-f2341b40f1f8">

# PromptFlow Iherb assistant Chatbot Engine

## Overview
This repository contains the implementation of PromptFlow, a sophisticated chatbot engine designed to handle various types of user inputs efficiently and dynamically. The chatbot classifies inputs, processes them according to their categories—such as chitchat, product information requests, or Wikipedia-based queries—and generates appropriate outputs.

## Features
- **Input Classification**: Determines whether a user input is casual chitchat, a specific product inquiry, or a question suitable for a Wikipedia search.
- **Product Information Handling**: Fetches product details based on user specifications using SQL queries.
- **Wikipedia Search**: Performs an automated search for general knowledge questions and retrieves information from Wikipedia.
- **Dynamic Flow Management**: Redirects process flows based on the classification results, handling each type of query with a specialized approach.

## Flow Description
The chatbot operates as follows:
1. **Input Reception**: Receives user inputs and classifies them into distinct categories.
2. **Query Handling**:
   - **Chitchat**: Directly processes informal conversations.
   - **Product Search**: Generates and executes SQL queries based on the user's detailed requirements.
   - **Wikipedia Queries**: Searches for and processes information from Wikipedia URLs.
3. **Output Generation**: Compiles the response based on the retrieved data or interaction and presents it back to the user.

The included flow diagram illustrates the process branches and operational logic.
