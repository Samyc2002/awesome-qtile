# IMPORTING MODULES
import os
import subprocess

from pygments import highlight
from libqtile import hook, extension
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen

# UTILITY FUNCTIONS
def env(name, default):
    return os.environ.get(name, default)

def parseWindowName(name):
    nameParts = name.split("-")
    # initial = nameParts[0]
    end = nameParts[-1]
    return end

# HOTKEYS AND HOT APPS
mod = "mod4"
terminal = guess_terminal()

# COLOURS
colors = {
    "foreground": "#D9E1EE",
    "background": "#282C34",
    "selection": "#3E4451",
    "red": "#FF6C6B",
    "blue": "#46D9FF",
    "magenta": "#A9A1E1",
    "yellow": "#ECBE7B",
    "green": "#4DB5BD",
    "light-purple": "#E6CCFF",
    "purple": "#8000FF",
    "violet": "#B366FF"
}

# GLOBAL VARIABLES
border_focus = env("BORDER_FOCUS", colors["light-purple"])
border_normal = env("BORDER_NORMAL", "#220000")
border_width = int(env("BORDER_WIDTH", 2))
margin = int(env("MARGIN", 10))
margin_on_single = int(env("MARGIN_ON_SINGLE", 0))
num_stacks = int(env("NUM_STACKS", 2))
active_bg= colors["purple"]
bg_color= colors["violet"]

# KEYBINDINGS
keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
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
    Key([mod], 'r', lazy.run_extension(extension.DmenuRun(
        dmenu_prompt="$_",
        dmenu_font="Poppins",
        dmenu_lines=15,
        dmenu_ignorecase=True,
        background=colors["background"],
        foreground=colors["foreground"],
        selected_background=colors["selection"],
        selected_foreground=colors["yellow"],
        dmenu_height=20,  # Only supported by some dmenu forks
    )), desc="Spawn a command using a prompt widget"),
    Key([mod], 'w', lazy.run_extension(extension.WindowList(
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
    )), desc="Spawn a command using a prompt widget"),
    Key([mod, "control"], 'q', lazy.run_extension(extension.CommandSet(
        commands={
            'Lock': 'xscreensaver-command -lock',
            'Shut Down': 'poweroff',
            'Restart': 'restart',
            'Log Out': 'loginctl terminate-user 1000',
            'Exit': '',
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
    )), desc="To provide options for restart, shutdown, logout or lock the screen"),
    # Custom daemon shortcuts
    Key([mod], "l", lazy.spawn("xscreensaver-command -lock"), desc="Lock the Screen"),
    Key([mod], "m", lazy.spawn("spotify"), desc="Launch Spotify"),
    Key([mod, "shift"], "e", lazy.spawn("emacsclient -c -a 'emacs'"), desc="Launch doom emacs"),
    # Custom app shortcuts
    Key([mod], "e", lazy.spawn("pcmanfm"), desc="File Explorer")
]

#WORKSPACES
workspaces = [
    {
        "name": "1",
        "matches": None,
        "exclusive": False,
        "spawn": None,
        "layout": None,
        "layouts": None,
        "persist": True,
        "label": "" #Code
    },
    {
        "name": "2",
        "matches": None,
        "exclusive": False,
        "spawn": None,
        "layout": None,
        "layouts": None,
        "persist": True,
        "label": "" #Browser
    },
    {
        "name": "3",
        "matches": None,
        "exclusive": False,
        "spawn": None,
        "layout": None,
        "layouts": None,
        "persist": True,
        "label": "" #Testing
    },
    {
        "name": "4",
        "matches": None,
        "exclusive": False,
        "spawn": ["Alacritty"],
        "layout": None,
        "layouts": None,
        "persist": True,
        "label": "" #Terminal
    },
    {
        "name": "5",
        "matches": None,
        "exclusive": False,
        "spawn": None,
        "layout": None,
        "layouts": None,
        "persist": True,
        "label": "" #Documentations
    },
    {
        "name": "6",
        "matches": None,
        "exclusive": False,
        "spawn": None,
        "layout": None,
        "layouts": None,
        "persist": True,
        "label": "" #Meetings
    },
    {
        "name": "7",
        "matches": None,
        "exclusive": False,
        "spawn": None,
        "layout": None,
        "layouts": None,
        "persist": True,
        "label": "" #Social
    },
    {
        "name": "8",
        "matches": None,
        "exclusive": False,
        "spawn": None,
        "layout": None,
        "layouts": None,
        "persist": True,
        "label": "" #Media
    },
    {
        "name": "9",
        "matches": None,
        "exclusive": False,
        "spawn": None,
        "layout": None,
        "layouts": None,
        "persist": True,
        "label": "" #Miscellaneous
    }
]

groups = [Group(i["name"], matches=i["matches"], exclusive=i["exclusive"], spawn=i["spawn"], layout=i["layout"], layouts=i["layouts"], persist=i["persist"], label=i["label"]) for i in workspaces]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

#LAYOUTS
layouts = [
    layout.Columns(
        border_focus=border_focus,
        border_normal=border_normal,
        border_width=border_width,
        margin=margin,
        margin_on_single=margin_on_single
    ),
    layout.Max(
        border_focus=border_focus,
        border_normal=border_normal,
        border_width=border_width,
        margin=margin,
        margin_on_single=margin_on_single
    ),
    layout.Stack(
        border_focus=border_focus, border_normal=border_normal,
        border_width=border_width,
        margin=margin,
        margin_on_single=margin_on_single,
        num_stacks=num_stacks
    ),
    layout.Bsp(
        border_focus=border_focus,
        border_normal=border_normal,
        border_width=border_width,
        margin=margin,
        margin_on_single=margin_on_single
    ),
    layout.Matrix(
        border_focus=border_focus,
        border_normal=border_normal,
        border_width=border_width,
        margin=margin,
        margin_on_single=margin_on_single
    ),
    layout.MonadTall(
        border_focus=border_focus,
        border_normal=border_normal,
        border_width=border_width,
        margin=margin,
        margin_on_single=margin_on_single
    ),
    layout.MonadWide(
        border_focus=border_focus,
        border_normal=border_normal,
        border_width=border_width,
        margin=margin,
        margin_on_single=margin_on_single
    ),
    layout.RatioTile(
        border_focus=border_focus,
        border_normal=border_normal,
        border_width=border_width,
        margin=margin,
        margin_on_single=margin_on_single
    ),
    layout.Tile(
        border_focus=border_focus,
        border_normal=border_normal,
        border_width=border_width,
        margin=margin,
        margin_on_single=margin_on_single
    ),
    layout.TreeTab(
        border_focus=border_focus,
        border_normal=border_normal,
        border_width=border_width,
        margin=margin,
        margin_on_single=margin_on_single,
        active_bg=active_bg
    ),
    layout.VerticalTile(
        border_focus=border_focus,
        border_normal=border_normal,
        border_width=border_width,
        margin=margin,
        margin_on_single=margin_on_single
    ),
    layout.Zoomy(
        border_focus=border_focus,
        border_normal=border_normal,
        border_width=border_width,
        margin=margin,
        margin_on_single=margin_on_single
    ),
]

# WIDGET CONFIGURATIONS
widget_defaults = dict(
    font="Poppins",
    fontsize=13,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth=0,
                    padding=10
                ),
                widget.Image(filename="~/.config/qtile/Logo_Light.png", margin=7),
                widget.Sep(
                    linewidth=0,
                    padding=6
                ),
                widget.GroupBox(
                    fontsize=23,
                    highlight_method="block",
                    foreground=colors["yellow"],
                    this_current_screen_border=colors["selection"],
                    padding_x=4,
                    padding_y=0,
                    active=colors["yellow"],
                    inactive=colors["light-purple"]
                ),
                widget.Sep(
                    linewidth=0,
                    padding=6
                ),
                widget.CurrentLayoutIcon(scale=0.5),
                widget.Prompt(),
                widget.WindowName(
                    empty_group_string="Hey, Samy! What are yah up to ?",
                    parse_text=parseWindowName
                ),
                # widget.Chord(
                #     chords_colors={
                #         "launch": ("#ff0000", "#ffffff"),
                #     },
                #     name_transform=lambda name: name.upper(),
                # ),
                # widget.TextBox("default config", name="default"),
                # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # widget.BatteryIcon(scale=3),
                # widget.Moc(),
                widget.OpenWeather(location="Kolkata", format="{icon}", fontsize=23),
                widget.OpenWeather(location="Kolkata", format=" {weather_details} {temp}°{units_temperature}", fontsize=13),
                widget.Sep(
                    linewidth=0,
                    padding=6
                ),
                widget.TextBox("&#xf274;", fontsize=23),
                widget.Clock(
                    format="%A %wth %B  %I:%M %p"
                ),
                widget.Sep(
                    linewidth=0,
                    padding=6
                ),
                widget.Systray(),
                # widget.QuickExit(),
                widget.Sep(
                    linewidth=0,
                    padding=10
                ),
            ],
            35,
            background=colors["background"],
            # border_width=[0, 10, 0, 10],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# DRAG FLOATING LAYOUT WINDOWS
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# STARTUP APPLICATIONS
@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser('~/.config/qtile/autostart.sh') # STARTUP SCRIPT
    subprocess.run([script])
    picom = os.path.expanduser('~/.config/picom/picom.sample.conf') # STARTUP SCRIPT
    subprocess.run([picom])

# MAKE DIALOGS FLOAT AUTOMATICALLY
@hook.subscribe.client_new
def floating_dialogs(window):
    dialog = window.window.get_wm_type() == 'dialog'
    transient = window.window.get_wm_transient_for()
    if dialog or transient:
        window.floating = True

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=border_focus,
    border_normal=border_normal, 
    border_width=border_width,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
