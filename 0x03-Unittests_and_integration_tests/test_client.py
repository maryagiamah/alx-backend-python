#!/usr/bin/env python3
from unittest import TestCase
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(TestCase):
    """Implement the test_org method"""

    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json')  # Patch the get_json function
    def test_org(self, org_name, mock_json):
        """Test that GithubOrgClient.org returns the correct value"""

        # Define what the mock should return, mimicking the API response
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
