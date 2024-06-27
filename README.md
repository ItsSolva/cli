
# Report for Assignment 1

## Project Chosen

**Name:** HTTPie CLI: human-friendly HTTP client for the API era

**URL:** [https://github.com/httpie/cli](https://github.com/httpie/cli)

**Number of lines of code and the tool used to count it:**
The HTTPie CLI project has around 14,924 lines. The Lizard library was used to count the amount of lines.

![lizard](/readme_images%20/Picture%201.png)


**Programming language:** Python

## Coverage Measurement

### Existing Tool

Since the project we chose is written in Python, we used `coverage.py` tool for checking if our tests cover functions and branches within the chosen code.

After following the installation steps provided in the manual as a link to the documentation, and running the tests with the command `coverage run -m --branch pytest tests`, followed by running the command `coverage report -m`, we get this:

![lizard](/readme_images%20/coverage1.png)
![lizard](/readme_images%20/coverage2.png)
#
### Your Own Coverage Tool

For our own coverage tool, we created the following functions:
- `test_print_coverage()`: This functions checks all flags in every branch and prints whether or not the branch has been reached.
- `get_coverage_percentage()`: This functions calculates the branch coverage.
- `print_colored()`: This function is used in the `test_print_coverage()` function for a more visual result of the branch coverage. 

#

#### Mohamed
**cli_sessions()**
- Link to commit: https://github.com/httpie/cli/commit/8dc36b271548e8371cb48d388c799bb2fb73cd63
- Old Coverage 71%:

![lizard](/readme_images%20/coverage_cli_sessions.png)
 
- New Coverage (with our own tool):

![lizard](/readme_images%20/new_coverage_sessions.png)
 
 - How?
  - Added these flags to every branch for our own tool to check which branch has been reached.

![lizard](/readme_images%20/coverage_branches_sessions.png)

  - Then we created a new test file and we added these tests:

![lizard](/readme_images%20/tests_sessions.png)

  - Lastly, we output the coverage with this print function:

![lizard](/readme_images%20/print_coverage.png)

  - To run the test, we use the following command:

  `python -m pytest -s our_tool/test_cli_sessions.py`
  
#

**get_site_paths()**
- Link to commit: https://github.com/httpie/cli/commit/3f898e26874b1dcec026c00909c7dc59ca0ddac5
- Old Coverage 36%:

![lizard](/readme_images%20/coverage_site.png)
 
- New Coverage (with our own tool):

![lizard](/readme_images%20/new_coverage_site.png)
 
 - How?
  - Added these flags to every branch for our own tool to check which branch has been reached.

![lizard](/readme_images%20/branch_site.png)

  - Then we created a new test file and we added these tests:

![lizard](/readme_images%20/test_site.png)

  - Lastly, we output the coverage with this print function:

![lizard](/readme_images%20/print_coverage.png)

  - To run the test, we use the following command:
`python -m pytest -s our_tool/test_utils.py`

- Tests about get_site_paths improved:

- Old Coverage 36%:

#

#### Christina
**load_text_file()**:
- Link to commit: https://github.com/httpie/cli/commit/8dc36b271548e8371cb48d388c799bb2fb73cd63
- File path: `httpie/cli/requestitems.py`
- Old coverage of the function: 30%

![lizard](/readme_images%20/coverage_load.png)

- New Coverage (with our own tool)

![lizard](/readme_images%20/new_coverage_load.png)

- How?
  - We added flags to every branch for our own tool to check which branch has been reached.

![lizard](/readme_images%20/branches_load.png)
  - Then we created a new test file in our tool and we added these tests:

![lizard](/readme_images%20/test_load.png)

  - Lastly, we print our coverage by this function:

![lizard](/readme_images%20/print_coverage.png)

  - To run the test, we use the following command:
  `python -m pytest -s our_tool/test_requestitems.py`
  
#

**print_manual()**
  - Link to commit: https://github.com/httpie/cli/commit/ea48fbc194bbfd9c049c6593c317daf664a80f10
  - File path: `httpie/cli/argparser.py`

  - Old coverage of the function: 0%
    
![lizard](/readme_images%20/print_manual.png)

  - New Coverage (with our own tool)
  
![lizard](/readme_images%20/new_print_coverage.png)

  - How?
    - We added flags to every branch for our own tool to check which branch has been reached.

![lizard](/readme_images%20/branches_manual.png)

  - Then we created a new test file in our tool and we added these tests:

![lizard](/readme_images%20/test_manual.png)

  - Lastly, we print our coverage by this function:

![lizard](/readme_images%20/print_coverage.png)

  - To run the test, we use the following command:
  `python -m pytest -s our_tool/test_argparser.py`

#

#### Alua:
**write_message()**:
- Link to commit: https://github.com/httpie/cli/commit/ed2a3271bb7a68057dc8f15b886cb37374afc0d7
- File path: `httpie/output/writer.py`
- Old coverage: 79%

![lizard](/readme_images%20/write_message.png)

- New Coverage (with own tool): 100%

![lizard](/readme_images%20/new_coverage_write.png)

- Running the command:

- How?
  - We added flags to every branch for our own tool to check which branch has been reached.

![lizard](/readme_images%20/branch_write.png)

  - Then we created a new test file in our tool and we added these tests:

![lizard](/readme_images%20/branch_test.png)
  
  - Then, we print coverage with our own tool using this function:

![lizard](/readme_images%20/print_coverage.png)

  - To run the test, we use the following command:
  `python -m pytest -s our_tool/test_writer.py`
  
#

**__iter__()**
- Link to commit: https://github.com/httpie/cli/commit/ebb711eed69f848e0db27abbe5d7e55a7a83ec32
- File path: `httpie/uploads.py`
- Old coverage of function: 0%

![lizard](/readme_images%20/iter.png)

- New coverage: 100%

![lizard](/readme_images%20/new_coverage_uploads.png)

- How?
  - We added these flags to every branch for our own tool to check which branch has been reached.

![lizard](/readme_images%20/branch_iter.png)

  - Then we created test functions for each branch:

![lizard](/readme_images%20/print_coverage.png)

  - Then, we print coverage with our own tool using this function:

![lizard](/readme_images%20/print_coverage.png)

  - To run the test, we use the following command:
  
  `python -m pytest -s our_tool/test_uploads.py`
  
#

#### Bo:
**get_dist_name()**
- Link to commit: https://github.com/httpie/cli/commit/7079a1de79fa966772333bf7ae90f4e1d4ca2457
- Path: `httpie\compat.py`
- Old coverage: 0%

![lizard](/readme_images%20/name.png)

- New coverage: 100%

![lizard](/readme_images%20/new_coverage_name.png)

- How?
  - Added these flags to every branch for our own tool to check which branch has been reached.

![lizard](/readme_images%20/branches_name.png)

  - Then we created a new test file and we added these tests:
  
![lizard](/readme_images%20/tests_name.png)

  - Lastly, we output the coverage with this print function:

![lizard](/readme_images%20/print_coverage.png)

  - To run the test, we use the following command:

  `python -m pytest -s our_tool/test_get_dist_name.py`
  
#

**fetch_updates()**
  - Link to commit: https://github.com/httpie/cli/commit/0689242bccb89f6703d574103e789af8ca9c5fa6
  - Path: `httpie\internal\update_warnings.py`
  - Old coverage: 0%

  ![lizard](/readme_images%20/fetch.png)

  - New coverage: 100%

  ![lizard](/readme_images%20/new_coverage_fetch.png)

  - How?
    - Added these flags to every branch for our own tool to check which branch has been reached.

  ![lizard](/readme_images%20/branch_fetch.png)

    - Then we created a new test file and we added these tests:
   
  ![lizard](/readme_images%20/test_fetch.png)

    - Lastly, we output the coverage with this print function:
   
   ![lizard](/readme_images%20/print_coverage.png)
  
  - To run the test, we use the following command:

  `python -m pytest -s our_tool/test_update_warnings.py`
  
#    

### Overall

**Total Old Coverage (89%)**

![lizard](/readme_images%20/coverage1.png)
![lizard](/readme_images%20/coverage2.png)

**Total New Coverage(91%)**
![lizard](/readme_images%20/new_total_coverage4.png)
![lizard](/readme_images%20/new_total_coverage3.png)
![lizard](/readme_images%20/new_total_coverage2.png)
![lizard](/readme_images%20/new_total_coverage1.png)

## Statement of Individual Contributions

**Mohamed**
- Assisted in researching potential projects.
- Selected and instrumented functions for coverage measurement. 
- Developed and enhanced test cases. 
- Prepared sections of the final report. 
 
**Christina**
 - Assisted in researching potential projects.
 - Selected and instrumented functions for coverage measurement.
 - Developed and enhanced test cases.
 - Compiled findings into the README.md.

**Alua**
 - Found the project.
 - Selected and instrumented functions for coverage measurement.
 - Developed and enhanced test cases. 
 - Prepared sections of the final report. 

 **Bo** 
 - Reviewed project criteria and ensured compliance. 
 - Selected and instrumented functions for coverage measurement. 
 - Developed and enhanced test cases. 
 - Reviewed push requests. 



