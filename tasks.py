"""
python3 -m venv .venv
source .venv/bin/activate

inv <task>

deactivate
"""

from invoke import task


@task
def vs(c):
    "virtualenv setup"
    c.run("pip install -r requirements.txt")


@task
def vrf(c):
    "virtualenv requirements freeze"
    c.run("pip freeze > requirements.txt")


@task
def ds(c):
    "docs serve"
    c.run("mkdocs serve")
