from django.db import models

class UserDetail(models.Model):
    username = models.CharField(max_length=150, unique=True)
    given_name = models.CharField(max_length=100, blank=True)  # This represents the first name
    family_name = models.CharField(max_length=100, blank=True)  # This represents the last name
    middle_name = models.CharField(max_length=100, blank=True)
    application_type_initial_permission = models.CharField(max_length=5, blank=True)  # "True" or "False"
    application_type_replacement = models.CharField(max_length=5, blank=True)
    application_type_renewal = models.CharField(max_length=5, blank=True)
    alien_registration_number = models.CharField(max_length=100, blank=True)
    uscis_account_number = models.CharField(max_length=100, blank=True)
    date_of_birth = models.CharField(max_length=10, blank=True)  # "YYYY-MM-DD"
    country_of_birth = models.CharField(max_length=100, blank=True)
    city_of_birth = models.CharField(max_length=100, blank=True)
    state_province_of_birth = models.CharField(max_length=100, blank=True)
    immigration_status_at_arrival = models.CharField(max_length=100, blank=True)
    current_immigration_status = models.CharField(max_length=100, blank=True)
    sevis_number = models.CharField(max_length=100, blank=True)
    employer_name_e_verify = models.CharField(max_length=100, blank=True)
    employer_e_verify_id = models.CharField(max_length=100, blank=True)
    eligibility_category = models.CharField(max_length=100, blank=True)
    travel_document_number = models.CharField(max_length=100, blank=True)
    form_i94_number = models.CharField(max_length=100, blank=True)
    place_of_last_arrival = models.CharField(max_length=100, blank=True)
    date_of_last_arrival = models.CharField(max_length=10, blank=True)  # "YYYY-MM-DD"
    country_of_passport = models.CharField(max_length=100, blank=True)
    passport_expiration_date = models.CharField(max_length=10, blank=True)  # "YYYY-MM-DD"
    passport_number = models.CharField(max_length=100, blank=True)
    stem_opt_category = models.CharField(max_length=100, blank=True)
    arrested_or_convicted = models.CharField(max_length=5, blank=True)  # "True" or "False"
    special_filing_instructions = models.CharField(max_length=255, blank=True)
    employment_based_categories = models.CharField(max_length=100, blank=True)
    apt_ste_flr_physical = models.CharField(max_length=100, blank=True)
    city_or_town_physical = models.CharField(max_length=100, blank=True)
    state_physical = models.CharField(max_length=100, blank=True)
    zip_code_physical = models.CharField(max_length=15, blank=True)
    uscis_online_account_number = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=50, blank=True)
    marital_status = models.CharField(max_length=50, blank=True)


class OtherName(models.Model):
    user_detail = models.ForeignKey(UserDetail, related_name='other_names', on_delete=models.CASCADE)
    family_name = models.CharField(max_length=100, blank=True)
    given_name = models.CharField(max_length=100, blank=True)
    middle_name = models.CharField(max_length=100, blank=True)
