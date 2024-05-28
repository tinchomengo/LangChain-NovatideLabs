from langchain_community.chat_models import ChatPerplexity
from langchain_core.prompts import ChatPromptTemplate
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

chat = ChatPerplexity(temperature=0, pplx_api_key="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", model="pplx-70b-online")

system = "You are a helpful assistant."
human = "{input}"
prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

chain = prompt | chat

def get_web_content(topic):
    search_url = f"https://www.google.com/search?q={topic.replace(' ', '+')}"
    print("search_url", search_url)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(search_url)
        
        results = []
        page_content = page.content()
        soup = BeautifulSoup(page_content, 'html.parser')

        for g in soup.find_all('div', class_='tF2Cxc'):
            print("g", g)
            link = g.find('a')['href']
            text_snippet = g.find('h3').get_text() if g.find('h3') else ''
            snippet_text = g.find('span.aCOpRe').get_text() if g.find('span.aCOpRe') else ''
            results.append((text_snippet + " " + snippet_text, link))
        
        browser.close()
    
    print("results", results)
    return results

def get_summarized_web_content(topic):
    web_content = get_web_content(topic)
    
    summarized_content = []
    for text_snippet, link in web_content:
        print("starting summarization")
        print("length of web_content",len(web_content))
        print("text_snippet", text_snippet)
        print("link", link)
        response = chain.invoke({"input": f"Summarize the following text: {text_snippet}"})
        summary = response.content.strip()
        summarized_content.append((summary, link))
    print("ended summarization")
    
    return summarized_content

topic = "5 latest advancements in AI"

summarized_web_content = get_summarized_web_content(topic)

for summary, link in summarized_web_content:
    print("lolxd")
    print(f"Summary: {summary}\nLink: {link}\n")
