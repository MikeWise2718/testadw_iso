# Feature: Add Question Mark to Hello World Output

## Metadata
issue_number: `1`
adw_id: `8b979918`
issue_json: `{"number":1,"title":"Add an question mark.","body":"feature  - we want the hello world output to have a question mark appended."}`

## Feature Description
This feature modifies the existing hello world output to include a question mark at the end, changing the output from "Hello world" to "Hello world?". This simple enhancement adds punctuation to make the greeting more inquisitive.

## User Story
As a user running the main.py script
I want to see "Hello world?" with a question mark
So that the output has proper punctuation and a more engaging tone

## Problem Statement
The current main.py script outputs "Hello world" without any punctuation, which could be improved with a question mark to give it a more interactive and friendly tone.

## Solution Statement
Update the print statement in main.py to append a question mark to the "Hello world" string, changing it to "Hello world?". This is a straightforward single-line change that will be validated with a unit test.

## Relevant Files
Use these files to implement the feature:

- `main.py` - Contains the current "Hello world" print statement that needs to be modified to include a question mark

### New Files
- `test_main.py` - Unit test file to validate the hello world output includes the question mark

## Implementation Plan
### Phase 1: Foundation
No foundational work is required. This is a simple modification to an existing print statement.

### Phase 2: Core Implementation
Modify the print statement in main.py to change "Hello world" to "Hello world?" by appending a question mark to the string.

### Phase 3: Integration
No integration work is required. The change is self-contained within main.py and doesn't affect any other components.

## Step by Step Tasks
IMPORTANT: Execute every step in order, top to bottom.

### Task 1: Create unit test for main.py output
- Create a new file `test_main.py` in the root directory
- Import necessary testing modules (pytest or unittest)
- Write a test function that captures stdout when main.py is executed
- Assert that the output equals "Hello world?" with the question mark
- Ensure the test is structured to follow Python testing best practices

### Task 2: Modify main.py to add question mark
- Open `main.py`
- Locate the print statement on line 1
- Change `print("Hello world")` to `print("Hello world?")`
- Save the file

### Task 3: Run validation commands
- Execute all validation commands listed below to ensure the feature works correctly
- Verify the unit test passes
- Confirm the output displays "Hello world?" when running main.py directly

## Testing Strategy
### Unit Tests
- Create `test_main.py` with a test that captures the output of the main module
- Test should verify the exact output is "Hello world?" including the question mark
- Test should handle both the actual output and any trailing whitespace/newlines appropriately

### Edge Cases
- Verify the question mark is included in the output
- Verify there are no extra spaces or characters
- Verify the output format matches expected encoding (UTF-8)

## Acceptance Criteria
- The main.py file prints "Hello world?" with a question mark when executed
- A unit test exists that validates the output includes the question mark
- The unit test passes successfully when run with pytest
- Running `python main.py` directly shows "Hello world?" in the terminal
- No regressions are introduced

## Validation Commands
Execute every command to validate the feature works correctly with zero regressions.

- `python main.py` - Verify the output is "Hello world?" with the question mark
- `uv run pytest test_main.py -v` - Run the new unit test to validate the output format
- `uv run pytest` - Run all tests to ensure zero regressions across the codebase

## Notes
- This is a simple one-line change but demonstrates the importance of proper testing even for small modifications
- The unit test will serve as regression protection if the output format needs to change in the future
- Consider using `capsys` fixture in pytest for capturing stdout in the test
- The test should be maintainable and clearly document the expected output format
