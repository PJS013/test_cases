from playwright.sync_api import Page, expect

class MiscClass:

    def __init__(self, page, loginpage):
        self.page = page
        self.loginpage = loginpage

    def generated_0(self, action_keyword_0, action_keyword_1, action_keyword_2, locator_arg_0):
        self.loginpage.login(locator=action_keyword_0, login=action_keyword_1, password=action_keyword_2)
        expect(self.page.locator(locator_arg_0)).to_be_visible()

    def generated_1(self, action_keyword_0, action_keyword_1, action_keyword_2, locator_arg_0, action_arg_0):
        self.loginpage.login(locator=action_keyword_0, login=action_keyword_1, password=action_keyword_2)
        expect(self.page.locator(locator_arg_0)).to_contain_text(action_arg_0)
        self.page.close()

    def generated_2(self, locator_arg_0, locator_arg_1):
        self.page.locator(locator_arg_0).click()
        self.page.locator(locator_arg_1).click()

    def generated_3(self, locator_arg_0, action_arg_0, locator_arg_1):
        self.page.locator(locator_arg_0).fill(action_arg_0)
        self.page.locator(locator_arg_1).fill(action_arg_0)

    def generated_4(self, locator_arg_0, action_arg_0, locator_arg_1):
        expect(self.page.locator(locator_arg_0)).to_contain_text(action_arg_0)
        self.page.locator(locator_arg_1).click()