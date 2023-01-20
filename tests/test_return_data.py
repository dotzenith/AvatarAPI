"""
A module to test the data returned from various requests
"""
import json

import pytest
from fastapi.testclient import TestClient

from avatarapi.main import app
from avatarapi.schemas import ReturnQuotes


class TestReturnData:
    """
    A simple class for all the tests to live in
    """

    client = TestClient(app)

    @pytest.mark.parametrize(
        "route",
        [
            "/api/quotes",
            "/api/quotes/character?name=Katara",
            "/api/quotes/nation?name=Fire",
            "/api/quotes/bending?bending=All",
            "/api/quotes/episode?title=Imprisoned",
            "/api/quotes/book?title=Fire",
        ],
    )
    def test_all_routes_data(self, route):
        """
        A default call to any of the routes should return a list of 10 quote objects
        """

        response = self.client.get(route)
        response = json.loads(response.content)

        assert response["num"] == 10

        # Attempts to load the data in pydantic model
        # Test fails if this doesn't work
        ReturnQuotes(**response)

    @pytest.mark.parametrize(
        "route, num",
        [
            ("/api/quotes?num=", 6),
            ("/api/quotes/character?name=Katara&num=", 7),
            ("/api/quotes/nation?name=Fire&num=", 12),
            ("/api/quotes/bending?bending=All&num=", 24),
            ("/api/quotes/episode?title=Imprisoned&num=", 4),
            ("/api/quotes/book?title=Fire&num=", 10),
        ],
    )
    def test_num_url_param(self, route, num):
        """
        Adding num param to any of the routes should return that many quotes
        """

        response = self.client.get(f"{route}{num}")
        response = json.loads(response.content)

        assert response["num"] == num

    def test_return_less_quotes_if_num_too_large(self):
        """
        For some characters and episodes, the default 10 quotes is too large
        Or, the passed in value of num is too large

        This test tries to run a default query for the character named Koh
        Koh only has 2 quotes, but the default num is 10. the response should return 2 quotes.
        """
        # TODO There has to be a better way to test for this condition, find it

        response = self.client.get("/api/quotes/character/?name=Koh")
        response = json.loads(response.content)

        assert response["num"] == 2
