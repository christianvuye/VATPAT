from django.apps import apps

def test_acknowledgement_received_model_fields():
    try:
        AcknowledgementReceived = apps.get_model('dashboard', 'AcknowledgementReceived')
    except LookupError:
        assert False, "The 'AcknowledgementReceived' model does not exist."

    # Test A_ID field
    a_id_field = AcknowledgementReceived._meta.get_field('A_ID')
    assert a_id_field.get_internal_type() == 'AutoField', "A_ID field type is not AutoField"
    assert a_id_field.unique == True, "A_ID field is not unique"
    assert a_id_field.primary_key == True, "A_ID field is not a primary key"

    # Test R_ID field
    r_id_field = AcknowledgementReceived._meta.get_field('R_ID')
    assert r_id_field.get_internal_type() == 'IntegerField', "R_ID field type is not IntegerField"
    assert r_id_field.null == True, "R_ID field does not allow null values"  

    # Test MsgFile field
    msg_file_field = AcknowledgementReceived._meta.get_field('MsgFile')
    assert msg_file_field.get_internal_type() == 'BinaryField', "MsgFile field type is not BinaryField"
