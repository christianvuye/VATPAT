from django.apps import apps

def test_dealers_model_fields():
    try:
        Dealers = apps.get_model('dashboard', 'Dealers')
    except LookupError:
        assert False, "The 'dealers' model does not exist."
    
    # Test D_ID field
    d_id_field = Dealers._meta.get_field('D_ID')
    assert d_id_field.max_length == 10, "D_ID field max_length does not match"
    assert d_id_field.unique == True, "D_ID field is not unique"
    assert d_id_field.get_internal_type() == 'CharField', "D_ID field type is not CharField"

    # Test DealerName field
    dealer_name_field = Dealers._meta.get_field('DealerName')
    assert dealer_name_field.max_length == 100, "DealerName field max_length does not match"
    assert dealer_name_field.get_internal_type() == 'CharField', "DealerName field type is not CharField"

    # Test DealerVATnumber field
    dealer_vat_number_field = Dealers._meta.get_field('DealerVATnumber')
    assert dealer_vat_number_field.max_length == 20, "DealerVATnumber field max_length does not match"
    assert dealer_vat_number_field.get_internal_type() == 'CharField', "DealerVATnumber field type is not CharField"

    # Test DealerEmail field
    dealer_email_field = Dealers._meta.get_field('DealerEmail')
    assert dealer_email_field.max_length == 80, "DealerEmail field max_length does not match"
    assert dealer_email_field.get_internal_type() == 'CharField', "DealerEmail field type is not CharField"

    # Test CreatedDate field
    created_date_field = Dealers._meta.get_field('CreatedDate')
    assert created_date_field.get_internal_type() == 'DateTimeField', "CreatedDate field type is not DateTimeField"

    # Test ModifiedDate field
    modified_date_field = Dealers._meta.get_field('ModifiedDate')
    assert modified_date_field.get_internal_type() == 'DateTimeField', "ModifiedDate field type is not DateTimeField"
