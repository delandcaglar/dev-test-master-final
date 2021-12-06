from .test_setup import TestSetup, TestHandle
import pdb
from sellers.models import Seller,OldHandles
import json
class TestSellerByIdView(TestSetup):

    def test_elma_name(self):
        Seller.objects.create(name='elma', handle='test-seller')


    def test_get_a_seller_by_id_with_known_id(self):
        Seller.objects.create(name='test seller name', handle='test-seller')
        res = self.client.get(self.seller_url,self.user_data1,format='json')
        # pdb.set_trace()
        self.assertEqual(res.status_code,200)
        self.assertEqual(json.loads(res.content), {
            'id': 1,
            'name': 'test seller name',
            'handle': 'test-seller'
        })


    def test_get_a_seller_by_if_with_known_id(self):

        res = self.client.get(self.seller_url_out_of_range)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(json.loads(res.content), {
            'error': 'seller not found'
        })

    def test_update_seller_handle(self):
        Seller.objects.create(name='test seller name',handle='test_seller')
        res = self.client.put(self.seller_url_put_id,self.put_user_data,seller_id=1)
        print(res.data)
        print(res.status_code)
        print(res.content)
        self.assertEqual(res.status_code, 202)
        self.assertEqual(json.loads(res.content), {"cannot_be_done":"cannot_be_done"}) # missing name

class TestHandle(TestHandle):

    def test_create_handle_post_with_no_data(self):
        res = self.client.post(self.handle_url)
        # pdb.set_trace()
        self.assertEqual(res.status_code,400)

    def test_get_a_seller_by_handle_with_known_handle(self):
        Seller.objects.create(name="test seller name", handle="test-seller")
        OldHandles.objects.create(seller_id = '1',name="test seller name", old_handle="test-seller")
        res = self.client.get(self.handle_url_with_handle)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(json.loads(res.content), {
            'id': 1,
            'name': 'test seller name',
            'handle': 'test-seller'
        })

    def test_get_a_seller_by_handle_with_unknown_handle(self):
        res = self.client.get(self.handle_url_with_unknown_handle)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(json.loads(res.content), {
            'error': 'seller not found'
        })

