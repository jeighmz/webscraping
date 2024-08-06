import requests
import os
import xml.etree.ElementTree as ET

def fetch_papers(topic, max_results=5):
    base_url = "http://export.arxiv.org/api/query?"
    query = f"search_query=all:{'+'.join(topic.split())}&start=0&max_results={max_results}"
    response = requests.get(base_url + query)
    return response.content

def parse_papers(xml_content):
    root = ET.fromstring(xml_content)
    papers = []
    for entry in root.findall('{http://www.w3.org/2005/Atom}entry'):
        paper = {
            'title': entry.find('{http://www.w3.org/2005/Atom}title').text,
            'authors': [author.find('{http://www.w3.org/2005/Atom}name').text for author in entry.findall('{http://www.w3.org/2005/Atom}author')],
            'published_date': entry.find('{http://www.w3.org/2005/Atom}published').text,
            'link': entry.find('{http://www.w3.org/2005/Atom}id').text
        }
        papers.append(paper)
    return papers

def save_papers_to_file(papers, topic):
    directory = "data/docs"
    os.makedirs(directory, exist_ok=True)
    file_path = os.path.join(directory, f"{topic.replace(' ', '_')}.txt")
    
    with open(file_path, 'w') as file:
        for paper in papers:
            authors = ', '.join(paper['authors'])
            arxiv_id = paper['link'].split('/')[-1]
            pdf_link = f"https://arxiv.org/pdf/{arxiv_id}"
            file.write(f"Title: {paper['title']}\n")
            file.write(f"Authors: {authors}\n")
            file.write(f"Published: {paper['published_date']}\n")
            file.write(f"Link: {pdf_link}\n\n")
    print(f"Results saved to {file_path}")

def main():
    topic = input("Enter the topic to search for papers: ").strip()
    max_results = int(input("Enter the maximum number of results to fetch: ").strip())
    xml_content = fetch_papers(topic, max_results)
    papers = parse_papers(xml_content)
    save_papers_to_file(papers, topic)

if __name__ == "__main__":
    main()