from  fixture.application import WinApp
import pytest
fixture = None

@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = WinApp("D:\\project\\kus8\\addressbook\\AddressBook.exe")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    global fixture
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

