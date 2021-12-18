# cli_tasks
https://vimeo.com/648902045
## current complexity of app:
 FAIL  ./task.test.js (17.548 s)
 - √ prints help when no additional args are provided (447 ms)
 - √ prints help (475 ms)
 - √ add a single tasks (473 ms)
 - √ show error message when add is not followed by a tasks (423 ms)
 - √ add multiple tasks (1413 ms)
 - × list tasks in order of priority (1687 ms)
 - × list when there are no remaining tasks (541 ms)
 - √ delete a task (1878 ms)
 - × delete tasks numbered 3, 2 & 1 (1850 ms)
 - √ delete first task 3 times (2759 ms)
 - × delete non-existent tasks (1906 ms)
 - × delete does not have enough arguments (430 ms)
 - √ mark a tasks as done (1775 ms)
 - × mark as done a tasks which does not exist (1758 ms)
 - × mark as done without providing a tasks number (1659 ms)
 - × report pending & completed tasks (2150 ms)
 
##### Test Suites: 1 failed, 1 total
##### Tests:       8 failed, 8 passed, 16 total
##### Snapshots:   0 total
##### Time:        22.659 s
##### Ran all test suites.
