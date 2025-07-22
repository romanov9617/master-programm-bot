import requests
from bs4 import BeautifulSoup


def fetch_program_page(url: str) -> BeautifulSoup:
    """Скачивает страницу и возвращает объект BeautifulSoup."""
    response = requests.get(url)
    response.raise_for_status()  # выкинет исключение, если статус != 200
    return BeautifulSoup(response.text, "html.parser")


def parse_sections(soup: BeautifulSoup) -> dict:
    """
    Находит все основные разделы страницы:
    - заголовки h2
    - связанный с ними контент (до следующего h2)
    Возвращает словарь {заголовок: текст содержимого}.
    """
    sections = {}
    for header in soup.find_all("h2"):
        title = header.get_text(strip=True)
        content_parts = []
        # идём по всем следующим соседям, пока не встретим следующий h2
        for sib in header.find_next_siblings():
            if sib.name == "h2":
                break
            content_parts.append(sib.get_text(separator="\n", strip=True))
        sections[title] = "\n".join(filter(None, content_parts))
    return sections
