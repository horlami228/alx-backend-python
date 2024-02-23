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

    @unittest.mock.patch('client.get_json')
    def test_public_repos(self, mock_json):
        """
        Test that the list of repos is what you expect from the chosen payload.
        Test that the mocked property and the mocked get_json was called once.
        """
        json_payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_json.return_value = json_payload

        with unittest.mock.patch('client.GithubOrgClient._public_repos_url',
                                 new_callable=unittest.mock.PropertyMock
                                 ) as mock_public:

            mock_public.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            check = [i["name"] for i in json_payload]
            self.assertEqual(result, check)

            mock_public.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """ unit-test for GithubOrgClient.has_license """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
