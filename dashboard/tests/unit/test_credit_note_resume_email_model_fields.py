from django.apps import apps

def test_credit_note_resume_email_model_fields():
    try:
        CreditNoteResumeEmail = apps.get_model('dashboard', 'CreditNoteResumeEmail')
    except LookupError:
        assert False, "The 'CreditNoteResumeEmail' model does not exist."

    # Test CNR_ID field
    cnr_id_field = CreditNoteResumeEmail._meta.get_field('CNR_ID')
    assert cnr_id_field.get_internal_type() == 'AutoField', "CNR_ID field type is not AutoField"
    assert cnr_id_field.unique == True, "CNR_ID field is not unique"
    assert cnr_id_field.primary_key == True, "CNR_ID field is not a primary key"

    # Test CN_ID field
    cn_id_field = CreditNoteResumeEmail._meta.get_field('CN_ID')
    assert cn_id_field.max_length == 10, "CN_ID field max_length does not match"
    assert cn_id_field.get_internal_type() == 'CharField', "CN_ID field type is not CharField"

    # Test DateIssued field
    date_issued_field = CreditNoteResumeEmail._meta.get_field('DateIssued')
    assert date_issued_field.get_internal_type() == 'DateTimeField', "DateIssued field type is not DateTimeField"

    # Test Month field
    month_field = CreditNoteResumeEmail._meta.get_field('Month')
    assert month_field.get_internal_type() == 'IntegerField', "Month field type is not IntegerField"

    # Test Year field
    year_field = CreditNoteResumeEmail._meta.get_field('Year')
    assert year_field.get_internal_type() == 'IntegerField', "Year field type is not IntegerField"

    # Test Body field
    body_field = CreditNoteResumeEmail._meta.get_field('Body')
    assert body_field.get_internal_type() == 'TextField', "Body field type is not TextField"

    # Test Subject field
    subject_field = CreditNoteResumeEmail._meta.get_field('Subject')
    assert subject_field.max_length == 40, "Subject field max_length does not match"
    assert subject_field.get_internal_type() == 'CharField', "Subject field type is not CharField"

    # Test Status field
    status_field = CreditNoteResumeEmail._meta.get_field('Status')
    assert status_field.get_internal_type() == 'BooleanField', "Status field type is not BooleanField"

    # Test IsValid field
    is_valid_field = CreditNoteResumeEmail._meta.get_field('IsValid')
    assert is_valid_field.get_internal_type() == 'BooleanField', "IsValid field type is not BooleanField"
