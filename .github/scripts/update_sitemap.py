import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from lxml import etree
import time

# Configuration
BASE_URL = "https://multiverse-dataverse.netlify.app/"  # Replace with your website URL
OUTPUT_FILE = "sitemap.xml"
INPUT_FILE = "sitemap.xml"  # Input file with the stylesheet and placeholders
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0"
}

visited_urls = set()
queue = set()


def is_valid_url(url):
    """Check if the URL is valid and belongs to the same domain."""
    parsed = urlparse(url)
    return bool(parsed.netloc) and parsed.netloc == urlparse(BASE_URL).netloc


def fetch_links(url):
    """Fetch all valid links from a page."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        links = set()

        for anchor in soup.find_all("a", href=True):
            href = urljoin(url, anchor["href"])
            href_parsed = urlparse(href)
            href = href_parsed.scheme + "://" + href_parsed.netloc + href_parsed.path  # Normalize URL
            if is_valid_url(href):
                links.add(href)

        return links
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return set()


def crawl(url):
    """Crawl the website to gather all unique URLs."""
    queue.add(url)
    while queue:
        current_url = queue.pop()
        if current_url not in visited_urls:
            print(f"Crawling: {current_url}")
            visited_urls.add(current_url)
            new_links = fetch_links(current_url)
            queue.update(new_links - visited_urls)


def create_sitemap(urls):
    """Create an XML sitemap from the crawled URLs, without disturbing the existing content."""
    
    # Read the existing XML file to preserve the XML-stylesheet and placeholders
    with open(INPUT_FILE, 'r', encoding='utf-8') as file:
        xml_content = file.read()

    # Split the XML content at the placeholder comments
    start_comment = "<!--START-->"
    end_comment = "<!--END-->"
    
    start_index = xml_content.find(start_comment) + len(start_comment)
    end_index = xml_content.find(end_comment)
    
    # If placeholders are found, extract the content between them
    if start_index != -1 and end_index != -1:
        before_content = xml_content[:start_index]  # Everything before START
        after_content = xml_content[end_index:]  # Everything after END
        
        # Generate the dynamic content for the sitemap
        dynamic_content = ""
        for url in urls:
            dynamic_content += f"""
            <url>
                <loc>{url}</loc>
                <lastmod>{time.strftime("%Y-%m-%d")}</lastmod>
                <changefreq>daily</changefreq>
                <priority>0.8</priority>
            </url>
            """
        
        # Reconstruct the XML content with dynamic content inserted between the comments
        new_xml_content = f"{before_content}\n{dynamic_content}\n{after_content}"

        return new_xml_content.encode("utf-8")

    # If placeholders are not found, return the original content (should not happen)
    return xml_content.encode("utf-8")


def save_sitemap(content, file_name):
    """Save the sitemap content to a file."""
    with open(file_name, "wb") as file:
        file.write(content)
    print(f"Sitemap saved to {file_name}")


if __name__ == "__main__":
    print("Starting sitemap generation...")
    crawl(BASE_URL)
    print(f"Found {len(visited_urls)} URLs.")
    sitemap_content = create_sitemap(visited_urls)
    save_sitemap(sitemap_content, OUTPUT_FILE)
    print("Sitemap generation completed.")
