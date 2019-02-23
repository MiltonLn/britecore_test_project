from django.utils import timezone

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from risk_types.models import RiskType
from .models import Risk


class RiskAPITests(APITestCase):
    def setUp(self):
        super().setUp()
        self.risk_type = RiskType.objects.create(
            name='RiskType1',
            fields_type={
                'string_field': 'STRING',
                'number_field': 'NUMBER',
                'date_field': 'DATE',
                'choice_field': ['option1', 'option2', 'option3']
            }
        )

    def test_successfully_create_risk(self):
        """Test we can successfully create a new Risk"""
        url = reverse('risk-list')
        data = {
            'risk_type': str(self.risk_type.id),
            'field_values': {
                'string_field': 'Some string',
                'number_field': 144,
                'date_field': str(timezone.now()),
                'choice_field': 'option1'
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Risk.objects.count(), 1)
        new_risk = Risk.objects.get()
        self.assertDictEqual(new_risk.field_values, data['field_values'])

    def test_create_risk_with_invalid_atomic_type(self):
        """Test we can't create a Risk with an invalid type for a field"""
        url = reverse('risk-list')
        data = {
            'risk_type': str(self.risk_type.id),
            'field_values': {
                'string_field': 24,  # This is not valid since it should be a string
                'number_field': 144,
                'date_field': timezone.now(),
                'choice_field': 'option1'
            }
        }
        error_msg = '"24" is not a valid "STRING"'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Risk.objects.count(), 0)
        self.assertIn(error_msg, response.data['non_field_errors'])

    def test_create_risk_with_wrong_option(self):
        """Test we can't create a Risk with a enum type field with a wrong
        option"""
        url = reverse('risk-list')
        data = {
            'risk_type': str(self.risk_type.id),
            'field_values': {
                'string_field': 24,
                'number_field': 144,
                'date_field': timezone.now(),
                'choice_field': 'Wrong option'  # This is not a valid option
            }
        }
        error_msg = '"Wrong option" is not a valid option for choice_field'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Risk.objects.count(), 0)
        self.assertIn(error_msg, response.data['non_field_errors'][0])

    def test_update_risk(self):
        """Test we can update Risks"""
        risk = Risk.objects.create(
            risk_type=self.risk_type,
            field_values={
                'string_field': 'Some string',
                'number_field': 144,
                'date_field': str(timezone.now()),
                'choice_field': 'option1'
            }
        )
        data = {
            'risk_type': str(self.risk_type.id),
            'field_values': {
                'string_field': 'Another string',
                'number_field': 25,
                'date_field': str(timezone.now()),
                'choice_field': 'option2'
            }
        }
        url = reverse('risk-detail', kwargs={'pk': risk.id})
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        risk.refresh_from_db()
        self.assertDictEqual(risk.field_values, data['field_values'])

    def test_read_risk(self):
        """Test we can correctly read a Risk from the API"""
        risk = Risk.objects.create(
            risk_type=self.risk_type,
            field_values={
                'string_field': 'Some string',
                'number_field': 144,
                'date_field': str(timezone.now()),
                'choice_field': 'option1'
            }
        )
        url = reverse('risk-detail', kwargs={'pk': risk.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.data['field_values'], risk.field_values)

    def test_read_risk_type_not_found(self):
        """Test the API gives the correct response when a Risk isn't found"""
        url = reverse('risk-detail', kwargs={'pk': "anything"})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_list_risks_types(self):
        """Test getting all Risks work properly"""
        risk1 = Risk.objects.create(
            risk_type=self.risk_type,
            field_values={
                'string_field': 'Some string',
                'number_field': 144,
                'date_field': str(timezone.now()),
                'choice_field': 'option1'
            }
        )
        risk2 = Risk.objects.create(
            risk_type=self.risk_type,
            field_values={
                'string_field': 'Another string',
                'number_field': 5,
                'date_field': str(timezone.now()),
                'choice_field': 'option3'
            }
        )
        url = reverse('risk-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(
            response.data[0]['field_values'],
            risk1.field_values
        )
        self.assertDictEqual(
            response.data[1]['field_values'],
            risk2.field_values
        )
