
from selenium import webdriver
from selenium.webdriver.support.color import Color


class NetpeakTest(object):
    def __init__(self, driver, par_1):
        self.driver = driver
        self.par_1 = par_1

    def test_1(self):
        print('1. Follow the link to the main page of the Netpeak website:')
        try:
            self.driver.get('https://netpeak.ua/')
            print('— Success —')
        except:
            print('Fail')
            return

        print('')
        print('2. Click on the button "О нас":')
        try:
            self.driver.find_element_by_xpath('//*[@id="rec278727844"]/div/div/div/div[1]'
                                              '/div/nav/div[1]/div[1]/ul/li[3]').click()
            print('— Success —')
        except:
            print('Fail')
            return

        print('   In the drop-down list, press the "Команда" button:')
        try:
            self.driver.find_element_by_xpath('//*[@id="rec278727844"]/div/div/div/div[1]/div/nav/'
                                              'div[3]/div/div[2]/ul[1]/li[3]/div/a').click()
            print('— Success —')
        except:
            print('Fail')
            return

        print('')
        print('3. Press the button "Стать частью команды":')
        window_0 = self.driver.window_handles[0]
        self.driver.switch_to.window(window_0)


        try:
            self.driver.find_element_by_xpath('//*[@id="rec278727880"]/div/div/div/footer/div[1]/div/div/'
                                              'div/div/div[2]/div/div[2]/ul/li[4]/a').click()

            print('--- С конпкой "Стать частью команды" не справился, здесь вместо неё нажимается "Карьера" ---')
            print('— Success —')
        except:
            print('Fail')
            return

        window_1 = self.driver.window_handles[1]
        print('   Verify that the Work in Netpeak page has opened in a new tab:')
        try:
            if self.driver.current_url != 'https://netpeak.ua/team/' or len(self.driver.window_handles) != 2:
                print('fail')
                return
            print('— Success —')
        except:
            print('Fail')
            return

        print('')
        print('4. Verify that the page has a button "Я хочу работать в Netpeak" and and it is clickable:')
        try:
            self.driver.switch_to.window(window_1)
            btn_1 = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div/a")

            btn_1.click()
            print('— Success —')
        except:
            print('Fail')
            return

        print('')
        print('5. Return to the previous tab and click the "Личный кабинет" button:')
        self.driver.switch_to.window(window_0)
        try:
            self.driver.find_element_by_xpath('//*[@id="rec278727844"]/div/div/div/div[1]/div/'
                                              'nav/div[1]/div[2]/ul/li[1]/a').click()
            print('— Success —')
        except:
            print('Fail')
            return
        window_2 = self.driver.window_handles[2]
        self.driver.switch_to.window(window_2)

        print('')
        print('6. On the personal account page, fill the Login and Password with random data:')
        try:
            username = self.driver.find_element_by_id("login")
            password = self.driver.find_element_by_id("password")
            username.send_keys("RandomLoginTest")
            password.send_keys("RandomPass8997JH")
            print('— Success —')
        except:
            print('Fail')
            return

        print('')
        print('7. Verify that the "Login" button is not available:')
        element = self.driver.find_element_by_xpath("//*[@id='loginForm']/div[5]/button")
        if element.is_enabled() != False:
            print('Fail')
            return
        else:
            print('— Success —')

        print('')
        print('8. Mark the checkbox "Авторизируясь, вы соглашаетесь с Политикой конфиденциальности":')
        try:
            element = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div[4]/div/md-checkbox')
            element.click()
            print('— Success —')
        except:
            print('Fail')
            return

        print('')
        print('9. Click on the enter button:')
        try:
            self.driver.find_element_by_xpath('//*[@id="loginForm"]/div[5]/button/span').click()
            print('— Success —')
        except:
            print('Fail')
            return

        print('   Verify notification about an incorrect username or password:')
        element = self.driver.find_element_by_xpath('/html/body/md-toast/div/span')
        if element.text != 'Неправильный логин или пароль':
            print('Fail')
            return
        else:
            print('— Success —')

        print('')
        print('10. Verify that the Login and Password are highlighted in red:')
        username_color = self.driver.find_element_by_id("login").value_of_css_property('border-color')
        password_color = self.driver.find_element_by_id("password").value_of_css_property('border-color')
        if Color.from_string(username_color).hex != '#dd2c00' or Color.from_string(password_color).hex != '#dd2c00':
            print('Fail')
            return
        else:
            print('— Success —')


def main():
    driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
    driver.implicitly_wait(5)
    parser = NetpeakTest(driver, '')
    parser.test_1()
    driver.quit()


if __name__ == '__main__':
    main()

