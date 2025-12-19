# Speaker Profile

## Name
Dan Yeaw

## Biography
Dan Yeaw is a Sr. Engineering Manager for Open Source Software at Anaconda,
where he leads a team focused on improving the conda CLI's performance,
reliability, and user experience. For the last eight years, he has contributed
to open source projects, including as a core developer for GNOME, BeeWare, and
Gaphor, while helping build Michigan's Python community. Dan brings a unique
background having previously worked on Functional Safety at Ford Motor Company
and as a Naval Officer.

# Title
Exit Code Zero: Designing Delightful CLIs

## Description
What about using certain CLIs puts a smile on your face and gets you telling all
your friends and colleagues about it?

The Unix philosophy emphasizes simplicity, modularity, and the idea that
programs should do one thing well and work together. However, CLI programs are
primarily used by humans. Programs that you actually enjoy using can achieve
both of these aims of composability and human-centeredness.

This talk explores what makes CLIs great: fast, trusted, and delightful. Through
real-world examples from modern tools like uv, cargo, ripgrep, and GitHub CLI,
plus lessons from modernizing conda, you'll learn the design patterns that
separate good CLIs from great ones.

Whether you're building package managers, creating developer tools, or just
curious why modern CLIs feel so much better, you'll leave with a practical
checklist of techniques to apply to any CLI tool you build.

## Notes
Although there have been recent talks at PyCon US about Design, for example,
Lynn Root’s PyCon US 2024 talk on The Design of Everyday APIs, there hasn’t been
recent talks about CLI design. Previously, Amjith Ramanujam gave a PyCon US 2017
talk on Awesome Command Line Tools which focused on autocomplete. However, there
have been large changes to the CLI tool ecosystem with tools like uv, Pixi,
Poetry, and PDM coming out over the last few years. This is a timely topic to
show why some of these tools can be such a joy to use.

Animations and code examples on the slides will use asciinema and static code
screenshots, there will be no live demonstrations. Slides will have a light
background with dark text. My previous talk experience includes:

- PyCon US 2019 talk - 5 Steps to Build Python Native GUI Widgets for BeeWare
- PyCon US 2025 Maintainer’s Summit - From Nights & Weekends to 9-to-5, Transitioning to Professional Open Source
Leadership
- GUADEC 2025 - The State of Python in GNOME: Progress and Future Directions
- GUADEC 2024 - Showing Up for Python in GNOME Current organizer of Michigan Python
- Given over 15 talks on a wide range of topics
- Linux App Summit 2021 - Make Your Application Multiplatform!

I have walked through the outline, and I’m confident in the timing and content.

All CLI tools I talk about are open source software including uv, conda, pip,
Cargo, ripgrep, gh CLI, and bat.

Although I’ll be giving a real-world example about how we have used these
techniques recently to make improvements to the conda CLI, the talk won’t be
focusing on just that tool.

This talk draws on the excellent open source [Command Line Interface
Guidelines](https://clig.dev) as well as my experience implementing CLIs with
conda and a build tool called Gvsbuild.

## Outline
1. Intro (2.5 min)
- What is your favorite CLI tool? (30 sec)
- Examples (30 sec)
  - uv install that finishes magically fast
  - cargo telling you how to fix your errors
  - ripgrep, bat, and other next gen CLIs
- Contrast examples (1 min)
  - Old: conda install with no color or status updates
  - Modern: pixi install with color, emoji, and feedback
- The thesis & framework (30 sec)
  - Unix philosophy - composable and do one thing well
  - CLIs are used by humans
  - We can achieve both
  - Framework - Fast, Trusted, Delightful
2. Fast (6.5 min)
- The Psychology of Speed (1 min)
  - Responsive is more important than fast
- Show progress for operations > 1 sec (3 min)
  - Bad Example - conda installing with no updates
  - Good Example - Cargo
    - Show’s what’s happening
    - Progress counter
    - Timing at the end for confidence
    - Each line appear as work is done so it feels alive
    - Implementation using Rich, `rich.progress.track`
- Perceived vs. Actional Performance (2.5 min)
  - uv Case Study
  - uv appears really fast, but doesn’t compile byte code
  - This is a UX decision, fast installs feel great
3. Trusted (7 min)
- Why trust matters (1 min)
  - CLIs modify your system
  - Mistakes can be costly
  - Users need confidence
- Show what’s happening in real-time (2 min)
  - Good example of streaming install information with uv
  - Real-time progress
  - No confirmation for routine operations
- Error messages as a conversation (2 min)
  - Catch errors and rewrite them as a conversation to a human
  - Wrong package version examples, one with pip showing a cryptic error, one with Cargo suggesting the latest version of the package
  - Clear cause and effect
  - Actionable suggestions (with exact commands)
- Dry run for safe exploration (1 min)
  - Good example of `git add –dry-run`
    - Safe to experiment
    - Learn without consequences
- Confirm when dangerous (1 min)
  - Moderately risky (show preview with brief delay)
  - Dangerous require explicit confirmation like `gh repo delete`, type entire repo name
  - Guardrails without being annoying
4. Delightful (5 min)
- Sensible defaults (1 min)
  - Make the default the right thing for most users, minimize configurations
  - Beginners should succeed immediately
- Helpful suggestions (1 min)
  - If the user does something wrong, try to suggest the right command
  - Heroku CLI suggests the right commands
- Color and emoji with intention (1 min)
  - Example of beautiful tables with color with `gh pr list`
  - Don’t overdo it
- Accessibility (1 min)
  - Visual: NO_COLOR, colorblind palettes
  - Screen readers: Text alternatives
  - Motion: Disable animations
  - `gh a11y` example
- Progressive disclosure (1 min)
  - Provide output that is clean, clear, and done
  - Verbose mode that helps debug issues
  - Consistent, clean output also matters for automation and AI agents
  - uv install example
5. Real-world example - modernizing conda (2 min)
- Constraints (30 sec)
  - 12 years of legacy behavior, 50M users
  - Can’t break backwards compatibility
  - Performance constraints (SAT solver takes time)
- Challenge 1: the silent solver (30 sec)
  - Show progress at key checkpoints
  - Estimate solve time
  - Make it feel faster
- Challenge 2: information overload and confirmations (30 sec)
  - Show progressive disclosure of what’s happening
  - Remove confirmations for normal operations, explicit overrides for dangerous ones
  - Add color
- Challenge 3: Guide to fixing problems (30 sec)
  - Provide command suggestions
  - Dependency conflicts show a way to resolve them
6. Wrap-up and Call to Action (1 min)
- Exit code zero isn't just about the program succeeding
- It's about the user succeeding, smiling while they do it
- Fast, Trusted, Delightful
- Go build a great CLI!
7. Q&A (5 min)

## Category
Development & Software Engineering

## Audience
Some experience

## Provide link to presentation slides
Not provided

## Have you given this presentation before?
No
