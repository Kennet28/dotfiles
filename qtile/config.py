from os import system
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
# from libqtile.widget.net import Net
from settings.theme import colors
# from settings.groups import groups

mod = "mod4"
terminal = guess_terminal()

keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "j", lazy.layout.up(),
        desc="Move focus up in stack pane"),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, "control"], "j", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate(),
        desc="Swap panes of split stack"),

    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
    # Rofi
    Key([mod], "m", lazy.spawn("rofi -show run")),
    Key([mod, 'shift'], "m", lazy.spawn("rofi -show")),
    # Volume
    Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
    Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),
    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]
groups = [Group(i) for i in ["  ", "  ", "  ", "", "甆"]]

for i, group in enumerate(groups):
    actual_key = str(i+1)
    keys.extend([
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])
# Workspaces

# groups = [Group(i) for i in "asdfuiop"]

# for i in groups:
#     keys.extend([
#         Key([mod], i.name, lazy.group[i.name].toscreen(),
#             desc="Switch to group {}".format(i.name)),

#         Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
#             desc="Switch to & move focused window to group {}".format(i.name)),
#     ])

layouts = [
    layout.MonadTall()
]

widget_defaults = dict(
    font='UbuntuMono Nerd Font Bold',
    fontsize=14,
    padding=1,
)
extension_defaults = widget_defaults.copy()


#


def base(fg='text', bg='dark'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="",  # Icon: nf-oct-triangle_left
        fontsize=37,
        padding=-2
    )


# Screens
screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.GroupBox(
                    **base(fg='light'),
                    font='UbuntuMono Nerd Font',
                    fontsize=19,
                    margin_y=3,
                    margin_x=0,
                    padding_y=8,
                    padding_x=5,
                    borderwidth=1,
                    active=colors['active'],
                    inactive=colors['inactive'],
                    rounded=False,
                    highlight_method='block',
                    urgent_alert_method='block',
                    urgent_border=colors['urgent'],
                    this_current_screen_border=colors['focus'],
                    this_screen_border=colors['grey'],
                    other_current_screen_border=colors['dark'],
                    other_screen_border=colors['dark'],
                    disable_drag=True
                ),

                
                # widget.Prompt(),
                # widget.Chord(
                #     chords_colors={
                #         'launch': ("#ff0000", "#ffffff"),
                #     },
                #     name_transform=lambda name: name.upper(),
                # ),
                separator(),
                widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
                separator(),

                powerline('color4', 'dark'),

                icon(bg="color4", text=' '),  # Icon: nf-fa-download

                widget.CheckUpdates(
                    background=colors['color4'],
                    colour_have_updates=colors['text'],
                    colour_no_updates=colors['text'],
                    no_update_string='0',
                    display_format='{updates}',
                    update_interval=1800,
                    custom_command='checkupdates',
                ),
                powerline('color3', 'color4'),
                icon(bg="color3", text=' '),  # Icon: nf-fa-feed
                widget.Net(**base(bg='color3'), interface='wlp2s0'),
                powerline('color1', 'color3'),
                widget.CPU(**base(bg='color1'), padding=5),
                widget.ThermalSensor(**base(bg='color1'), padding=5),
                powerline('color2', 'color1'),
                icon(bg="color2", text=' '),  # Icon: nf-fa-feed
                widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),
                powerline('dark', 'color2'),
                # widget.Systray(background=colors['dark'], padding=5),
                widget.CapsNumLockIndicator(),
                widget.BatteryIcon(**base(bg='dark')), #Baterry Icon
            ],
            24,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# Name
wmname = "LG3D"
# Autostart config
autoStart = [
    "setxkbmap -layout latam",
    "feh --bg-fill ~/.config/qtile/wallpapers/01.png"
]

for command in autoStart:
    system(command)
