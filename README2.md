# This is an <h1> tag
## This is an <h2> tag
###### This is an <h6> tag

--------

*This text will be italic*
_This will also be italic_

**This text will be bold**
__This will also be bold__

_You **can** combine them_

--------

* Item 1
* Item 2
  * Item 2a
  * Item 2b
  
1. Item 1
1. Item 2
1. Item 3
   1. Item 3a
   1. Item 3b

--------
   
![GitHub Logo](/images/logo.png)
Format: ![Alt Text](url)

http://github.com - automatic!
[GitHub](http://github.com)

--------

As Kanye West said:
> We're living the future so
> the present is our past.

--------

I think you should use an
`<addr>` element here instead.

--------

```javascript
function fancyAlert(arg) {
  if(arg) {
    $.facebox({div:'#foo'})
  }
}
```
    
    function fancyAlert(arg) {
      if(arg) {
        $.facebox({div:'#foo'})
      }
    }

--------

```python
def foo():
    if not bar:
        return True
```

--------

- [x] @mentions, #refs, [links](), **formatting**, and ~~tags~~ supported
- [x] list syntax required (any unordered or ordered list supported)
- [x] this is a complete item
- [ ] this is an incomplete item

--------

First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column


# Full-stack Framework:

Django # _Используем всегда где можно_

Pyramid # _Используем крайне редко_

Web2Py # _Используем крайне редко_

Pylons  # _Не используем_

TurboGears # _Не используем_

CubicWeb # _Не используем_

Giotto # _Не используем_

Grok # _Не используем_

# Asynchronous Framework:

AIOHTTP # _Используем для асинхронных приложений_

Tornado # _Используем крайне редко_

Sanic # _Используем крайне редко_

Growler # _Не используем_

Muffin # _Не используем_

Vibora # _Не используем_

WebCore # _Не используем_

# Micro Framework:

Flask # _Используем для микро-приложений_

Bottle # _Используем крайне редко_

CherryPy # _Используем крайне редко_

Falcon # _Используем крайне редко_

Web.py # _Не используем_

Dash # _Не используем_

BlueBream # _Не используем_

Hug # _Не используем_

MorePath # _Не используем_

Pycnic # _Не используем_

Quixote # _Не используем_

Zope # _Не используем_

Nevow # _Не используем_

Bobo # _Не используем_

Ray # _Не используем_


Краткое описание проекта

Как запустить проект

Все сервисы

Если есть АПИ то ссылка на АПИ

--------

# Venv 

```
python3 -m venv /path/to/new/virtual/environment 

source venv/bin/activate

deactivate
```

# Virtualenvwrapper

```
pip3 install virtualenvwrapper

mkvirtualenv [venv-name]

workon [venv-name]

source deactivate
```

# [Pipenv](https://github.com/pypa/pipenv)

```
pip3 install pipenv

pipenv --python 3.8

pipenv shell

exit

pipenv install [lib][==<version>] [--dev]

pipenv uninstall [lib]

pipenv run python script.py

pipenv lock

pipenv install --system
```

# [Pyenv](https://github.com/pyenv/pyenv)

```
curl https://pyenv.run | bash

pyenv install [version]

pyenv uninstall [version]

pyenv local [version]

pyenv global [version]

pyenv shell [version]

pyenv version

pyenv versions

pyenv virtualenv [version] <virtualenv-name>

pyenv virtualenvs
```

# Git

### Getting & Creating Projects

| Command | Description |
| ------- | ----------- |
| `git init [repository path_name/None]` | Initialize a local Git repository |
| `git clone ssh://git@github.com/[username]/[repository-name].git` | Create a local copy of a remote repository |
| `git clone https://www.github.com/[username]/[repository-name].git` | Create a local copy of a remote repository |

### Basic Snapshotting

| Command | Description |
| ------- | ----------- |
| `git status` | Check status |
| `git add [file-name.txt]` | Add a file to the staging area |
| `git add -A` | Add all new and changed files to the staging area |
| `git add *` | Add all new and changed files to the staging area |
| `git add .` | Add all new and changed files to the staging area from root |
| `git commit -m "[commit message]"` | Commit changes |
| `git rm -r [file-name.txt]` | Remove a file (or folder) |

### Branching & Merging

| Command | Description |
| ------- | ----------- |
| `git branch` | List branches (the asterisk denotes the current branch) |
| `git branch -a` | List all branches (local and remote) |
| `git branch [branch name]` | Create a new branch |
| `git branch -d [branch name]` | Delete a branch |
| `git push origin --delete [branch name]` | Delete a remote branch |
| `git checkout -b [branch name]` | Create a new branch and switch to it |
| `git checkout -b [branch name] origin/[branch name]` | Clone a remote branch and switch to it |
| `git branch -m [old branch name] [new branch name]` | Rename a local branch |
| `git checkout [branch name]` | Switch to a branch |
| `git checkout -` | Switch to the branch last checked out |
| `git checkout -- [file-name.txt]` | Discard changes to a file |
| `git merge [branch name]` | Merge a branch into the active branch |
| `git merge [source branch] [target branch]` | Merge a branch into a target branch |
| `git stash` | Stash changes in a dirty working directory |
| `git stash clear` | Remove all stashed entries |
| `git stash save` | Save all stashed files |
| `git stash pop` | Restore last stash |
| `git stash discard` | Discard last stash |
| `git stash list` | Show list of stash |
| `git stash append` | Load all stash of stash |
| `git reset [file]` | Reset file or everything to a previous state|

### Sharing & Updating Projects

| Command | Description |
| ------- | ----------- |
| `git push origin [branch name]` | Push a branch to your remote repository |
| `git push -u origin [branch name]` | Push changes to remote repository (and remember the branch) |
| `git push` | Push changes to remote repository (remembered branch) |
| `git push origin --delete [branch name]` | Delete a remote branch |
| `git push –all [variable name]` | Git push all branches |
| `git pull` | Update local repository to the newest commit |
| `git pull origin [branch name]` | Pull changes from remote repository |
| `git remote add origin ssh://git@github.com/[username]/[repository-name].git` | Add a remote repository |
| `git remote set-url origin ssh://git@github.com/[username]/[repository-name].git` | Set a repository's origin branch to SSH |

### Inspection & Comparison

| Command | Description |
| ------- | ----------- |
| `git log` | View changes |
| `git log --summary` | View changes (detailed) |
| `git log --oneline` | View changes (briefly) |
| `git diff` | Show changes |
| `git diff [source branch] [target branch]` | Preview changes before merging between branches |

### Configuration

| Command | Description |
| ------- | ----------- |
| `git config --list`| Display config |
| `git config –global user.name “[name]”` | Set username globally |
| `git config –global user.email “[email address]”` | Set email globally |
