from libqtile.config import Key
from libqtile.command import lazy

mod = "mod4"

keys = [Key(key[0],key[1],*key[2:]) for key in [
    # Switch between windows in current stack pane
    ([mod], "k", lazy.layout.down()),
    ([mod], "j", lazy.layout.up()),

    # Move windows up or down in current stack
    ([mod, "control"], "k", lazy.layout.shuffle_down()),
    ([mod, "control"], "j", lazy.layout.shuffle_up()),

    # Switch window focus to other pane(s) of stack
    ([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    ([mod, "shift"], "space", lazy.layout.rotate()),

    ([mod, "shift"], "Return", lazy.layout.toggle_split()),
    ([mod], "Return", lazy.spawn("alacritty")),

    # Toggle between different layouts as defined below
    ([mod], "Tab", lazy.next_layout()),
    ([mod], "w", lazy.window.kill()),

    ([mod, "control"], "r", lazy.restart()),
    ([mod, "control"], "q", lazy.shutdown(),),
    ([mod], "r", lazy.spawncmd()),
    #rofi
    ([mod], "m", lazy.spawn("rofi -show run")),
    ([mod, 'shift'], "m", lazy.spawn("rofi -show")),
    # Volumen
    ([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    ([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
    ([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),  
    # Brillo
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),  
]]