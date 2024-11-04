#!/usr/bin/env python3
from unittest import TestCase
from unittest.mock import patch, Mock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    """Implement the test_org method"""

    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_json):
        """Test that GithubOrgClient.org returns the correct value"""

        val = {
            'login': org_name,
            'repos_url': f'https://api.github.com/orgs/{org_name}/repos'
        }

        mock_json.return_value = Mock(return_value=val)

        org_client = GithubOrgClient(org_name)

        self.assertEqual(org_client.org(), val)

        mock_json.assert_called_once_with(
            org_client.ORG_URL.format(org=org_name)
        )

    def test_public_repos_url(self):
        """make it return a known payload"""

        with patch.object(
                GithubOrgClient,
                '_public_repos_url',
                new_callable=PropertyMock) as mck:
            org_client = GithubOrgClient('google')
            mck.return_value = {"License": None, "name": "test_url"}
            self.assertEqual(
                    org_client._public_repos_url,
                    {"License": None, "name": "test_url"}
                )
