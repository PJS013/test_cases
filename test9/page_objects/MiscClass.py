from playwright.sync_api import Page, expect

class MiscClass:

    def __init__(self, page):
        self.page = page

    def generated_0(self, action_arg_0, locator_arg_0, action_arg_1, locator_arg_1, locator_keyword_0, action_arg_2, locator_keyword_1, action_arg_3, locator_arg_2, action_arg_4):
        self.page.goto(action_arg_0)
        expect(self.page.get_by_role(locator_arg_0)).to_contain_text(action_arg_1)
        self.page.get_by_role(locator_arg_1, name=locator_keyword_0).fill(action_arg_2)
        self.page.get_by_role(locator_arg_1, name=locator_keyword_1).fill(action_arg_3)
        self.page.get_by_role(locator_arg_2, name=action_arg_1).click()
        expect(self.page.get_by_role(locator_arg_0)).to_contain_text(action_arg_4)

    def generated_1(self, action_arg_0, locator_arg_0, locator_keyword_0, action_arg_1, locator_keyword_1, action_arg_2, locator_arg_1, locator_keyword_2):
        self.page.goto(action_arg_0)
        self.page.get_by_role(locator_arg_0, name=locator_keyword_0).fill(action_arg_1)
        self.page.get_by_role(locator_arg_0, name=locator_keyword_1).fill(action_arg_2)
        self.page.get_by_role(locator_arg_1, name=locator_keyword_2).click()