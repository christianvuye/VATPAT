from django.contrib import admin
from .models import (
    Dealers, 
    CreditNoteResume, 
    CreditNotes, 
    AcknowledgementRequest, 
    AcknowledgementReceived
)

# Register your models here.
admin.site.register(Dealers)
admin.site.register(CreditNoteResume)
admin.site.register(CreditNotes)
admin.site.register(AcknowledgementRequest)
admin.site.register(AcknowledgementReceived)