import unittest
from unittest.mock import patch, MagicMock
import requests
from main import check_url_exists, get_depends, create_graph, main
import os


class TestDependencyGraph(unittest.TestCase):
    @patch("main.requests.head")
    def test_check_url_exists_valid_url(self, mock_head):
        mock_head.return_value.status_code = 200
        result = check_url_exists("https://pkgs.alpinelinux.org")
        self.assertTrue(result)

    @patch("main.requests.head")
    def test_check_url_exists_invalid_url(self, mock_head):
        mock_head.return_value.status_code = 404
        result = check_url_exists("https://pkgs.alpinelinux.org")
        self.assertFalse(result)

    @patch("main.requests.get")
    def test_get_depends_no_depends(self, mock_get):
        # Зависимостей нет
        mock_response = MagicMock()
        mock_response.text = "<html><body>No dependencies</body></html>"
        mock_get.return_value = mock_response
        result = get_depends("https://pkgs.alpinelinux.org/package/edge/main/x86_64/dnscontrol-doc")
        self.assertEqual(result, -1)

    @patch("main.requests.get")
    def test_get_depends_invalid_url(self, mock_get):
        # Ошибка URL
        mock_get.side_effect = requests.RequestException
        result = get_depends("https://pkgs.alpinelinux")
        self.assertEqual(result, -2)

    def test_create_graph(self):
        # Проверка создания графа
        package_str = "intel-media-driver"
        depends_lst = ['so_libc_musl_x86_64.so.1', 'so_libgcc_s.so.1']
        output_dir = "./graphs"

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        result_path = create_graph(package_str, depends_lst, "", output_dir)
        self.assertTrue(os.path.exists(result_path))
        os.remove(result_path)


if __name__ == '__main__':
    unittest.main()