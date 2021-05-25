import pytest
import os.path
from fixture.application import Application
import json
import jsonpickle

fixture = None
target = None

@pytest.fixture
def app(request, config):
    global fixture
    browser = request.config.getoption("--browser")
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=config['web']['baseUrl'])
    fixture.session.ensure_login(username=config['webadmin']['username'], password=config['webadmin']['password'])
    return fixture

@pytest.fixture(scope = 'session', autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

#описание опций
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")


#функция для загрузки конфигурации
def load_config(file):
    global target
    if target is None:
        #определяем путь относительно директории проекта
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


def load_from_json(file):
    # os.path.abspath(__file__) - 'это путь к текущему файлу конфтест
    # dirname получаем директорию, в которой он находится - это корневая дир проекта
    # join подклеиваем путь к json файлу
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        # перекодируем обратно в в формат объектов питон
        return jsonpickle.decode(f.read())

@pytest.fixture(scope="session")
def config(request):
    return load_config(request.config.getoption("--target"))

