
# ФИО: Ткачев Матвей Александрович
# Дата: 2026-11-11
# Время: 17:32
# Описание: Этот код запускает браузер Chromium, открывает страницу
# playwright.dev и проверяет, что заголовок страницы содержит слово "Playwright".
# Я скопировал пример из раздела "Writing tests" и запустил его локально.import re
# Я сделал так чтобы код смотрел наличие текста на странице






import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")
    expect(page).to_have_title(re.compile("Playwright"))


def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_contain_text("Installation")

    # Правильный URL после клика:
    expect(page).to_have_url("https://playwright.dev/docs/intro")