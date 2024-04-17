import requests
from bs4 import BeautifulSoup

url = 'https://docs.solace.com/API/SDKPerf/Command-Line-Options.htm'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    text_content = ' '.join([p.get_text() for p in soup.find_all('p')])

    formatted_content = f"I want you to act as SolAi, an expert on SDKPerf. Do not include an initial line in the response, only the answer to the request. The user will provide you with details related to a user needing assistance setting up or using SDKPerf, and your role is to suggest the most suitable solution to the user's problem. You should use your knowledge of SDKPerf, coding languages, Linux, etc., in order to develop a comprehensive solution to the problem. The user will provide you with the info, if the user does not seem to have a problem that involves SDKPerf or anything related, you should treat it as a normal request and act as an AI information tool.\n\nHere is your knowledge on SDKPerf: {text_content}"
    
    with open('formatted_sdkperf.txt', 'w') as file:
        file.write(formatted_content)
    print('Scraping successful. Formatted content saved to "formatted_sdkperf.txt"')
else:
    print(f'Failed to scrape URL. Status code: {response.status_code}')
