#!/usr/bin/env python3
from unittest import TestCase
from unittest.mock import patch, Mock, PropertyMock, MagicMock
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
                'org',
                new_callable=PropertyMock) as mck:
            org_client = GithubOrgClient('google')
            mck.return_value = {'repos_url': "test_url"}
            self.assertEqual(
                    org_client._public_repos_url, 'test_url')

    @patch('client.get_json')
    def test_public_repos(self, mock_getjson):
        """make it return a payload of your choice."""

        val = {
            'login': 'google',
            'repos_url': 'https://api.github.com/orgs/google/repos'
        }
        mock_getjson.return_value = MagicMock(return_value=val)
        with patch(
                'client.GithubOrgClient._public_repos_url',
                new_callable=PropertyMock) as repos_mck:
            org_client = GithubOrgClient('google')
            repos_mck.return_value = org_client.org()['repos_url']
            self.assertEqual(
                    org_client._public_repos_url,
                    'https://api.github.com/orgs/google/repos'
                )
            mock_getjson.assert_called_once_with(
                     'https://api.github.com/orgs/google'
                     )
            repos_mck.assert_called_once()
