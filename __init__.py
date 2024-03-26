# This file is part of Alva Sequencer.
# Copyright (C) 2024 Alva Theaters

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


'''
=====================================================================
                      DESIGNED BY ALVA THEATERS
                       FOR THE SOLE PURPOSE OF
                         MAKING PEOPLE HAPPY
=====================================================================
'''


## Double hashtag indicates notes for future development requiring some level of attention


import bpy
from .scene_props import register as scene_props_register, unregister as scene_props_unregister
from .sequencer_main import register as sequencer_main_register, unregister as sequencer_main_unregister
from .sequencer_operators import register as sequencer_operators_register, unregister as sequencer_operators_unregister
from .sequencer_ui import register as sequencer_ui_register, unregister as sequencer_ui_unregister
from .hotkeys_popups import register as hotkeys_popups_register, unregister as hotkeys_popups_unregister


bl_info = {
    "name": "Alva Sequencer",
    "author": "Alva Theaters",
    "location": "Sequencer",
    "version": (1, 1, 1),
    "blender": (4, 0, 2),
    "description": "Sequence-based editing for ETC Eos lighting consoles and others.",
    "warning": "For reliability, migrate all data to console prior to real show.",
    "doc_url": "https://alva-sorcerer.readthedocs.io/en/latest/index.html#",
    "tracker_url": "https://github.com/Alva-Theaters/Sequencer/tree/main",
    }


def register():
    try:
        scene_props_register()
    except Exception as e:
        print("Failed to register scene props:", e)
    
    try:
        sequencer_main_register()
    except Exception as e:
        print("Failed to register sequencer main:", e)
    
    try:
        sequencer_operators_register()
    except Exception as e:
        print("Failed to register sequencer operators:", e)
    
    try:
        sequencer_ui_register()
    except Exception as e:
        print("Failed to register sequencer UI:", e)
    
    try:
        hotkeys_popups_register()
    except Exception as e:
        print("Failed to register hotkeys and popups:", e)
        

def unregister():
    try:
        scene_props_unregister()
    except Exception as e:
        print("Failed to unregister scene props:", e)
    
    try:
        sequencer_main_unregister()
    except Exception as e:
        print("Failed to unregister sequencer main:", e)
    
    try:
        sequencer_operators_unregister()
    except Exception as e:
        print("Failed to unregister sequencer operators:", e)
    
    try:
        sequencer_ui_unregister()
    except Exception as e:
        print("Failed to unregister sequencer UI:", e)
    
    try:
        hotkeys_popups_unregister()
    except Exception as e:
        print("Failed to unregister hotkeys and popups:", e)
  

if __name__ == "__main__":
    register()
