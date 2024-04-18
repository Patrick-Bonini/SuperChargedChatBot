import requests
from bs4 import BeautifulSoup

def scrapeWebsite(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            text_content = ' '.join([p.get_text() for p in soup.find_all(['h2', 'h3', 'p', 'table'])])

            title = ' '.join([p.get_text() for p in soup.find_all(['h1'])])
            print(f'topic = {title}')

            formatted_content = f"I want you to act as SolAi, an expert on {title}. Do not include an initial line in the response, only the answer to the request. The user will provide you with details related to a user needing assistance setting up or using {title}, and your role is to suggest the most suitable solution to the user's problem. You should use your knowledge of {title}, coding languages, Linux, etc., in order to develop a comprehensive solution to the problem. The user will provide you with the info, if the user does not seem to have a problem that involves {title} or anything related, you should treat it as a normal request and act as an AI information tool.\n\nHere is your knowledge on {title}: {text_content}"
            
            with open('formatted_prompt.txt', 'w') as file:
                file.write(formatted_content)
            print('Scraping successful. Formatted content saved to "formatted_prompt.txt"')
        else:
            print(f'Failed to scrape URL. Status code: {response.status_code}')

    except Exception as e:
        print(f'{e}\n Defaulting to PubSub+ Platform Documentation')
        # Default to PubSub+ Platform if webscrape is unsuccessful
        scrapeWebsite('https://docs.solace.com/Get-Started/Solace-PubSub-Platform.htm')
