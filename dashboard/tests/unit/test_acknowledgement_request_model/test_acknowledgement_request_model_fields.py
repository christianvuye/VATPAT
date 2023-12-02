from django.apps import apps

def test_acknowledgement_request_model_fields():
    try:
        AcknowledgementRequest = apps.get_model('dashboard', 'AcknowledgementRequest')
    except LookupError:
        assert False, "The 'AcknowledgementRequest' model does not exist."

    # Test R_ID field
    r_id_field = AcknowledgementRequest._meta.get_field('R_ID')
    assert r_id_field.get_internal_type() == 'AutoField', "R_ID field type is not AutoField"
    assert r_id_field.unique == True, "R_ID field is not unique"
    assert r_id_field.primary_key == True, "R_ID field is not a primary key"

    # Test CNR_ID field
    cnr_id_field = AcknowledgementRequest._meta.get_field('CNR_ID')
    assert cnr_id_field.get_internal_type() == 'IntegerField', "CNR_ID field type is not IntegerField"
    assert cnr_id_field.null == True, "CNR_ID field does not allow null values" 

    # Test Status field
    status_field = AcknowledgementRequest._meta.get_field('Status')
    assert status_field.get_internal_type() == 'BooleanField', "Status field type is not BooleanField"

    # Test CreatedDate field
    created_date_field = AcknowledgementRequest._meta.get_field('CreatedDate')
    assert created_date_field.get_internal_type() == 'DateTimeField', "CreatedDate field type is not DateTimeField"

    # Test SendDate field
    send_date_field = AcknowledgementRequest._meta.get_field('SendDate')
    assert send_date_field.get_internal_type() == 'DateTimeField', "SendDate field type is not DateTimeField"
