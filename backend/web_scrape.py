import requests
from bs4 import BeautifulSoup
import autopep8

def scrapeWebsite(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            text_content = ' '.join([p.get_text() for p in soup.find_all(['h2', 'h3', 'p', 'table'])])

            title = ' '.join([p.get_text() for p in soup.find_all(['h1'])])
            print(f'topic = {title}')

            formatted_content = f"As Solly, an expert on {title}, your task is to provide brief and precise assistance to users seeking help with {title}. Respond directly to user queries without introductory lines. Use your expertise in {title}, coding, Linux, etc., to offer concise solutions in 150 characters or less. If the inquiry doesn't relate to {title}, respond as a general AI assistant or guide users to relevant documentation. Your {title} knowledge: {text_content}"

            formatted_content = autopep8.fix_code(formatted_content, options={'aggressive': 1})

            with open('formatted_prompt.txt', 'w') as file:
                file.write(formatted_content)
            print('Scraping successful. Formatted content saved to "formatted_prompt.txt"')
        else:
            print(f'Failed to scrape URL. Status code: {response.status_code}')

    except Exception as e:
        print(f'{e}\n Defaulting to PubSub+ Platform Documentation')
        # Default to PubSub+ Platform if webscrape is unsuccessful
        scrapeWebsite('https://docs.solace.com/API/SDKPerf/SDKPerf.htm')

scrapeWebsite('https://docs.solace.com/API/SDKPerf/SDKPerf.htm')