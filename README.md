Alva Sorcerer is a heavyweight Blender addon consisting currently of about 20,000 lines and several hundred custom UI elements. It extends Blender's functionality far beyond computer graphics into the realm of theatrical show control for live performance venues. Sorcerer leverages the power of Blender to provide technical theatre designers to think and work in completely new ways. This allows creation of truly exotic theatrical experiences. In the realm of professional 3D animation, it is not uncommon for an animator to spend weeks or even months creating and perfecting just 10 seconds of an animation. This speaks volumes to the level of precision that Blender provides. Sorcerer connects theatrical designers to the same precision. 

Contrary to most similar softwares, Sorcerer does not directly control any stage hardware. Instead, Sorcerer remote-controls existing consoles/mixers through OSC during design time and transfers deliverables to the consoles for local execution during final performances. For this reason, Sorcerer is considered an External Multi-discplinary Animation Renderer. 

Currently, most Sorcerer features are for light design, although there is support for 3D audio rendering as well. Much of the Sequencer component of Sorcerer is only compatible with ETC Eos lighting consoles. The other aspects of Sorcerer are expected to be compatible with universal lighting consoles.

**Core Feature Sets of Sorcerer:**

• “Orb” assistant that rapidly automates many repetitive tasks on Eos 
• Most static menu panels can be hidden and accessed instead as popups 
• Rapidly create flash effects with the sequencer and link to nodes 
• Animate 3D objects over the lighting plot in 3D view for 3D-object-based effects (influencers)
• Directly link pan/tilt of movers to 3D audio objects and create deliverables (sonic light beam)
• Create “qmeo” deliverables after animating complex effects 
• Sequencer automatically creates events in the Eos event list based on strips 
• Use your own Python code to control lights or 3D audio objects 
• “School mode” password-protects key settings that students/volunteers shouldn’t touch

**Relevant Blender Feature Sets:**

• Advanced animation tools like Graph Editor, NLA Editor, and Dope Sheet 
• Blender’s .blend file management 
• Blender’s highly customizable UI themes and keymap 
• Performance capture for moving lights using motion tracking 
• Many other tools within Blender that have been under continuous, iterative evolution for 3 decades

**BORING DEV NOTES:**
3/28/2024 — I'm experimenting with the new 4.1 stable build. I'm finding that that the new "Cancel" UI element they added to popup menus does indeed affect ALL popup menus including addon ones (see release video if you haven't already). Will need to expidite adding cancel logic to all those modals now. The button does not appear to be causing runtime errors, fortunately.
