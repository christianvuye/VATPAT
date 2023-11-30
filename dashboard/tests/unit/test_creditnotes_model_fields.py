from django.apps import apps
from dashboard.models import Dealers   

def test_creditnotes_model_fields():
    try:
        CreditNotes = apps.get_model('dashboard', 'creditnotes')
    except LookupError:
        assert False, "The 'creditnotes' model does not exist."
    
    # Test CN_ID field
    cn_id_field = CreditNotes._meta.get_field('CN_ID')
    assert cn_id_field.max_length == 20, "CN_ID field max_length does not match"
    assert cn_id_field.unique == True, "CN_ID field is not unique"
    assert cn_id_field.get_internal_type() == 'CharField', "CN_ID field type is not CharField"

    # Test D_ID field
    d_id_field = CreditNotes._meta.get_field('D_ID')
    assert d_id_field.get_internal_type() == 'ForeignKey', "D_ID field type is not ForeignKey"
    assert d_id_field.related_model == Dealers, "D_ID field does not relate to Dealers model"

    # Test TotalDocumentAmount field
    total_document_amount_field = CreditNotes._meta.get_field('TotalDocumentAmount')
    assert total_document_amount_field.get_internal_type() == 'DecimalField', "TotalDocumentAmount field type is not DecimalField"
    assert total_document_amount_field.max_digits == 38, "TotalDocumentAmount field max_digits does not match"
    assert total_document_amount_field.decimal_places == 20, "TotalDocumentAmount field decimal_places does not match"

    # Test TotalVATAmountDocumentt field
    total_vat_amount_document_field = CreditNotes._meta.get_field('TotalVATAmountDocumentt')
    assert total_vat_amount_document_field.get_internal_type() == 'DecimalField', "TotalVATAmountDocumentt field type is not DecimalField"
    assert total_vat_amount_document_field.max_digits == 38, "TotalVATAmountDocumentt field max_digits does not match"
    assert total_vat_amount_document_field.decimal_places == 20, "TotalVATAmountDocumentt field decimal_places does not match"

    # Test TotalDocumentAmountWithVAT field
    total_document_amount_with_vat_field = CreditNotes._meta.get_field('TotalDocumentAmountWithVAT')
    assert total_document_amount_with_vat_field.get_internal_type() == 'DecimalField', "TotalDocumentAmountWithVAT field type is not DecimalField"
    assert total_document_amount_with_vat_field.max_digits == 38, "TotalDocumentAmountWithVAT field max_digits does not match"
    assert total_document_amount_with_vat_field.decimal_places == 20, "TotalDocumentAmountWithVAT field decimal_places does not match"

    # Test AccountingNumberID field
    accounting_number_id_field = CreditNotes._meta.get_field('AccountingNumberID')
    assert accounting_number_id_field.max_length == 30, "AccountingNumberID field max_length does not match"
    assert accounting_number_id_field.get_internal_type() == 'CharField', "AccountingNumberID field type is not CharField"

    # Test IssuedDate field
    issued_date_field = CreditNotes._meta.get_field('IssuedDate')
    assert issued_date_field.get_internal_type() == 'DateTimeField', "IssuedDate field type is not DateTimeField"
