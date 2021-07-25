from django.test import TestCase

# Create your tests here.

from django.contrib.auth.models import User
from storage.models import LinkStorage, Topic

class Test_create_bookmark(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_category = Category.objects.create(name='django')
        testuser1 = user.objects.create_user(username='testuser1', password='7898788')
        test_bmark = LinkStorage.objects.create(topic_id=1, author_id=1, name='Testii', link='django.com', visited=False)

        def test_lineaar_doc(self):
            pass