### Stuff learned during development of the demo:

- __Markdown:__\
Priorly, I've used Markdown online in various websites for years. I have also created README files, but I didn't really pay much attention to formatting them, since plain text was sufficient for my purposes. In this project, I wanted to explain a bit more to reflect my thought process as well as explaining the usage of this simple library, so I completed [this neat little interactive tutorial for markup.](https://commonmark.org/)

- **\*args and \*\*kwargs:**\
These two are used to provide non-keyworded and keyworded variables to functions in Python, respectively. Obviously enough, (from C argc and argv parameters) the names "args" and "kwargs" come from conventions, meaning asterisk `*` characters are necessary but the names followed could be anything, such as "var", "vars" etc. There seems to be a lot of use cases for these two which I haven't needed before, but the most relevant use case in our context would be passing JSON as a parameter in our functions. More info can be find [here.](https://book.pythontips.com/en/latest/args_and_kwargs.html)

- `pip freeze > requirements.txt`\
Turns out you don't need to manually save your dependencies and their versions manually, since this pip command automatically saves them into `requirements.txt` file. There seems to exist equivalent tools for `bower.json` or `package.json` as well if I were to work with node.js. [A lengthy medium article which I didn't bother reading comprehensively.](https://medium.com/@boscacci/why-and-how-to-make-a-requirements-txt-f329c685181e)

- **f-strings:**\
I have been using string interpolation (or templates) since I learned about it [when I was getting familiar with ECMAScript6 a while ago](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals). While developing with Java, I felt the absense of this feature and fortunately Python already has it. Quickly had a look on official docs to learn Python alternative. It basically helps substituting variables on strings like URLs. More about them in [here](https://www.python.org/dev/peps/pep-0498/).

- **Entropy and password strengths**\
Ensuring that passwords are not extracted or guessed trivially by brute-force requires grasping and computing entropy. [As stated in an online discussion](https://stackoverflow.com/questions/22277493/calculating-entropy-for-user-and-random-passwords), this problem seems simple but gets surprisingly difficult with unknown constraints. How these concept are very relevant to the subjects of the courses I'm taking this semester (statistics and security) is quite nice. I've tried not to get drifted away reading information which I won't need (and probably forget soon), but apparently there are a lot to read in this subject given that it is a fundamental topic for communication, cryptography, compression and more. Priorly, I've associated the term only with thermodynamics which I wasn't also deeply informed . [The wiki page for further reference.](https://en.wikipedia.org/wiki/Entropy_(information_theory)) Also, it turns out there is a famous xkcd with the title "[xkcd: Password Strength](https://xkcd.com/936/)" about this topic.

### Random thoughts:

- Building a client API involves completing a lot of "nobrainer" tasks such as manually creating a lot of different functions which are very similar but requires slight modifications. This could be automated partially, if the code was not documented respecting [docstring conventions](https://www.python.org/dev/peps/pep-0257/). Trying to minimize amount of code repetition can get annoying, but I think it makes you appreciate OOP principles and modular, reusable code more at least. I'll probably not going to "overly optimize" the library though.

- "Entropy of a string" is nonsense, the correct expression is probably "entropy of the possible strings given a pattern". Regular expressions come into play once again. When it comes to the library, I should probably just use a simple algorithm and move on, this is getting too deep for just a demo.

- Since the requests are going to be asynchronous, async/await-like approach should be utilized. Also exception handling could be added, but the demo is there to "demonstrate", it is not a hobby project or anything, so I'll not spend hours figuring these out for now.