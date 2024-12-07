import unittest

import py3_requests


class MyTestCase(unittest.TestCase):
    def test_requests(self):
        response=py3_requests.request(
            response_handler=lambda r: r.status_code,
            method='GET',
            url='https://www.baidu.com',
        )
        print(response)
        self.assertTrue(True, "ok")  # add assertion here


if __name__ == '__main__':
    unittest.main()
