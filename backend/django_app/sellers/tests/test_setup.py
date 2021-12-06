from django.urls import reverse
from test.support import EnvironmentVarGuard
from rest_framework.test import APITestCase
class TestSetup(APITestCase):

    def setUp(self):
        self.handle_url = reverse('handle_post')

        self.user_data = {
            'old_handle': 'deland1',
            'seller': '1',
            'name': 'deland'
        }

        self.seller_url = reverse('seller_id', kwargs={'seller_id': 1})

        self.user_data1 = {
            'id': 1,
            'name': 'test seller name',
            'handle': 'test-seller'
        }

        self.seller_url_out_of_range = reverse("seller_id", kwargs={'seller_id': 99})

        self.seller_url_put_id = reverse("seller_id", kwargs={'seller_id': 1})

        self.put_user_data = {
            # 'name' : 'test seller name',
            'handle': 'new-handle'
        }


        return super().setUp()

    def tearDown(self):
        return super().tearDown()

class TestHandle(APITestCase):
    def setUp(self):
        self.handle_url = reverse('handle_post')

        self.handle_url_with_handle = reverse('handle_get', kwargs={'seller_handle': 'test-seller'})

        self.handle_url_with_unknown_handle = reverse('handle_get', kwargs={'seller_handle': 'test-unknown'})

        self.handle_data = {
            'id': 1,
            'name': 'test seller name',
            'handle': 'test-seller'
        }

    def tearDown(self):
        return super().tearDown()