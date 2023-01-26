import os
from libqtile import bar, layout, widget
from libqtile.config import Match


def env(name, default):
    """
    This function gets the name of the current window
    """
    return os.environ.get(name, default)


def lays(colors):
    """
    This function configures the layouts for qtile
    """
    border_focus = env("BORDER_FOCUS", colors["light-purple"])
    border_normal = env("BORDER_NORMAL", "#220000")
    border_width = int(env("BORDER_WIDTH", 0))
    margin = int(env("MARGIN", 4))
    margin_on_single = int(env("MARGIN_ON_SINGLE", 0))
    num_stacks = int(env("NUM_STACKS", 2))
    return [
        layout.Columns(
            border_focus=border_focus,
            border_normal=border_normal,
            border_width=border_width,
            margin=margin,
            margin_on_single=margin_on_single,
        ),
        layout.Max(
            border_focus=border_focus,
            border_normal=border_normal,
            border_width=border_width,
            margin=margin,
            margin_on_single=margin_on_single,
        ),
        layout.Stack(
            border_focus=border_focus,
            border_normal=border_normal,
            border_width=border_width,
            margin=margin,
            margin_on_single=margin_on_single,
            num_stacks=num_stacks,
        ),
        layout.Bsp(
            border_focus=border_focus,
            border_normal=border_normal,
            border_width=border_width,
            margin=margin,
            margin_on_single=margin_on_single,
        ),
        layout.Matrix(
            border_focus=border_focus,
            border_normal=border_normal,
            border_width=border_width,
            margin=margin,
            margin_on_single=margin_on_single,
        ),
        layout.MonadTall(
            border_focus=border_focus,
            border_normal=border_normal,
            border_width=border_width,
            margin=margin,
            margin_on_single=margin_on_single,
        ),
        layout.MonadWide(
            border_focus=border_focus,
            border_normal=border_normal,
            border_width=border_width,
            margin=margin,
            margin_on_single=margin_on_single,
        ),
        layout.RatioTile(
            border_focus=border_focus,
            border_normal=border_normal,
            border_width=border_width,
            margin=margin,
            margin_on_single=margin_on_single,
        ),
        layout.Tile(
            border_focus=border_focus,
            border_normal=border_normal,
            border_width=border_width,
            margin=margin,
            margin_on_single=margin_on_single,
        ),
        layout.TreeTab(
            border_focus=border_focus,
            border_normal=border_normal,
            border_width=border_width,
            margin=margin,
            margin_on_single=margin_on_single,
            active_bg=active_bg,
        ),
        layout.VerticalTile(
            border_focus=border_focus,
            border_normal=border_normal,
            border_width=border_width,
            margin=margin,
            margin_on_single=margin_on_single,
        ),
        layout.Zoomy(
            border_focus=border_focus,
            border_normal=border_normal,
            border_width=border_width,
            margin=margin,
            margin_on_single=margin_on_single,
        ),
    ]


def floating(colors):
    """
    This function configures the floating layout for qtile
    """
    border_focus = env("BORDER_FOCUS", colors["light-purple"])
    border_normal = env("BORDER_NORMAL", "#220000")
    border_width = int(env("BORDER_WIDTH", 0))

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
        ],
    )

    return floating_layout
