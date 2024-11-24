# LeetCode in Python

## Prerequisite
We use **Poetry** for dependency management. Please ensure that Poetry is installed on your system.

## How to Run Lint and Format
We use **flake8** and **black** as the linter and formatter, respectively.

You can run them using the following commands:

```sh
poetry run flake8 .
poetry run black .
```

## How to Run Code
To execute a specific solution file, you can use Poetry to run the corresponding script. For example, if you want to run the solution for `p20_valid_parentheses.py`, use the following command:

```sh
poetry run python src/leetcode/p20_valid_parentheses.py
```
