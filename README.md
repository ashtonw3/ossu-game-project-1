# OSSU Game Project

## Purpose

This project is here to help people in the [OSSU](https://github.com/ossu/computer-science)
program get their feet wet with a real project. We'll follow a lot of the normal
process that you'd follow when writing code for a company.

## Setup

We're using virtualenvs with Python 3.10, ensure you're using something similar:

```
python3 --version
```

To get started, create a virtual environment:

```
python3 -m venv .
```

Activate the virtual environment based on the operating system you're using. See
the Python documentation on [activating your venv](https://docs.python.org/3/library/venv.html#how-venvs-work)
for more details on how to activate it for your platform.

Once you're activated, install any requirements necessary:

```
pip install -r requirements.txt
```

That should have everything all set up. Just run the game:

```
python main.py
```

## Coding

### Contributing

To contribute:

- Grab an unclaimed issue in the [issues](https://github.com/robbrit/ossu-game-project-1/issues)
  section.
- If you need clarification, just ask.
- If you have an idea, feel free to create an issue for it, but get buy-in from
  @robbrit before spending a lot of time on it.
- Fork the repo to start working on your change.
- When you're done, send a pull request.

Before sending it though, ensure:

- You're following the formatting guidelines listed below.
- You're using [mypy](https://mypy-lang.org/) type annotations.
- You're following the style guide as defined below.
- You specify which issue you're completing.

### Formatting

We're using black to format the code. Why? Because I don't like to argue about
formatting. Just use the default settings.

#### Function Breaks

Sometimes black will format a multiline function call like this:

```python
func(
    arg1, arg2, arg3
)
```

This is tricky to read. In order to get black to format this nicely, put a comma
at the end:

```python
func(
    arg1, arg2, arg3,
)
```

This will cause black to format it with one argument per line:

```python
func(
    arg1,
    arg2,
    arg3,
)
```

### Style

Use the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)
to style your code.

In the case of a conflict between black's defaults and the style guide, prefer
the black version.

Note that reviewers may not know/remember the style guide 100%, so feel free to
mention (with references) when a review comment violates it.
