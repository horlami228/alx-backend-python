#!/usr/bin/env python3

"""A github org client"""

from client import GithubOrgClient
import unittest
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """
    TestGithubOrgClient class
    """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @unittest.mock.patch('client.get_json')
    def test_org(self, org_name, mock_object):
        """test org method"""
        url = f"https://api.github.com/orgs/{org_name}"
        expected_result = {"name": org_name, "payload": True}

        mock_object.return_value = expected_result

        client = GithubOrgClient(org_name)

        result = client.org

        mock_object.assert_called_once_with(url)

        self.assertEqual(result, expected_result)


class TestGithubOrgClient(unittest.TestCase):
    """
    TestGithubOrgClient class
    """

    def test_public_repos_url(self):
        """test public repos method"""
        with unittest.mock.patch('client.GithubOrgClient.org',
                                 new_callable=unittest.mock.PropertyMock) as mock_object:
            test_payload = {"repos_url": "google"}
            mock_object.return_value = test_payload
            client = GithubOrgClient("test")

            self.assertEqual(client._public_repos_url,
                             test_payload["repos_url"])


if __name__ == "__main__":
    unittest.main()
