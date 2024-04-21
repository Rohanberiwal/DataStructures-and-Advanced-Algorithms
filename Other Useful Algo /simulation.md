## Simulation-Based Approach

1. **Initialization**:
   - Start with a while loop that continues until there are no more students left in the queue (`students` list is empty).

2. **Check Preference**:
   - Inside the loop, check if the preference of the student at the front of the queue (`students[0]`) matches the type of sandwich at the top of the stack (`sandwiches[0]`).
   - If the preferences match:
     - Remove both the student and the sandwich from their respective lists using `pop(0)`.

3. **Check for Stalemate**:
   - If all remaining students have the same preference (indicated by the condition `len(Counter(students).keys()) == 1`), it means none of the students can eat any of the remaining sandwiches.
   - In this case, return the number of students remaining (`len(students)`).

4. **Rotate Queue**:
   - If the preferences don't match, rotate the queue by moving the student at the front of the queue to the end.
   - This is done by popping the first student (`s = students.pop(0)`) and then appending them to the end of the queue (`students.append(s)`).

5. **Return Remaining Sandwiches**:
   - If the loop exits without encountering a stalemate, return the number of remaining sandwiches (`len(sandwiches)`).
   - This indicates the number of students who couldn't eat.

