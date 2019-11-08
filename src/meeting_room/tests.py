from django.test import TestCase
from rest_framework.test import APIRequestFactory

# https://www.django-rest-framework.org/api-guide/testing/
factory = APIRequestFactory()
request = factory.get('/reservations/')