# ФИО: Ткачев Матвей Александрович
# Дата: 12-11-22026
# Время: 17:04
# Я написал код playwright codegen demo.playwright.dev/todomvc в терминал и у меня открылось туду
# В ней я начал проверять видно ли символы, текст который я написал, можно ли кликнуть 



import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_role("heading", name="todos").click()
    expect(page.get_by_placeholder("What needs to be done?")).to_be_visible()
    page.get_by_test_id("todo-title").click()
    expect(page.get_by_label("Delete")).to_be_visible()
    expect(page.get_by_test_id("todo-title")).to_contain_text("i love bilyard")
    page.get_by_role("link", name="real TodoMVC app.").click()
    expect(page.get_by_test_id("todo-title")).to_contain_text("i love bilyard")
    expect(page.get_by_test_id("todo-title")).to_contain_text("i love bilyard")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
