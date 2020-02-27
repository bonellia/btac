## Requirements:
- A client library should be implemented.
- A programming language that is seen fit should be used.
- The following task should be solved:
    * Search for invalid values (e.g '111111', '12345678')
    * Update users in order to default them to empty string.
    * Report all instances.

### Decisions made prior to implementation:
- Python is to be used as the programming language.
- The project should contain two files:
    - `btac.py` : The library that contains various methods.
    - `main.py` : The driver file which demonstrates usage of the library.

### Stuff learned during development of the demo:

- __Markdown:__\
Priorly, I've used Markdown online in various websites for years. I have also created README files, but I didn't really pay much attention to formatting them, since plain text was sufficient for my purposes. In this project, I wanted to explain a bit more to reflect my thought process as well as explaining the usage of this simple library, so I completed [this neat little interactive tutorial for markup.](https://commonmark.org/)

- **\*args and \*\*kwargs:**\
These two are used to provide non-keyworded and keyworded variables to functions in Python, respectively. Obviously enough, (from C argc and argv parameters) the names "args" and "kwargs" come from conventions, meaning asterisk `*` characters are necessary but the names followed could be anything, such as "var", "vars" etc. There seems to be a lot of use cases for these two which I haven't needed before, but the most relevant use case in our context would be passing JSON as a parameter in our functions. More info can be find [here.](https://book.pythontips.com/en/latest/args_and_kwargs.html)

- `pip freeze > requirements.txt`\
Turns out you don't need to manually save your dependencies and their versions manually, since this pip command automatically saves them into `requirements.txt` file. There seems to exist equivalent tools for `bower.json` or `package.json` as well if I were to work with node.js. [A lengthy medium article which I didn't bother reading comprehensively.](https://medium.com/@boscacci/why-and-how-to-make-a-requirements-txt-f329c685181e)

- **f-strings:**\
I have been using string interpolation (or templates) since I learned about it [when I was getting familiar with ECMAScript6 a while ago](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals). While developing with Java, I felt the absense of this feature and fortunately Python already has it. Quickly had a look on official docs to learn Python alternative. It basically helps substituting variables on strings like URLs. More about them in [here](https://www.python.org/dev/peps/pep-0498/).