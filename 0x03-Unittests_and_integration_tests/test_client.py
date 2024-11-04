#!/usr/bin/env python3
import unittest
from unittest.mock import patch, Mock, PropertyMock, MagicMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Implement the test_org method"""

    @parameterized.expand([
        ('google',),
        ('abc',)
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_json: MagicMock) -> None:
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

    def test_public_repos_url(self) -> None:
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
    def test_public_repos(self, mock_getjson: MagicMock) -> None:
        """make it return a payload of your choice."""

        test_payload = {
                'repos_url': "https://api.github.com/users/google/repos",
                'repos': [
                    {
                        "id": 1936771,
                        "node_id": "MDEwOlJlcG9zaXRvcnkxOTM2Nzcx",
                        "name": "truth",
                        "full_name": "google/truth",
                        "private": "false"
                    },
                    {
                        "id": 3248507,
                        "node_id": "MDEwOlJlcG9zaXRvcnkzMjQ4NTA3",
                        "name": "ruby-openid-apps-discovery",
                        "full_name": "google/ruby-openid-apps-discovery",
                        "private": "false"
                    },
                ]
            }
        mock_getjson.return_value = test_payload["repos"]
        with patch(
                'client.GithubOrgClient._public_repos_url',
                new_callable=PropertyMock) as repos_mck:
            repos_mck.return_value = test_payload['repos_url']
            self.assertEqual(
                    GithubOrgClient('google').public_repos(),
                    [
                        'truth',
                        'ruby-openid-apps-discovery',
                    ]
                )
            repos_mck.assert_called_once()
            mock_getjson.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expct_val):
        """Implement TestGithubOrgClient.test_has_licens"""

        client_org = GithubOrgClient('Google')
        self.assertEqual(client_org.has_license(repo, license_key), expct_val)


@parameterized_class([
    {
        "org_payload": TEST_PAYLOAD[0][0],
        "repos_payload": TEST_PAYLOAD[0][1],
        "expected_repos": TEST_PAYLOAD[0][2],
        "apache2_repos": TEST_PAYLOAD[0][3]
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """setUpClass and tearDownClass"""

    @classmethod
    def setUpClass(cls):
        """return example payloads found in the fixtures"""

        test_payload = {
                'https://api.github.com/orgs/google': cls.org_payload,
                'https://api.github.com/orgs/google/repos': cls.repos_payload,
            }

        def side_effect(url):
            """Makes Side Effect"""
            if url in test_payload:
                return Mock({'json.return_value': test_payload[url]})
            return HTTPError

            cls.get_patcher = patch('requests.get', side_effect=side_effect)
            cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """method to stop the patcher"""
        cls.get_patcher.stop()
