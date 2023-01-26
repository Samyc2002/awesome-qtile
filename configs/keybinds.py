from libqtile import extension
from libqtile.lazy import lazy
from libqtile.config import Key


def keybinds(mod, terminal, colors):
    """
    This function configures the keybinds for qtile
    """
    return [
        # Switch between windows
        Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
        Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
        Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
        Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
        Key(
            [mod], "space", lazy.layout.next(), desc="Move window focus to other window"
        ),
        # Move windows between left/right columns or move up/down in current stack.
        # Moving out of range in Columns layout will create new column.
        Key(
            [mod, "shift"],
            "h",
            lazy.layout.shuffle_left(),
            desc="Move window to the left",
        ),
        Key(
            [mod, "shift"],
            "l",
            lazy.layout.shuffle_right(),
            desc="Move window to the right",
        ),
        Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
        Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
        # Grow windows. If current window is on the edge of screen and direction
        # will be to screen edge - window would shrink.
        Key(
            [mod, "control"],
            "h",
            lazy.layout.grow_left(),
            desc="Grow window to the left",
        ),
        Key(
            [mod, "control"],
            "l",
            lazy.layout.grow_right(),
            desc="Grow window to the right",
        ),
        Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
        Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
        Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
        # Toggle between split and unsplit sides of stack.
        # Split = all windows displayed
        # Unsplit = 1 window displayed, like Max layout, but still with
        # multiple stack panes
        Key(
            [mod, "shift"],
            "Return",
            lazy.layout.toggle_split(),
            desc="Toggle between split and unsplit sides of stack",
        ),
        Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
        # Toggle between different layouts as defined below
        Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
        Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
        Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
        # Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
        # Custom Extension Keybindnings
        Key(
            [mod],
            "r",
            lazy.run_extension(
                extension.DmenuRun(
                    dmenu_prompt="$_",
                    dmenu_font="Poppins",
                    dmenu_lines=15,
                    dmenu_ignorecase=True,
                    background=colors["background"],
                    foreground=colors["foreground"],
                    selected_background=colors["selection"],
                    selected_foreground=colors["yellow"],
                    dmenu_height=20,  # Only supported by some dmenu forks
                )
            ),
            desc="Spawn a command using a prompt widget",
        ),
        Key(
            [mod],
            "w",
            lazy.run_extension(
                extension.WindowList(
                    dmenu_prompt="$_",
                    dmenu_font="Poppins",
                    dmenu_lines=15,
                    dmenu_ignorecase=True,
                    background=colors["background"],
                    foreground=colors["foreground"],
                    selected_background=colors["selection"],
                    selected_foreground=colors["yellow"],
                    fontsize=15,
                    item_format="{group}    {window}",
                    dmenu_height=20,  # Only supported by some dmenu forks
                )
            ),
            desc="Spawn a command using a prompt widget",
        ),
        Key(
            [mod, "control"],
            "q",
            lazy.run_extension(
                extension.CommandSet(
                    commands={
                        "Lock": "xscreensaver-command -lock",
                        "Shut Down": "poweroff",
                        "Restart": "reboot",
                        "Log Out": "loginctl terminate-user 1000",
                        "Exit": "",
                    },
                    # pre_commands=[''],
                    dmenu_prompt="$_",
                    dmenu_font="Poppins",
                    dmenu_lines=15,
                    dmenu_ignorecase=True,
                    background=colors["background"],
                    foreground=colors["foreground"],
                    selected_background=colors["selection"],
                    selected_foreground=colors["yellow"],
                    fontsize=15,
                    item_format="{group}    {window}",
                    dmenu_height=20,  # Only supported by some dmenu forks
                )
            ),
            desc="To provide options for restart, shutdown, logout or lock the screen",
        ),
        # Custom daemon shortcuts
        Key(
            [mod], "l", lazy.spawn("xscreensaver-command -lock"), desc="Lock the Screen"
        ),
        Key([mod], "m", lazy.spawn("spotify"), desc="Launch Spotify"),
        Key(
            [mod, "shift"],
            "e",
            lazy.spawn("emacsclient -c -a 'emacs'"),
            desc="Launch doom emacs",
        ),
        # Custom app shortcuts
        Key([mod], "e", lazy.spawn("pcmanfm"), desc="File Explorer"),
    ]
