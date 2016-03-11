# FRCC Hacking Club
Front Range Community College Hacking Club projects

## Best practices for writing Pygame Code

* Please don't use anything specific to Python 2 or anything new in Python 3, so that it can run on all platforms. If you're calling the Python 2 interpreter (usually the default) from the command line, try using the -3 flag to show warnings about things that might break in 3. Most of the warnings will be related to the Pygame library itself
* Please use image and audio formats that are compatible on all platforms. For example, use Ogg Vorbis (.ogg) files for music instead of MP3. SDL should support .ogg out of the box on Windows and Mac, but even if it doesn't, you can update it with a version compiled to support that encoding. 24-bit PNG is usually the best format for images. Wave (.WAV) is acceptable for short sound effects.
* Please write docstrings for all of your functions and methods! Please see [this PEP document](https://www.python.org/dev/peps/pep-0257) for more on what a docstring is and how to write one. It's important to communicate what each function and method you wrote intended to do, as well as what data type the parameters are, so that other people using a function you wrote can know precisely how it is (intended to be) used, to avoid weird errors from passing an unintended argument or if the function needs to be rewritten.
* While you're at it, [the full PEP style guide](https://www.python.org/dev/peps/pep-0008/") is worth a read. Ignore the items mentioning concepts you haven't been introduced to, but at least look at the guidelines on indenting your code and naming your variables and functions.
