def test_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.implicitly_wait(5)
    browser.get(link)
    btn = browser.find_elements_by_css_selector('[class="btn btn-lg btn-primary btn-add-to-basket"]')
    assert btn, "Кнопка не найдена!"