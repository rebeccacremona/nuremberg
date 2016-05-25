from nuremberg.tests.acceptance_helpers import *

def test_404():
    response = client.get("THIS_URL_DOES_NOT_EXIST")
    page = PyQuery(response.content)

    page('h1').text().should.contain("can't find")