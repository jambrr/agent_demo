# Wikipedia Research Summarizer

This Python demo is a simple research assistant that fetches a Wikipedia page for a given topic and generates a concise summary using a language model. It leverages **Wikipedia API**, **Hugging Face Transformers**, and **LangChain** for prompt management.

## Requirements

* Python 3.8+
* `wikipedia-api`
* `transformers`
* `langchain`

## Code Overview

* **Wikipedia Connection**: Uses `wikipediaapi` to retrieve the page content.
* **LLM Summarization**: Uses `facebook/bart-large-cnn` with the `summarization` pipeline from Hugging Face.
* **Prompt Management**: `LangChain` `PromptTemplate` structures the input for summarization.
* **Limitations**: Only the first 3500 characters of the page are summarized to improve speed.

## Installation

```bash
# Clone the repository
git clone <repo-url>
cd <repo-directory>

# Install required packages
pip install wikipedia-api transformers langchain
```

## Usage

1. Run the Python script:

```bash
python research_agent.py
```

2. Enter a Wikipedia topic when prompted:

```
Enter Wikipedia topic to research: 
Machine Learning
```

3. The script will fetch the page and print a summarized version:

```
Summary:
Machine learning is a field of computer science that focuses on algorithms that can learn from data...
```
