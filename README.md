# cli_tasks
https://vimeo.com/648902045
## current complexity of app:
 FAIL  ./task.test.js (17.548 s)
 - √ prints help when no additional args are provided (378 ms)
 - √ prints help (360 ms)
 - √ add a single tasks (371 ms)
 - √ show error message when add is not followed by a tasks (377 ms)
 - √ add multiple tasks (1062 ms)
 - × list tasks in order of priority (1350 ms)
 - × list when there are no remaining tasks (349 ms)
 - √ delete a task (1392 ms)
 - √ delete tasks numbered 3, 2 & 1 (1981 ms)
 - √ delete first task 3 times (1911 ms)
 - × delete non-existent tasks (1376 ms)
 - × delete does not have enough arguments (338 ms)
 - √ mark a tasks as done (1324 ms)
 - × mark as done a tasks which does not exist (1261 ms)
 - × mark as done without providing a tasks number (1260 ms)
 - × report pending & completed tasks (2089 ms)
 
##### Test Suites: 1 failed, 1 total
##### Tests:       7 failed, 9 passed, 16 total
##### Snapshots:   0 total
##### Time:        17.622 s
##### Ran all test suites.
