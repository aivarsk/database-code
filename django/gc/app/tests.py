import gc
from django.test import TestCase
from app.models import Country, Currency, Account, Payment
import time


class PersonTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        eur = Currency.objects.create(symbol='EUR')
        lv = Country.objects.create(symbol='LV')
        account = Account.objects.create(country=lv, balance=0, currency=eur)
        for _ in range(100000):
            Payment.objects.create(amount=1, account=account)
        gc.set_debug(gc.DEBUG_STATS)

    def test_qs(self):
        start = time.time()
        for p in Payment.objects.all().select_related('account__country', 'account__currency'):
            pass
        print(time.time() - start)

    def test_iterator(self):
        start = time.time()
        for p in Payment.objects.all().select_related('account__country', 'account__currency').iterator():
            pass
        print(time.time() - start)

    def test_qs_no_gc(self):
        start = time.time()
        gc.disable()
        for p in Payment.objects.all().select_related('account__country', 'account__currency').iterator():
            pass
        gc.enable()
        print(time.time() - start)
