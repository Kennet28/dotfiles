from os import system
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from settings.theme import colors
from settings.utils import base, separator, icon, powerline
from settings.keys import keys,mod
from settings.screens import screens
from settings.widgets import widget_defaults,extension_defaults
from settings.workspaces import groups


terminal = guess_terminal()

#layouts
layouts = [
    layout.MonadTall()
]



# Drag floating layouts.
#TODO: I NEED THINK ABOUT THIS
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
