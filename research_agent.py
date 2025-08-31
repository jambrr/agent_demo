import wikipediaapi
from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from transformers.utils.logging import set_verbosity_error

set_verbosity_error()

# prepare your model
model = pipeline("summarization", model="facebook/bart-large-cnn")
llm = HuggingFacePipeline(pipeline=model)

# connect to Wikipedia
wiki = wikipediaapi.Wikipedia(language="en", user_agent="researcher")

# define the prompt template
template = PromptTemplate.from_template(
    "Summarize the following Wikipedia text: \n\n{text}"
)

summarizer_chain = template | llm

# ask user for topic
topic = input("Enter Wikipedia topic to research: \n")

# fetch Wikipedia page
page = wiki.page(topic)

if not page.exists():
    print(f"No Wikipedia page found for '{topic}'")
else:
    text_to_summarize = page.text[:3500]  # limit for speed
    summary = summarizer_chain.invoke({"text": text_to_summarize})

    print("\nSummary:")
    print(summary)
