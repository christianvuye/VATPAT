# CreditNoteResumeEmail Model Testing Checklist

## Test Field Validations
- [ ] Test that creating a resume email with a duplicate `CNR_ID` raises an error.
- [ ] Test for maximum length constraints on string fields (`Subject`).
- [ ] Test for required fields being not nullable.
- [ ] Test for proper date handling in `DateIssued`.

## Test Field Data Types
- [ ] Ensure `CharFields` accept and store strings.
- [ ] Ensure `DateTimeFields` accept and store datetime objects.
- [ ] Ensure `BooleanFields` correctly store true/false values.

## Test Default Values and Behaviors
- [ ] Test default values for `Status` and `IsValid`.
- [ ] Test automatic assignment of `CNR_ID` as primary key.

## Test Custom Methods
- [ ] Test any custom methods or model behaviors.

## Test Model's QuerySet Methods
- [ ] Test custom QuerySet methods return expected results.

## Test Deletion Restrictions
- [ ] Test behavior upon deletion to ensure data consistency.

## Test Model's String Representation
- [ ] Test the `__str__` method returns the expected string.

## Test Data Integrity
- [ ] Ensure data integrity when fields are updated.

## Test Relationships with Other Models
- [ ] Test relationships and interactions with the `CreditNotes` model.