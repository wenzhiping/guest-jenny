import requests
import unittest

#查询发布会接口
url = "http://127.0.0.1:8000/api/get_event_list/"
r = requests.get(url,params={'eid':'1'})
result = r.json()
print(result)
assert result['status'] == 200
assert result['message'] == "success"
assert result['data']['name'] == "小米5发布会"
assert result['data']['address'] == "高新区"
assert result['data']['start_time'] == "2019-06-04T13:04:57"

class GetEventListTest(unittest.TestCase):
    '''查询发布会接口测试'''
    def setUp(self):
        self.url = "http://127.0.0.1:8000/api/get_event_list/"
    def test_get_event_null(self):
        '''发布会id为空'''
        r = requests.get(self.url,params={'eid':''})
        result = r.json()
        print(result)
        self.assertEqual(result['status'],10021)
        self.assertEqual(result['message'],"parameter error")
    def test_get_event_success(self):
        '''发布会ID=1，查询成功'''
        r = requests.get(self.url,params={'eid':'1'})
        result = r.json()
        print(result)
        self.assertEqual(result['status'],200)
        self.assertEqual(result['message'], "success")
        self.assertEqual(result['data']['name'], "小米5发布会")
        self.assertEqual(result['data']['address'], "高新区1")
        self.assertEqual(result['data']['start_time'], "2019-06-04T13:04:57")
    if __name__ == '__main__':
        unittest.main()