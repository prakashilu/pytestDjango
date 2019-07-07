from django.urls import reverse, resolve


class TestUrls:

    def test_details_url(self):
        urls = reverse('detail', kwargs={'pk': 1})
        assert resolve(urls).view_name == 'detail'
