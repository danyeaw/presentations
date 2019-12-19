# Speaker Profile

## Name
Dan Yeaw

## Biography
Dan Yeaw is an engineer who helps design safety in to complex autonomous
and electrified vehicles at Ford Motor Company. He is passionate about
using Python and open source in engineering, and he is a core contributor
to the BeeWare project. He’s on Twitter at @danyeaw.

# Title
CI/CD: Automate Your Python Development Workflow

# Duration
I prefer a 30 minute slot

# Description
Do you want the ability to easily automate the testing, packaging, and
deployment of your project on Windows, macOS, and Linux? Do you want to
spend more time on your projects focusing on implementing new features and
other enjoyable parts of programming, and less time doing manual and boring
project maintenance?

This talk gives an overview of CI/CD, a short history of CI/CD providers and
what features to look for, and walks you through how you can easily setup a
CI/CD pipeline for your Python library or application using GitHub Actions as
an example.

At the end of this talk, you should be able to set up a CI/CD pipeline
for your Python projects to test, package, and deploy your Python library or
application.

# Who and Why (Audience)

I am aiming this talk at individuals who want to get started with automating
parts of their Python workflow including CI/CD. Attendees will require basic
familiarity with Python programming and Git workflows, but don’t require any
experience with CI/CD. Experienced Python programmers and programmers
who have set up CI/CD pipeline, should still benefit from seeing how they can
translate their previous knowledge into being able to set up CI/CD on projects
in the future more quickly.

This talk will use the Briefcase packaging library, and a simple application as
examples to teach fundamental knowledge about CI/CD:

1. Patterns for pipelines for libraries and applications, including
similarities and differences.
   
2. Common libraries used in Python for CI/CD, like pre-commit, Black, and
pytest.

3. How to break up a pipeline in to steps, and how to translate those steps in
to a YAML formatted configuration.

In addition to the fundamental CI/CD knowledge, the audience will see some
examples of how open source workflow steps can be leveraged to build up a
working configuration faster and with higher quality. This is especially
important for CI/CD since it can take minutes to receive feedback from a change
to a configuration. This can result in slow and tedious debugging.

The audience will leave with the ability and tools to contribute CI/CD to any
major software project. I hope that a subset of the audience will be interested
in contributing improvements to open source projects by helping to automate
CI/CD for BeeWare and other projects at the PyCon Sprints, using the knowledge
in this presentation.

# Outline
1. Intro (5 min total)
    a. Who am I? (1 min)
    d. Overview of CI/CD (2 min)
    c. CI/CD benefits for your Python project (1 min)
    c. What to look for in a CI/CD service (1 min)
    d. Quick history and comparison of CI/CD providers (1 min)
2. CI/CD for a Python Library (13 min total)
    a. Overview of steps for a library (1 min)
    b. Making use of Python CI/CD templates (1 min)
    c. Library Workflow (1 min)
    d. Lint job (3 min)
    e. Test job (3 min)
    f. Upload to PyPI (2 min)
    g. Caching dependencies (2 min)
3. CI/CD for a Python App (3 min total)
    a. App Workflow (1 min)
    b. Test job (1 min)
    c. Release job (1 min)
9. Wrap-up (4 min total)
    a. Recorded demo of setting up CI/CD for a library (3 min)
    b. My contact information, and ask for questions (1 min)

Total time: 25 minutes with 5 minutes for questions

# Additional Notes 

I gave a similar presentation at the Michigan Python meetup in November 2019
and I received really great feedback about it. The talk ran to the approximate
timing a similar outline, and I am confident in the timing and the content. I
am also scheduled to discuss similar content as this talk on the [Test & Code
podcast](https://testandcode.com/) in January 2020.

Last year, I gave my first talk at PyCon on [5 Steps to Build Python Native GUI
Widgets for BeeWare](https://www.youtube.com/watch?v=sWt_sEZUiY8). The talk was
well attended, and as of December 2019 it has about 2700 views, which is in the
top 1/3 of videos from PyCon 2019. I learned a lot during this experience, and
I am excited to make my talk this year even better.

I am also the organizer of the Michigan Python meetup, and I have given two
other talks on BeeWare at the Michigan Python User Group (MICHIPUG) and Eastern
Michigan Python Users Group (EMPUG), and another talk about packaging with
pyproject.toml and Poetry.

At work, I also started a technology users group that now has over 600
members, and I have taught multiple online and in-person classes with up
to 60 attendees each.

I have posted similar
[slides](https://dan.yeaw.me/slides/github-actions-automate-your-python-development-workflow/index.html#/)
and [blog
post](https://dan.yeaw.me/posts/github-actions-automate-your-python-development-workflow/)
for this talk. I will be de-emphasizing GitHub Actions and focusing more on
CI/CD in general, while using GitHub Actions as an example.

[Briefcase](https://github.com/beeware/briefcase) will be used for the
library example, is open source and part of the [BeeWare](https://beeware.org)
project.
