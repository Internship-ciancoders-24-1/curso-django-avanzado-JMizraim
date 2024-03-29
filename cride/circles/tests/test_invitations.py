from django.test import TestCase

#Models
from cride.circles.models import User, Circle, Membership

# class InvitationsManagerTestCase(TestCase):
#     """Invitations manager test case."""

#     def setUp(self):
#         """Test case setup."""
#         self.user = User.objects.create(
#             first_name='Franklin',
#             last_name='Garcia',
#             email='fm-garcia@outlook.com',
#             username='fmgarcia',
#             password='admin123'
#         )
#         self.circle = Circle.objects.create(
#             name='Computer Science Faculty',
#             slug_name='csfaculty',
#             about="Official UPC's Computer Science Faculty",
#             verified=True
#         )

#     def test_code_generation(self):
#         """Random codes should be generated automatically."""
#         invitation = Invitation.objects.create(
#             issued_by=self.user,
#             circle=self.circle
#         )
#         self.assertIsNotNone(invitation.code)

#     def test_code_usage(self):
#         """If a code is given, there's no need to create a new one."""
#         code = 'TESTCODE01'
#         invitation = Invitation.objects.create(
#             issued_by=self.user,
#             circle=self.circle,
#             code=code
#         )
#         self.assertEqual(invitation.code, code)

#     def test_code_generation_if_duplicated(self):
#         """If given code is not unique, a new one must be generated."""
#         code = Invitation.objects.create(
#             issued_by=self.user,
#             circle=self.circle,
#         ).code

#         # Create another invitation with the past code
#         invitation = Invitation.objects.create(
#             issued_by=self.user,
#             circle=self.circle,
#             code=code
#         )

#         self.assertNotEqual(code, invitation.code)

# Si hacen test de funcionalidades que no estan implementadas. 
# El curso termina antes de que se implementen las funcionalidades
