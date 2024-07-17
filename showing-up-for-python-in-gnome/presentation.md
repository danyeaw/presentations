% Showing Up for Python in GNOME
% Dan Yeaw (`dan@yeaw.me`)
% July 20, 2024

## About Me

- Dan Yeaw (pronounced: Yaw)
- Originally from California, now lives in Michigan
- Co-maintainer of Gaphor, SysML/UML Modeling tool (GNOME Circle)
- Co-maintainer of Gvsbuild for building GTK on Windows
- GNOME Foundation member, developer access this year
- Hosts Michigan Python monthly
- Works for Ford Motor Company on Functional Safety

::: notes

Hi, I'm Dan Yeaw, and I'm sooo excited to talk to you about Showing up for Python in GNOME!!

:::

## Python is a Mosiac

Mosiac here.

## GNOME Python

- PyGObject is the GTK and related library bindings for Python
- Successor to PyGTK that James Henstridge started in 1998

## On Python

"The current state of the Python bindings for GObject-based libraries is making it really hard to recommend using Python as a language for developing GTK and GNOME applications." Emmanuele Bassi (2022)

::: notes

In December 2022, Emmanuele Bassi wrote a blog post called On Python with a call to action to get involved to help Christoph.

:::

## Commits Over Time

 ![PyGObject Commits Over Time](commits-over-time.png)

- Major contributors like Simon Feltman, John Palmieri, and Martin Pitt left the project.
- Christoph Reiter heroically held things together since 2017.
- However, the number of changes started to fall off, especially after 2020.

## Getting Involved in an Undermaintained Project

- Contributing to an undermaintained project can be difficult
- Each extra contribution is placing a burden on the developer
- Timely feedback to contributions is often not possible
- To outsiders GNOME as a project can sometimes feel hard to join, especially in these undermaintained areas

## Community Building

![](handbook.svg){width=80%}

- The GNOME Project Handbook greatly improves clarity on how to get involved
- The GNOME Foundation could also take a greater role

::: notes
Wow! The GNOME Project Handbook which was released at the end of January. is such a special resource to document for everyone how to get involved and the expectations. A big shout out to the team whole helped make that happen!

Since GNOME as a project is made up of volunteers and individuals paid by companies with their own priorities, it can often be difficult to shift resources to help out a part of the ecosystem. Emmanuele shouldn't have to write blog posts asking for people to help get involved. There may be an opportunity for the GNOME Foundation here to track the health of key GNOME projects using metrics and then provide community building support for those that are starting to have challenges to help them out before it becomes an issue.
:::

# The State of Python in GNOME

## Issue and Merge Request Triage

- Closed about 200 issues
- Total issue count went from over 300 to 175
- Open or draft merge requests went from 30 to 19

::: notes
A clean issue backlog is important for a thriving community. We made some major in roads over the last year to reduce the total open issue and merge request counts.
:::

## https://pygobject.gnome.org

Screenshot here!

::: notes
We use to have the pygobject docs hosted on read the docs. Rafael Mardojai also had a really nice PyGObject-Guide which was a tutorial based on the Python GTK+3 Tutorial by Sebastian Pölsterl. We worked with the communities to convert the projects from the GNU Free Documentation License to the LGPL, merged the tutorials with the other docs, and moved them to a more official pygobject.gnome.org subdomain.
:::

## Fundamental Types

```python
def on_pressed(ctrl, n_press, x, y):
    print(ctrl.get_current_event())


def window():
    ctrl = Gtk.GestureClick()
    ctrl.connect("pressed", on_pressed)
    win = Gtk.Window.new()
    win.add_controller(ctrl)
    win.show()
    return win
```

::: notes
Now Python developers can finally use instances of fundamental types, which was one of the big blockers for people implementing custom widgets with GTK4. This original work was starting in 2010, and Arjan Molenaar brushed it off and implemented it this year.

This fixes a ton of low level issues. you’ll be able to do advanced custom drawing using render nodes, as well as accessing low level windowing system event objects, in your Python applications.
:::

## meson-python and PDM

```bash
meson setup _build
meson test -C _build
```

or

```bash
pdm install
pdm run pytest
```

::: notes
We moved from the legacy setup.py to the more modern pyproject.toml. We are using Meson for the build backend and using PDM to manage the project dependencies and virtualenvs.
:::

## Modernize API Docs

- Modernize building docs using GI-DocGen and Sphinx

### Template

`class Template(**kwargs)`

### Methods

```
	classmethod from_file(filename)
        Parameters: filename

    classmethod from_resource(resource_path)
        Parameters: resource_path

```

::: notes
Just like many other libraries have been upgrading from GTK-Doc to GI-DocGen, PyGObject also recently made the switch. GI-Docgen reuses the introspection data generated by GObject-based libraries to generate the API reference of these libraries.

Previously, we were using pgi-docgen, which was a more custom way
to read GIR docs and then create a Sphinx website from them.

Previously missing documentation, like for Gtk.Template is now available and because we are using the introspection data directly
less maintenance is required going forward.
:::

## Main Branch

- Small change to rename the primary branch to main
- Improves exclusivity and standardization with other GNOME projects

## Experimental: Asyncio Integration

- Implements Python asyncio await for Gio async results

```python
async def idle_test():
    bus = await Gio.bus_get(Gio.BusType.SYSTEM)
    # Actual bus call requires more paramters
    await bus.call("org.freedesktop.NetworkManager")

policy = GLibEventLoopPolicy()
asyncio.set_event_loop_policy(policy)
loop = policy.get_event_loop()
loop.run_until_complete(idle_test())
```

<!---
After 2 years of work, Benjamin Berg finished an initial implementation of Asyncio integration with PyGObject which was merged this week! This approach uses the GMainLoop to drive the EventLoop, as opposed to other approaches like GBulb and aysncio-glib which implement a full EventLoop or have the EventLoop drive the GMainContext.
-->


# The Future

## Wheels for Windows

- Python 3.8+ no longer loads DLLs on the path
- Building GTK using MSVC with `pip install pygobject` doesn't work for getting started
- Solution: build wheels of PyGObject with the DLLs included

::: notes
For security reasons, Python 3.8 stopped automatically loading DLLs on the path on Windows. Many libraries including PyGObject previously depended on this behavior. If you do build GTK on Windows using Gvsbuild or with MSVC directly, you don't end up with a working PyGObject without manually loading the DLLs or patching PyGObject.

We have discussed options to fix this, and there hasn't been much excitement in adding a DLL search routine in PyGObjects startup code. However, a Wheel format allows for DLLs to be bundled along side of the project though and then they are automatically loaded. This would also significantly improve install time as well, since users can directly install a pre-compiled version of PyGObject instead of compiling it during the installation.
:::

## Port to `libgirepository-2.0`

- `libgirepository` is now part of GLib
- The main enhancement is it now uses `GObject.TypeInstance` instead of C struct aliasing
- Utility programs are also renamed:

| girepository-1.0 | girepository-2.0      |
|------------------|-----------------------|
| g-ir-compiler    | gi-compile-repository |
| g-ir-generate    | gi-decompile-typelib  |
| g-ir-inspect     | gi-inspect-typelib    |

::: notes
This one is more of a chore to make sure that PyGObject is using the latest libraries. libgirepository was originally part of
gobject-introspection, however it is now very stable and has been integrated with GLib to improve the build process to prevent circular dependencies between GLib and gobject-introspection.

The main change between the two versions of libgirepository is that it now uses GObject.TypeInstance as the basis of its type system, rather than simple C struct aliasing. 

The symbol prefix was also updated from `g_` to `gi_`, various function arguments changed, and there were some modification to stack allocation.

Philip Withnall started this work to port PyGObject, and Arjan Molenaar has picked it up to try to bring it home.
:::

## Move API Docs

- Combine and merge the API docs to https://pygobject.gnome.org
- Would finish centralizing all docs

## Call to Action

- Contributions of any kind will help continue to help the community thrive
- Submit and help triage issues
- Continue to help us improve the docs
- Help us fix bugs and implement features
- Add examples to Workbench
- Build projects with PyGObject

::: notes
Many of you have even more ideas on what we could improve next, and we would love to have your contributions!

:::