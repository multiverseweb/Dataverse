import requests
from bs4 import BeautifulSoup

def generate_sitemap(base_url, output_file="Documentation/sitemap.md"):
    visited = set()
    to_visit = [base_url]

    with open(output_file, "w") as f:
        f.write(f"# Sitemap for {base_url}\n\n")

        while to_visit:
            url = to_visit.pop(0)
            if url in visited:
                continue

            visited.add(url)
            f.write(f"- [{url}]({url})\n")

            try:
                response = requests.get(url)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, "html.parser")
                for link in soup.find_all("a", href=True):
                    href = link["href"]
                    if href.startswith(base_url) and href not in visited:
                        to_visit.append(href)
            except Exception as e:
                print(f"Error visiting {url}: {e}")

if __name__ == "__main__":
    generate_sitemap("https://multiverse-dataverse.netlify.app/")
