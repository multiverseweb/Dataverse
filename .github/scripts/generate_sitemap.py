import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def is_internal_link(base_url, link):
    """Check if a link is internal to the base URL."""
    parsed_base = urlparse(base_url)
    parsed_link = urlparse(link)
    return parsed_link.netloc == parsed_base.netloc or parsed_link.netloc == ''

def generate_sitemap(base_url, output_file="Documentation/sitemap.md"):
    visited = set()
    to_visit = [base_url]

    with open(output_file, "w") as f:
        f.write(f"# Sitemap for {base_url}\n\n")

        while to_visit:
            current_url = to_visit.pop(0)
            if current_url in visited:
                continue

            visited.add(current_url)
            f.write(f"- [{current_url}]({current_url})\n")

            try:
                response = requests.get(current_url, timeout=10)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, "html.parser")
                
                for link in soup.find_all("a", href=True):
                    href = urljoin(base_url, link["href"])
                    if is_internal_link(base_url, href) and href not in visited and href not in to_visit:
                        to_visit.append(href)
            except Exception as e:
                print(f"Error visiting {current_url}: {e}")

if __name__ == "__main__":
    generate_sitemap("https://multiverse-dataverse.netlify.app/")
