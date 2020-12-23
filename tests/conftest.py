import json
import pytest
import selenium.webdriver

@pytest.fixture
def config(scope='session'):
  # Read the file
  with open('config.json') as config_file:
    config = json.load(config_file)
  
  # Assert values are acceptable
  assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
  assert isinstance(config['implicit_wait'], int)
  assert config['implicit_wait'] > 0

  # Return config so it can be used
  return config

@pytest.fixture
def browser(config):   
    # #initialize the ChromeDriver instance
    # driver = selenium.webdriver.Chrome()

    # #Make its calss wait up to 10 seconds for elements to appear
    # driver.implicitly_wait(10)

    # #Return the Webdriver instance for the setup
    # yield driver

    # #Quit the WebDriver instance for the cleanup
    # driver.quit()

    #Initialize the Webdriver instance
    if config['browser'] == 'Firefox':
        driver = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        driver = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        driver = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    #Make its calls wait for element to appear
    driver.implicitly_wait(config['implicit_wait'])

    #Return the WebDriver instance for the setup
    yield driver

    #Quit the WebDriver instace for the cleanup
    driver.quit()