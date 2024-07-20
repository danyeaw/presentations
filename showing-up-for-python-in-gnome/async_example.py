from gi.repository import GLib, Gio

import asyncio
from gi.events import GLibEventLoopPolicy


async def idle_test():
    bus = await Gio.bus_get(Gio.BusType.SESSION)
    print(
        await bus.call(
            "org.freedesktop.DBus",
            "/org/freedesktop/DBus",
            "org.freedesktop.DBus",
            "ListNames",
            None,
            None,
            0,
            -1,
        )
    )


policy = GLibEventLoopPolicy()
asyncio.set_event_loop_policy(policy)
loop = policy.get_event_loop()

loop.run_until_complete(idle_test())
