"""
A module to test response codes of various routes
"""
import pytest
from fastapi.testclient import TestClient

from avatarapi.main import app


class TestResponseCodes:
    """
    A simple class for all the tests to live in
    """

    client = TestClient(app)

    def test_root_path(self):
        """
        The root path doesn't exist (yet), thus it should return 404 (not found)
        """

        response = self.client.get("/")
        assert response.status_code == 404

    def test_invalid_request_type(self):
        """
        Only GET requests are not allowed, should return 405 (Method not allowed)
        """

        response = self.client.post("/api/quotes")
        assert response.status_code == 405

    @pytest.mark.parametrize("num", [0, 50])
    def test_invalid_number_of_quotes(self, num):
        """
        The valid range for num is 1 <= num <= 25
        In any other case, return code should be 422 (Unprocessable Entry)
        """

        response = self.client.get(f"/api/quotes?num={num}")
        assert response.status_code == 422

    @pytest.mark.parametrize(
        "route",
        [
            "/api/quotes",
            "/api/quotes/character?name=Katara",
            "/api/quotes/nation?name=Fire",
            "/api/quotes/bending?type=All",
            "/api/quotes/episode?title=Imprisoned",
            "/api/quotes/book?title=Fire",
        ],
    )
    def test_all_valid_requests(self, route):
        """
        A valid request to all of the routes should return 200
        """

        response = self.client.get(route)
        assert response.status_code == 200
