# IMPORTING MODULES
import os
import subprocess

from libqtile import hook
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import bar
from libqtile.config import Group, Key, Screen

from configs.keybinds import keybinds
from configs.workspaces import groups
from configs.layouts import lays
from configs.statusbar import statusbar
from configs.mousebinds import mousebinds

# HOTKEYS AND HOT APPS
MOD = "mod4"
terminal = guess_terminal()

# COLOURS
colors = {
    "foreground": "#D9E1EE",
    "background": "#33282C34",
    "selection": "#003E4451",
    "red": "#FF6C6B",
    "blue": "#46D9FF",
    "magenta": "#A9A1E1",
    "yellow": "#ECBE7B",
    "green": "#4DB5BD",
    "light-purple": "#E6CCFF",
    "purple": "#8000FF",
    "violet": "#B366FF",
}

ACTIVE_BG = colors["purple"]
BG_COLOR = colors["violet"]

# KEYBINDINGS
keys = keybinds(MOD, terminal, colors)

# WORKSPACES
# workspaces = workspaces()

groups = [
    Group(
        i["name"],
        matches=i["matches"],
        exclusive=i["exclusive"],
        spawn=i["spawn"],
        layout=i["layout"],
        layouts=i["layouts"],
        persist=i["persist"],
        label=i["label"],
    )
    for i in groups()
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [MOD],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [MOD, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
        ]
    )

# LAYOUTS
layouts = lays(colors)

# WIDGET CONFIGURATIONS
widget_defaults = dict(
    font="Poppins",
    fontsize=10,
    padding=2,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            statusbar(colors),
            30,
            background=colors["background"],
            # border_width=[0, 10, 0, 10],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# DRAG FLOATING LAYOUT WINDOWS
mouse = mousebinds(MOD)

# STARTUP APPLICATIONS
@hook.subscribe.startup_once
def autostart():
    """
    This function is responsible for autostarting apps on login
    """
    script = os.path.expanduser(
        "~/.config/qtile/configs/autostart.sh"
    )  # STARTUP SCRIPT
    subprocess.run([script])
    picom = os.path.expanduser("~/.config/picom/picom.sample.conf")  # PICOM CONFIG
    subprocess.run([picom])


# MAKE DIALOGS FLOAT AUTOMATICALLY
@hook.subscribe.client_new
def floating_dialogs(window):
    """
    This function makes the dialog boxes into floating layout
    """
    dialog = window.window.get_wm_type() == "dialog"
    transient = window.window.get_wm_transient_for()
    if dialog or transient:
        window.floating = True


# SOME DEFAULT SETTINGS FOR DAY TO DAY USES
DGROUP_KEY_BINDER = None
DGROUP_APP_RULES = []  # type: list
FOLLOW_MOUSE_FOCUS = True
BRING_FRONT_CLICK = False
CURSOR_WRAP = False
AUTO_FULLSCREEN = True
FOCUS_ON_WINDOW_ACTIVATION = "smart"
RECONFIGURE_SCREENS = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
AUTO_MINIMIZE = True

# When using the Wayland backend, this can be used to configure input devices.
WL_INPUT_RULES = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
WMNAME = "LG3D"
