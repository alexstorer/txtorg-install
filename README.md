Mac txtorg Installation
==============
* Download this repository (https://github.com/alexstorer/txtorg-install/archive/master.zip)
* Unzip it
* Double-click on the file named "install"

txtorg and all of its dependencies (including PyLucene) should install
automatically.

Notes
-----------------

* To uninstall from the terminal, run the remove script as `sh remove`
* The eggs used here are for Python 2.6!  This may not work forever.

Hey, that didn't work!
==============

That happens sometimes.

1.  Install the Command Line Tools for Mac OS-X by typing the
following into the Terminal:
`xcode-select --install`

(If that doesn't work, try it directly [here](http://developer.apple.com/downloads))

2.  Install Homebrew from the Terminal:
`ruby -e "$(curl -fsSL
https://raw.github.com/Homebrew/homebrew/go/install)"`

Homebrew will instruct you to run a few commands -- please follow its
instructions and make sure it's up to date before continuing!

3.  Install PyLucene from the Terminal:
`brew install pylucene`

If this doesn't work, please follow the instructions to install
PyLucene from source:

http://lucene.apache.org/pylucene/install.html

You will know that PyLucene has been installed correctly if you can
open the Terminal, and start Python (by typing `python`).  In the
Python terminal, type `import lucene`.  If there is no error, it
worked!

4.  More coming!
