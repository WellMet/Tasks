.. Filename: README.rst

##########
README
##########

This is a small guide to Git and Github/Gitlab

.. _Getting_Started:

***************
Getting Started
***************

The purpose of this page is to discuss and guide in the purpose and
use of the Git VCS (Version Control System).  Some key terms:

**Git/git**
    Git is the most widely used VCS system in use around the world today. It
    allows developers to each work on a codebase simultaneously without the 
    need of a centralized area or fear of any mishaps. Git backs up everything
    (that you tell it to). More on Git for those interested: Git_ 

    .. _Git: https://git-scm.com/

**GitHub**
    A web service recently bought by Microsoft. Used to *host* Git based projects.
    GitHub provides additonal benefits such as code reviews, home pages, easy release system,
    hooks, and more.

**GitLab**
    An up and coming competitor to GitHub. Features everything that GitHub provides
    and more, including some additional continous integration and operational fun stuff.

**VCS**
    **V** ersion **C** ontrol **S** ystem. Git is a subset of all VCS tools.
    Others you may have heard of: SVN, Perforce, Google Drive (pls no), Flash drives (pls, pls no)
    There are many types, wheras the most common are Distributed-VCS_ (Git is one) and Centralized-VCS_ (SVN)

    .. _Distributed-VCS: https://en.wikipedia.org/wiki/Distributed_version_control

    .. _Centralized-VCS: https://en.wikipedia.org/wiki/Version_control

**Repo/Repository**
    A container (think like a big folder) that holds the source for a project.

.. note:: Intel has been using GitHub Enterprise (corporation private hosting) for sometime
    now as its default Git hoster, but recently we are switching to GitLab. GitHub
    is the most widely used in the opensource community and otherwise.


Now, before we do any thing let's check for permissions:
Try visiting our FEDA-Github_.

.. _FEDA-Github: https://github.intel.com/feda

If you can poke around in there we are good.
Next, let's grab the repository this came from and explore some functionality.
Go ahead and Shift+RightClick in a folder you want to clone the repo in, and select
Git Bash.  Within the terminal type the *commands* marked below.
(Comments are marked with '#', commands are marked with '$')

.. code-block:: console

    # Set the global proxy
    $ git config --global http.proxy http://proxy-chain.intel.com:911
    $ git config --global https.proxy https://proxy-chain.intel.com:912

    $ git clone https://github.com/WellMet/Tasks.git


***************
Common Commands
***************

This is a shortcut command section for reference.

....

**Getting a repo**

    *git clone https://some-repo-here*      
        The clone command is used to get an existing repo
        for the first time.

    *git init*      
        When you are in a folder, use this to start a brand new git repo within
        that folder.

**Viewing**

    *git status*
        Reveal what is staged and unstaged with changes.
    
    *git log*
        View the commit history tree.

**Save stuff**

    *git add [\*/folder/file]*
        Stage whatever you have changed in the given folder, file or everything (* = wildcard character, means everything in current and sub folders)

    *git commit -m "Some message here"*
        Add your work to the committed tree with a message.

**Interacting with Server**

    *git push*
        Use this within your repo after committing to upload the changes to Github / wherever.
    
    *git pull*
        Use this within your repo to get any changes made since your last pull or clone made by someone else

**Tags**

    *git tag -a [release name] -m "release notes"*
        Tag a commit as a release

    *git push --tags*
        Upload the tag
    