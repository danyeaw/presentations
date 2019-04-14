# Speaker Profile

## Name
Dan Yeaw

## Biography
Dan Yeaw is an engineer who helps design safety in to complex autonomous
and electrified vehicles at Ford Motor Company. He is passionate about
using Python and open source in engineering and he is a core contributor
to the BeeWare project. He’s on twitter at @danyeaw.

# Title
5 Steps to Build Python Native GUI Widgets for BeeWare 

# Duration
I prefer a 30 minute slot

# Description
Have you ever wanted to write a GUI application in Python that you can
run on both your laptop and your phone? Have you been looking to
contribute to an open source project, but you don't know where to start?

BeeWare is a set of software libraries for cross-platform native app
development from a single Python codebase and tools to simplify app
deployment. The project aims to build, deploy, and run apps for Windows,
Linux, macOS, Android, iPhone, and the web. It is native because it is
actually using your platform's native GUI widgets, not a theme, icon
pack, or webpage wrapper.

This talk will teach you how Toga, the BeeWare GUI toolkit, is
architected and then show you how you can contribute to Toga by creating
your own GUI widget in five easy steps.

# Who and Why (Audience)

This talk is aimed at individuals who want to write native GUI
applications in Python, and would like to get involved contributing
to an open source project in that area. Attendees will require basic
familiarity with Python programming, but don’t require any GUI
programming experience. Experienced Python programmers and programmers
who have experience with GUI programming should still benefit from the
architectural aspects of the talk.

This talk will use this major open source software project to teach
fundamental knowledge that I learned the hard way: 

1. Documentation Driven Development, when you write code, start with
   documentation. Before doing anything else, read the documentation,
   and write your own for any changes you are making.
   
2. Tests Next (TDD), once the documentation and API are nailed down,
   next come tests.

3. Finally code.
   
In addition to the development process above, the audience will learn
about basic software architecture including fundamentals of abstraction
and the factory method pattern.

The audience will leave with the ability to contribute a GUI widget to
Toga, but also with tools to contribute to any major software project.
Also the talk will increase the audience's knowledge about abstracting
out pythonic APIs, in order to provide a great experience to a user of a
library. I hope that a subset of the audience will be interested in
contributing to Toga or other open source projects at the Pycon sprints
using the knowledge in this presentation.

# Outline
1. Intro (5 min)
    a. Who am I?
    b. Describe what BeeWare is
    c. Hello World in Toga
    d. Current Status of the project
    e. Explain Toga Widgets, examples will be a Canvas (drawing) widget
2. Toga software architecture (visually) (4 min)
3. The 5 steps (OK, really 6)
    a. Step 0: development platform selection (1 min)
    b. Step 1: research your widget (2 min)
    c. Step 2: interface layer (pythonic API) (3 min)
    d. Step 3: Implement the core portion with TDD (3 min)
    e. Step 4: Implement the dummy implementation layer (2 min)
    f. Step 5: Implement the implementation layer on your platform (2 min)
9. Wrap-up (3 min)
    a. Summary of the 5 Steps, and create a Pull Request!
    b. My contact information, and ask for questions

Total time: 25 minutes with 5 minutes for questions

# Additional Notes 

I gave this presentation at the Michigan Python meetup in October 2018
and I received really great feedback about it. The talk ran to the
approximate timing in the outline, and I am confident in the timing and
the content.

I have also given two other talks on BeeWare at the Michigan Python User
Group (MICHIPUG) and Eastern Michigan Python Users Group (EMPUG), and
another talk about packaging with pyproject.toml and Poetry.

At work, I also started a technology users group that now has over 600
members and I have taught multiple online and in-person classes. This
would be my first time speaking at a major conference, but I am a
confident and charismatic public speaker.

The slides for this talk are posted here:
https://dan.yeaw.me/slides/gui-widget-for-beeware/index.html#/

The blog post is posted here:
https://dan.yeaw.me/blog/gui-widget-for-beeware/

BeeWare and Toga are open source software: https://pybee.org
