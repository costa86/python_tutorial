============
Virtual environment
============

In most realistic scenarios, it's very likely that you will use third-party libraries, as they tend to contain many useful functionalities already 
developed by someone else, so you can connect them to your programs.

You can install these libraries locally on your computer, but the recommended approach is to avoid doing so, and use a virtual environment instead.
A virtual environment (let's call it "venv" from now on) is an isolated environment where you can install third-party libraries without interfering 
with the default local environment on your computer.
Think of a venv as a box that can hold many third-party libraries. You can then work on and run your Python programs 
relying only on those libraries available inside this box. You can create multiple venvs.

Using a venv is considered a convention in most Python programs, as it provides many advantages in terms of security, 
reproducibility and management of the program as a whole.

Let's create a folder named "my_project" and enter it. All the commands from now on will assume you are in this folder!

Create a venv named "myenv" via command-line:

.. code-block:: console

    $ python3 -m venv myenv


This command is expected to have created a folder named "myenv". I suggest you check that.

In order to start working with the "myenv" venv, it needs to be activated. Do it via command line:

Linux or macOS

.. code-block:: console
    
    source myenv/bin/activate 


Windows

.. code-block:: console
    
    source myenv\Scripts\activate.bat 


.. note::

    On Linux or macOS, you can write a period “ . ” instead of “source”, to activate a venv, as a shortcut.

If the activation worked, you should see "(myenv)" at the beginning of your terminal, as such:

.. code-block:: console

    (myvenv) $

.. warning::

    From now on, all the commands assume you have "myvenv" activated.

Now you can start installing third-party libraries. Let's install a library called "pydantic" via command-line using the ``pip`` program. 
This library will be used in the Classes chapter:

.. code-block:: console

    $ pip install pydantic


.. note::

    ``pip`` is a package manager tool that allows us to handle additional libraries that are not part of the standard Python library. 
    We typically use it to install and uninstall third-party libraries.

.. note::

    If you get an error saying ``pip`` is not found, try ``pip3`` instead. If it still does not work, you’ll have to download and install it. 

Curious to see if it worked? This command will list all the libraries currently installed:

.. code-block:: console

    $ pip list

Then you should see something similar to this as an output:

.. code-block:: console

    Package	                Version
    ----------------           ---------
    pip	                          23.1.2
    Prompt-toolkit                3.0.38
    pydantic	                  1.10.7
    setuptools	                  65.5.0
    typing_extensions             4.5.0
___________________________________________________________________

Notice that "pydantic" version 1.10.7 is installed. The notion of "library version" is another reason to justify the usage of a venv, 
as to avoid libraries with conflicting version numbers.

If you don't specify the version you wish to install (as you just did), the installation defaults to the most recent one. 
But if you wish to pick a speciﬁc version instead, let's say 1.5.7:

.. code-block:: console

    $ pip install pydantic==1.5.7

If you want to install many libraries at once, you can write their names (one library per line) in a ﬁle (let's call it "requirements.txt"), then:

.. code-block:: console

    $ pip install -r requirements.txt

Finally, to deactivate (exit) a venv, run:

.. code-block:: console

    $ deactivate

Uv - An alternative to pip
----------------------------

Uv is a tool that can work as a direct replacement for pip to create venvs. 
Its main advantages are speed (seriously, it’s really fast!) and caching. These features may become very handy in situations such as 
having a project with many third-party libraries or when multiple venvs are required to be reproduced, 
since the caching mechanism can avoid the downloading of the libraries multiple times. 
Regardless of these scenarios, I strongly recommend that you use uv in any Python project. Download it at: https://pypi.org/project/uv/.
