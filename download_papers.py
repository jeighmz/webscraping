import os
import requests

def download_pdf(link, title, topic):
    # Create the directory for the topic if it doesn't exist
    directory = f"data/docs/pdf/{topic}"
    os.makedirs(directory, exist_ok=True)
    
    # Generate a valid filename
    filename = f"{directory}/{title}.pdf"
    
    try:
        # Send GET request to the link
        response = requests.get(link)
        
        # Check if the response contains a PDF
        if response.headers['Content-Type'] == 'application/pdf':
            # Save the PDF to the file
            with open(filename, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded: {filename}")
        else:
            print(f"Failed to download {link}: Content is not a PDF")
    except Exception as e:
        print(f"Failed to download {link}: {e}")

def read_links_and_download(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            topic = os.path.splitext(os.path.basename(file_path))[0].replace(" ", "_")
            for i in range(len(lines)):
                if lines[i].startswith("Title:"):
                    title = lines[i].split("Title: ")[1].strip().replace(" ", "_")
                if lines[i].startswith("Link:"):
                    link = lines[i].split("Link: ")[1].strip()
                    arxiv_id = link.split('/')[-1]
                    pdf_link = f"https://arxiv.org/pdf/{arxiv_id}"
                    download_pdf(pdf_link, title, topic)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Path to the file containing the research paper details
    file_path = input("Enter the path to the text file with research paper details: ").strip()
    read_links_and_download(file_path)