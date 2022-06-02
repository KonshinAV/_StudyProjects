import pickle
from selenium import webdriver
from time import sleep


def get_cookies_dump (browser, link, time_to_login = 15, file_name = 'session'):
    """
    Cookies dump function. Create dump -to file.

    :param browser: obj.webdriver.Browser
    :param link: site link
    :param time_to_login: time in seconds for writing credentials
    :param file_name: dump's file name (path)
    :return: None
    """
    browser.get(link)
    sleep(time_to_login)
    pickle.dump(browser.get_cookies(), open(f'{file_name}', 'wb'))
    print(f'Cookies for site <{link}> has been saved to file <{file_name}>')

def load_cookies_in_brouser (browser, cookies_file_path, link):
    """
    The function for loading cookies session into browser

    :param browser: obj.webdriver.Browser
    :param cookies_file_path: dump's file name (path)
    :param link: site link
    :return: None
    """
    browser.get(link)

    try:
        for cookie in pickle.load(open(cookies_file_path, 'rb')):browser.add_cookie(cookie)
        print(f'Cookies has been loaded from <{cookies_file_path} to site session <{link}>')
        browser.refresh()
    except EOFError as ex:
        print(f"File <{cookies_file_path}> is bad or isn't a cookie file")

if __name__ == '__main__':
    browser = webdriver.Chrome()
    link = 'https://rutracker.net/forum/index.php'
    # get_cookies_dump(browser=browser,link=link,time_to_login=30,file_name='seccion_tracker')
    load_cookies_in_brouser(browser,'seccion_tracker',link)