# Credit Notes Model Testing Checklist

## Test Field Validations
- [X] Test that creating a credit note with a duplicate `CN_ID` raises an error.
- [ ] Test for maximum length constraints on string fields (`CN_ID`, `AccountingNumberID`).
- [ ] Test for required fields being not nullable.
- [ ] Test for unique constraints on fields that should be unique (`CN_ID`).
- [ ] Create shared fixture for credit notes model that each test can refer to.
- [ ] Rewrite and retest all tests with shared fixture.

## Test Field Data Types
- [ ] Ensure `CharFields` accept and store strings.
- [ ] Ensure `DateTimeFields` accept and store datetime objects.
- [ ] Ensure `DecimalFields` accept and store decimal values correctly.

## Test Default Values and Behaviors
- [ ] Test that fields without default values (like `IssuedDate`) must be provided and do not default silently.
- [ ] Test any other default values are assigned as expected.

## Test Custom Methods in Credit Notes Model
- [ ] Test each custom method behaves as expected, including any methods managing financial calculations or constraints.

## Test Business Logic
- [ ] Test that `TotalVATAmountDocumentt` cannot exceed `TotalDocumentAmount`.
- [ ] Test that `TotalDocumentAmountWithVAT` is calculated correctly based on the other total fields.

## Test Model's QuerySet Methods
- [ ] Test custom QuerySet methods return expected results.
- [ ] Test custom manager methods behave correctly.

## Test Deletion Restrictions
- [ ] Test that deletion of a `CreditNotes` instance does what it's supposed to do based on model configuration (check cascading effects).

## Test Relationships with Other Models
- [ ] Test the relationship between `Dealers` and `CreditNotes` (e.g., cascading deletes, update propagation).
- [ ] Test foreign key constraints are enforced (e.g., cannot create a `CreditNotes` without a valid `Dealers` foreign key).

## Test Model's String Representation
- [ ] Test the `__str__` method returns the expected string format.

## Test Data Integrity
- [ ] Test that updating a `CreditNotes` instance maintains data integrity.
- [ ] Test unrelated fields or records are not changed inadvertently.

## Test Edge Cases
- [ ] Test boundary values for `TotalDocumentAmount`, `TotalVATAmountDocumentt`, and `TotalDocumentAmountWithVAT`.
- [ ] Test inserting extreme values for `DateTimeFields` like `IssuedDate`.
- [ ] Test handling of partial or over-limit data inputs.

## Regression Testing
- [ ] Ensure that adding new features to the model doesn't break existing functionality (run pytest on the entire repository).
