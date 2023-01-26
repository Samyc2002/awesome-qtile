from libqtile import widget


def parse_window_name(name) -> str:
    """
    This Function parses the window names and shows only the open application name
    and not the entire window name
    """
    name_parts = name.split("-")
    # initial = nameParts[0]
    end = name_parts[-1]
    return end


def statusbar(colors):
    """
    This function configures the top bar for qtile
    """
    return [
        widget.Sep(linewidth=0, padding=10),
        widget.Image(filename="~/.config/qtile/configs/Logo_Light.png", margin=7),
        widget.Sep(linewidth=0, padding=6),
        widget.GroupBox(
            fontsize=13,
            highlight_method="block",
            foreground=colors["yellow"],
            this_current_screen_border=colors["selection"],
            padding_x=4,
            padding_y=0,
            active=colors["yellow"],
            inactive=colors["light-purple"],
        ),
        widget.Sep(linewidth=0, padding=6),
        widget.CurrentLayoutIcon(scale=0.5),
        widget.Prompt(),
        widget.WindowName(
            empty_group_string="Hey, Samy! What are yah up to ?",
            parse_text=parse_window_name,
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
        # widget.OpenWeather(location="Kolkata", format="{icon}", fontsize=23),
        # widget.OpenWeather(
        #     location="Kolkata",
        #     format=" {weather_details} {temp}°{units_temperature}",
        #     fontsize=13,
        # ),
        widget.Sep(linewidth=0, padding=6),
        widget.TextBox("&#xf274;", fontsize=13),
        widget.Clock(format="%A %wth %B  %I:%M %p"),
        widget.Sep(linewidth=0, padding=6),
        widget.Systray(),
        # widget.QuickExit(),
        widget.Sep(linewidth=0, padding=10),
    ]
