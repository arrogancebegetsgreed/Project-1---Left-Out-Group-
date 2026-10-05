# Test Report

## Verified checks

**23 checks passed; 6 failed.** Account actions, course loading, entry, and deletion
worked in the checked cases. The complete workflow is blocked by GPA errors,
missing grade editing, and missing deletion-form protection.

|Area|Passed|Failed|Result|
|---|---|---|---|
|Pages and styles|4|0|Home, signup, login, and stylesheet loaded.|
|Account actions|6|0|Signup, login, and signout worked; duplicate IDs, wrong passwords, and mismatched confirmation were rejected.|
|Signed-out access|3|0|Course listing, entry, and signout were denied.|
|Course loading|2|0|Five courses totaling 18 credits were saved without duplicates on reload.|
|Course records|7|1|Entry, deletion, empty-list display, and checked student separation cases passed; a nonempty list failed.|
|GPA calculation|1|3|Empty input returned 0; weighted grades, A+, and unknown-grade input failed.|
|Grade editing|0|1|No editing page was available.|
|Deletion-form protection|0|1|A request without a form token still deleted a record.|

## Repository-reported manual results

The upstream [README at `5231a25`](https://github.com/arrogancebegetsgreed/Project-1---Left-Out-Group-/blob/5231a25/README.md)
records six manual passes. The original entries remain in the repository README;
they do not identify the source revision, environment, or test inputs.

The reported GPA pass conflicts with the checks here. The reviewed application
source is unchanged from `71737c8`, and a targeted recheck still raises
`AttributeError` on a nonempty course list. Both results are retained with their
source identified; GPA acceptance needs a reproducible manual check.

## Failures and next steps

- **GPA and course display:** the calculator reads a course from the entire list
  instead of an individual entry. Nonempty GPA checks raise `AttributeError`, and
  the course-list page returns a server error (HTTP 500). Correct the calculation
  and unknown-grade handling, then repeat those checks.
- **Grade editing:** the editing URL returns “not found” (HTTP 404). Add the workflow
  and verify that a correction changes the GPA.
- **Deletion:** a tokenless request deletes a record. Validate the form's security
  token before changing records.

## Test scope

The 29 checks used `main` at `71737c8`, a temporary source copy and database,
Python 3.13.2, Flask 3.1.3, SQLAlchemy 2.1.3, and SQLite. Scripted requests exercised real forms
and account actions; separate calls checked the GPA library. Some sample records
were restored between checks. Repository data was unchanged.

Application code at the latest reviewed `main` (`5231a25`) is identical to the
tested revision; only the upstream README and ignore rules changed. No automated
test suite was added. The results establish the listed cases, not full browser
acceptance.
