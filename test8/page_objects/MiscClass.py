from playwright.sync_api import Page, expect

class MiscClass:

    def __init__(self, page):
        self.page = page

    def generated_0(self, action_arg_0, locator_arg_0, locator_keyword_0, locator_arg_1, locator_keyword_1, locator_arg_2, action_arg_1):
        self.page.goto(action_arg_0)
        self.page.get_by_role(locator_arg_0, name=locator_keyword_0).click()
        expect(self.page.get_by_role(locator_arg_1, name=locator_keyword_1)).to_be_visible()
        expect(self.page.locator(locator_arg_2)).to_contain_text(action_arg_1)

    def generated_1(self, locator_arg_0, action_arg_0, locator_arg_1, locator_keyword_0, locator_arg_2, action_arg_1, locator_arg_3, locator_keyword_1, locator_arg_4, locator_keyword_2, locator_keyword_3):
        expect(self.page.locator(locator_arg_0)).to_contain_text(action_arg_0)
        self.page.get_by_role(locator_arg_1, name=locator_keyword_0).click()
        expect(self.page.locator(locator_arg_2)).to_contain_text(action_arg_1)
        self.page.get_by_role(locator_arg_3, name=locator_keyword_1).click()
        expect(self.page.get_by_role(locator_arg_4, name=locator_keyword_2)).to_be_visible()
        expect(self.page.get_by_role(locator_arg_4, name=locator_keyword_3)).to_be_visible()

    def generated_2(self, locator_arg_0, action_arg_0, locator_arg_1, action_arg_1, locator_arg_2, locator_keyword_0, action_arg_2, locator_arg_3, locator_keyword_1, locator_arg_4, action_arg_3):
        expect(self.page.locator(locator_arg_0)).to_contain_text(action_arg_0)
        self.page.locator('form').filter(has_text=locator_keyword_1).get_by_placeholder(locator_arg_1).fill(action_arg_1)
        self.page.get_by_role(locator_arg_2, name=locator_keyword_0).fill(action_arg_2)
        self.page.get_by_role(locator_arg_3, name=locator_keyword_1).click()
        expect(self.page.locator(locator_arg_4)).to_contain_text(action_arg_3)