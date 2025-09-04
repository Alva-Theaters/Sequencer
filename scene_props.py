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

# pyright: reportInvalidTypeForm=false


import bpy
from bpy.props import *


def school_mode_password_updater(self, context):
    if self.school_mode_password.lower() in ["password123", "password 123"]:
        self.school_mode_enabled = not self.school_mode_enabled
        self.school_mode_password = ""
    
    
class SceneProperties(bpy.types.PropertyGroup):
    str_osc_ip_address: StringProperty(default="192.168.1.1", description="This should be the IP address of the console. This must set for anything to work. Press the About key on the console to find the console's IP address. Console must be on same local network")
    int_osc_port: IntProperty(min=0, max=65535, description="On the console, Displays > Setup > System Settings > Show Control > OSC > (enable OSC RX and make the port number there on the left match the one in this field in Alva. OSC TX = transmit and OSC RX = receive. We want receive", default=8000)

    school_mode_password: StringProperty(default="", description="Reduces potential for students or volunteers to break things", update=school_mode_password_updater)
    school_mode_enabled: BoolProperty(default=False, description="Reduces potential for students or volunteers to break things")


def register():
    bpy.utils.register_class(SceneProperties)
    bpy.types.Scene.scene_props = PointerProperty(type=SceneProperties)
    
    
def unregister():
    del bpy.types.Scene.scene_props
    bpy.utils.unregister_class(SceneProperties)
    

# For development purposes only.
if __name__ == "__main__":
    register()
