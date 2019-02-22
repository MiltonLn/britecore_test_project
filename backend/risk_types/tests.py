from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import RiskType


class RiskTypeAPITests(APITestCase):
    def test_successfully_create_risk_type(self):
        """Test we can successfully create a new RiskType"""
        url = reverse('risktype-list')
        data = {
            'name': 'RiskType1',
            'fields_type': {
                'string_field': 'STRING',
                'number_field': 'NUMBER',
                'date_field': 'DATE',
                'choice_field': ['option1', 'option2', 'option3']
            }
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(RiskType.objects.count(), 1)
        self.assertEqual(RiskType.objects.get().name, 'RiskType1')
        self.assertEqual(
            RiskType.objects.get().fields_type,
            {
                'string_field': 'STRING',
                'number_field': 'NUMBER',
                'date_field': 'DATE',
                'choice_field': ['option1', 'option2', 'option3']
            }
        )

    def test_create_risk_type_with_wrong_fields_type_format(self):
        """Test we can't create a RiskType with an unsupported field type"""
        url = reverse('risktype-list')
        data = {
            'name': 'RiskType1',
            'fields_type': {
                'string_field': 'STRING',
                'unsupported_thing': 4

            }
        }
        error_msg = 'Unsupported type "4" for field "unsupported_thing"'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(RiskType.objects.count(), 0)
        self.assertEqual(error_msg, response.data['fields_type'][0])

    def test_create_risk_type_with_wrong_enum_type(self):
        """Test we can't create a RiskType with a enum type field with a wrong
        format"""
        url = reverse('risktype-list')
        data = {
            'name': 'RiskType1',
            'fields_type': {
                'string_field': 'STRING',
                'number_field': 'NUMBER',
                'date_field': 'DATE',
                'wrong_choice_field': ['option1', 400, []]
            }
        }
        error_msg = '"wrong_choice_field" is not a strings list'
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(RiskType.objects.count(), 0)
        self.assertEqual(error_msg, response.data['fields_type'][0])

    def test_update_risk_type(self):
        """Test we can update RiskTypes"""
        risk_type = RiskType.objects.create(
            name='RiskType1',
            fields_type={
                'field1': 'STRING'
            }
        )
        data = {
            'name': 'New Name',
            'fields_type': {
                'field1': 'NUMBER'
            }
        }
        url = reverse('risktype-detail', kwargs={'pk': risk_type.id})
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        risk_type.refresh_from_db()
        self.assertEqual(risk_type.name, data['name'])
        self.assertEqual(risk_type.fields_type, data['fields_type'])

    def test_read_risk_type(self):
        """Test we can correctly read a RiskType from the API"""
        risk_type = RiskType.objects.create(
            name='RiskType1',
            fields_type={
                'field1': 'STRING'
            }
        )
        url = reverse('risktype-detail', kwargs={'pk': risk_type.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data,
            {
                'id': str(risk_type.id),
                'name': risk_type.name,
                'fields_type': risk_type.fields_type
            }
        )

    def test_read_risk_type_not_found(self):
        """Test the API gives the correct response when a RiskType isn't found"""
        url = reverse('risktype-detail', kwargs={'pk': "anything"})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_list_risk_types(self):
        """Test getting all RiskTypes work properly"""
        risk_type1 = RiskType.objects.create(
            name='RiskType1',
            fields_type={
                'field1': 'STRING'
            }
        )
        risk_type2 = RiskType.objects.create(
            name='RiskType2',
            fields_type={
                'field1': 'NUMBER'
            }
        )
        url = reverse('risktype-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['name'], risk_type1.name)
        self.assertEqual(response.data[1]['name'], risk_type2.name)
