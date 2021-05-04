from django.test import TestCase
from .models import Company
# Create your tests here.

class CompanyTestClass(TestCase):
    def setUp(self):
        self.company = Company(company_name='safaricom')

    def test_company_instance(self):
        self.assertTrue(isinstance(self.company, Company))

    def test_save_company_method(self):
        self.company.save_company()
        company_object = Company.objects.all()
        self.assertTrue(len(company_object) > 0)

    def test_delete_company_method(self):
        self.company.save_company()
        company_object = Company.objects.all()
        self.company.delete_company()
        company_object = Company.objects.all()
        self.assertTrue(len(company_object) == 0)
