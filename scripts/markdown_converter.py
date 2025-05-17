import os
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()

# Initialize the OpenAI client
client = OpenAI()

# return markdown from urls; it accepts a url and length of the content to return
def convert_to_markdown(urls: list[str], length: int = 1000) -> str:
    return "Hello, world!"

if __name__ == "__main__":
    urls = ["https://www.google.com", "https://www.youtube.com"]  
    print(convert_to_markdown(urls, 1000))