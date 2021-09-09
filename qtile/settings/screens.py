from os import system
from libqtile import bar, widget
from libqtile.config import Screen
from settings.theme import colors
from settings.utils import base, separator, icon, powerline
# Screens
screens = [
    Screen(
        top=bar.Bar(
            [
                # workspaces styles
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
                separator(),
                # Window name
                widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
                separator(),
                powerline('color4', 'dark'),
                icon(bg="color4", text=' '),  # Icon: nf-fa-download
                # updates
                widget.CheckUpdates(
                    background=colors['color4'],
                    colour_have_updates=colors['text'],
                    colour_no_updates=colors['text'],
                    no_update_string='0',
                    display_format='{updates}',
                    update_interval=1800,
                    custom_command='checkupdates',
                ),
                # Network
                powerline('color3', 'color4'),
                icon(bg="color3", text=' '),  # Icon: nf-fa-feed
                widget.Net(**base(bg='color3'), interface='wlp2s0'),
                powerline('color1', 'color3'),
                #CPU and temperature
                widget.CPU(**base(bg='color1'), padding=5),
                widget.ThermalSensor(**base(bg='color1'), padding=5),
                # calendar
                powerline('color2', 'color1'),
                icon(bg="color2", text=' '),  # Icon: nf-fa-feed
                widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),
                powerline('dark', 'color2'),
                # systray
                icon(fg='light', text='  '),
                widget.PulseVolume(**base(bg='dark', fg='light')),
                separator(),
                widget.CapsNumLockIndicator(**base(bg='dark', fg='light')),
                widget.BatteryIcon(**base(bg='dark')),  # Baterry Icon
            ],
        20,

        ),
    ),
]