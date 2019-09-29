
from App.Controllers import TopController as c
from Api import api as a
url = {
    "/":c.TopController.Index(),
    "/api/first":a.Api.first()
    }