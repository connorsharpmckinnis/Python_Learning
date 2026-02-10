Project 1: Configuration-Driven Command Tool
============================================

One-Sentence Goal
-----------------

Build a small Python command-line tool where almost all behavior is controlled by a config file, not hard-coded logic.

Simple on purpose. Clear on purpose.

* * * *

What You're Building
--------------------

You are creating a reusable CLI program called **`taskrunner`**.

`taskrunner`:

-   Reads a configuration file

-   Looks up a task by name

-   Runs that task using parameters defined *only* in the config

The program should be boring, predictable, and difficult to misuse.
That's success, not failure.

* * * *

How the Program Is Run
----------------------

From the command line:

```

`python taskrunner.py --task <task_name> [--config path/to/config.yaml]
`

```

Rules:

-   `--task` is required

-   `--config` is optional

        -   Defaults to `config.yaml` in the same directory as `taskrunner.py`

* * * *

Configuration File
------------------

You may use **YAML or JSON**.
YAML is recommended.

The config file must define:

-   Global settings

-   A collection of tasks

-   Per-task parameters and limits

Conceptual example (not required structure):

```

`global:retries:3timeout:5tasks:example_task:enabled:trueparameters:message:"Hello"constraints:max_length:100`

```

You decide the exact schema, **but you must document it** in the README.

* * * *

Tasks
-----

You must implement **at least 3 different task types**, such as:

-   A task that prints formatted output

-   A task that writes to a file

-   A task that simulates a network call (sleep + randomness)

Rules for tasks:

-   Tasks are selected by **name**, not `if/elif` chains

-   Disabled tasks must fail cleanly with a helpful message

-   Task logic must not care where its parameters came from

-   Tasks receive already-validated data

* * * *

Validation (This Is the Core)
-----------------------------

Before *any* task runs, the program must validate:

-   The config file exists

-   The config can be parsed

-   Required fields are present

-   Field types are correct

-   Values fall within allowed ranges

-   The requested task exists

-   The task is enabled

If validation fails:

-   Execution stops immediately

-   The error message explains:

        -   What went wrong

        -   Where in the config it happened

-   No stack traces for user mistakes

* * * *

Error Handling Rules
--------------------

You must clearly separate:

-   **User errors**

        -   Bad config

        -   Unknown task

        -   Invalid values

-   **Programmer errors**

        -   Logic bugs

        -   Broken assumptions

User errors get clean, readable messages.
Programmer errors can crash loudly.

You should be able to explain where that boundary is.

* * * *

Project Structure
-----------------

Suggested minimum structure (you may improve it):

```

`taskrunner/
│
├─ taskrunner.py
├─ config.yaml
├─ tasks/
│   ├─ __init__.py
│   ├─ base.py
│   ├─ print_task.py
│   └─ file_task.py
│
├─ config/
│   └─ loader.py
│
└─ README.md
`

```

No "everything in one file" solutions.

* * * *

Code Quality Expectations
-------------------------

-   Clear function and class boundaries

-   No magic numbers

-   No unnecessary global state

-   Type hints where they improve clarity

-   Readable over clever

* * * *

What You Must Turn In
---------------------

### 1\. Code

-   All source files

-   One **valid** config file

-   One **invalid** config file (intentional failure)

### 2\. README

Your README must explain:

-   What the program does

-   How to run it

-   The config schema

-   One known limitation

-   One design decision you struggled with

### 3\. Short Reflection

Briefly answer:

-   What was harder than you expected?

-   What part made you slow down and think?

-   What would you refactor first if this grew?

* * * *

Explicit Constraints (Read Carefully)
-------------------------------------

You may **NOT**:

-   Use external config validation libraries

-   Use `eval`, dynamic imports, or code-from-strings

-   Silently ignore unknown config values

You **MAY**:

-   Use the Python standard library freely

-   Use PyYAML if you choose YAML

-   Be slightly over-engineered if it improves clarity

* * * *

How This Will Be Evaluated
--------------------------

Primary focus:

-   How early validation happens

-   Whether tasks are truly decoupled from config parsing

-   Quality of error messages

-   Whether the code explains itself through structure

If it technically works but feels fragile, that will be called out.

* * * *

Final Thought
-------------

This project is about **control surfaces**:
deciding what users are allowed to change and what the program guarantees no matter what.

That's real software engineering---not scripting.