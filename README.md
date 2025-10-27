Running the script opens a new window with the GUI

A random sudoku is generated and printed to console for testing purposes.
Random spots in the sudoku is set to 0, the number of replacements depends on the current difficulty setting (defoult 1, with 45 numbers filled in already)
The GUI will show a sudoku with the 0s replaced with a text box

- NEW SUDOKU button will create a new sudoku using the current difficulty setting, as seen on the DIFFICULTY button.
- The DIFFICULTY button toggles through the difficulty settings
- CHECK button will run tests, marking user-filled textboxes with issues by changing the textbox background to red. Any textbox with a value that already exists in the row, column, or box will be marked.
  - Any input is first reduced to just the first character in the box. Then if input is not a number between 1-9, the box will be emptied.
  - Then the script checks the rows, columns, and blocks.
- The sudoku will only update the marked spaces when the CHECK button is clicked.

If all test complete successfully, the sudoku board will turn green.
