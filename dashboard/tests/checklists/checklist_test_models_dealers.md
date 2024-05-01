# Dealers Model Testing Checklist

## Test Field Validations
- [X] Test that creating a dealer with a duplicate D_ID raises an error.
- [X] Test for maximum length constraints on string fields.
- [X] Test for required fields being not nullable.
- [X] Test for unique constraints on fields that should be unique.
- [X] Create shared fixture for dealers model that each test can refer to.
- [X] Rewrite and retest all tests with shared fixture 

## Test Field Data Types
- [X] Ensure CharFields accept and store strings.
- [X] Ensure DateTimeFields accept and store datetime objects.

## Test Default Values and Behaviors
- [X] Test default timestamps are set correctly on new instances.
- [X] Test any other default values are assigned as expected.

## Test Custom Methods in Dealers Model
- [X] Test each custom method behaves as expected.

## Test Business Logic
- [X] Test DealerVATnumber format rules are enforced. 
- [X] Test DealerEmail format rules are enforced -> test if DealerEmail is emailfield and if raises an integrity error? 
- [X]  we should be able to add D_ID (its not a auto incremented code, has format too, Starts with PT + 6 digits, must be validated, currently importng from Navision DB, 

## Test Model's QuerySet Methods -> not needed for now, maybe later -> test them when you have business logic to test
- [ ] Test custom QuerySet methods return expected results.
- [ ] Test custom manager methods behave correctly.

## Test Deletion Restrictions
- [x] Test that deletion of a Dealers instance raises IntegrityError when not allowed.

## Test Relationships with Other Models -> do these tests after you have created and tested other models on their own
- [ ] Test cascading deletes (if applicable). -> Test this after credit notes model and other models are completed
- [X] Test related models' behavior when a Dealers instance is modified. -> Test that if Dealer data is changed, nothing changes in the credit notes model? 
- [ ] Ensure that the number of related objects does not change after a Dealer instance is updated. -> Test this after the Credit Notes model has been tested on its own 
- [ ] Test Deletion Attempt Does Not Affect Related Models: Since Dealers cannot be deleted, ensure this behavior doesn't lead to accidental removal or modification of related records.
- [ ] Test Consistency After Rollbacks: In cases where transactions are involved, ensure that if a transaction fails and is rolled back, the related models are unaffected.

## Test Model's String Representation
- [X] Test the `__str__` method returns the expected string.

## Test Data Integrity
- [X] Test that updating a Dealers instance maintains data integrity.
- [X] Test unrelated fields or records are not changed inadvertently.

## Test Edge Cases -> Do this later, at the end of development
    # Potential Edge Cases for the Dealers Model

    ## Field Limit Testing

    - **Maximum Length:** Ensure that string fields like `DealerName`, `DealerVATnumber`, and `DealerEmail` handle inputs at their maximum length without issues.
    - **Exceeding Maximum Length:** Test inputs that exceed the maximum allowed lengths to ensure that they are handled properly (likely by raising a `ValidationError`).

    ## Special Characters in Inputs

    - Include special characters, such as new lines, emojis, or non-standard Unicode characters in fields like `DealerName` and `DealerEmail` to test how your application handles them.

    ## Boundary Values for Numbers and Dates

    - If there are numerical fields or dates that have specific range requirements (not explicitly in your current model but potentially in other parts of your application), testing the boundaries of these ranges is important.

    ## Email Field Validation

    - Test the `DealerEmail` field with invalid email formats to ensure that your validation logic catches common mistakes.

    ## Concurrency

    - Test how the system behaves if multiple updates to the same Dealer record occur at the same time. This helps ensure that your application handles race conditions appropriately.

    ## Database Integrity

    - Attempt to create or update Dealers with duplicate `D_ID` values or other unique constraints to ensure that the database integrity constraints are enforced.

    ## Handling Null and Optional Fields

    - If any fields are optional, test submissions with these fields left blank.
    - Try to update fields to `None` where it shouldn't be allowed, and ensure that this raises appropriate errors.

## Regression Testing -> test when adding new features (run pytest on the whole repo) 