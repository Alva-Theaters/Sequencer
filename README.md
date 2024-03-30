**3D Animation in Real Life, For Theatre, With Blender**
======================================================================

Alva Sorcerer is a heavyweight Blender addon that uses OSC to remote-control ETC Eos family theatrical lighting consoles, Qlab, live sound mixers, and other professional lighting consoles. Blender is the free and open source 3D animation suite supporting modeling, rigging, animation, simulation, rendering, compositing, motion tracking and video editing. Alva Sorcerer connects that power to FOH show control to create 3D animations in real life in theatre.


**What Sorcerer Does Do:**
---------------------------------------

- Node-based light design
- Sequence-based light design
- Animation-based light design
- 3D-object-based light-design (dynamic spatial selections)
- Motion capture for light design
- 3D audio panner integrated directly into stage lighting control
- Pop-up ML editor within 3D view
- Automation tools that rapidly produce deliverables


**What Sorcerer Does NOT Do:**
---------------------------------------

- It is not DMX software, it instead remote-controls professional consoles and produces deliverables
- It is not visualization software
- It does not output multichannel audio, it instead outputs separate tracks for each speaker to Qlab and commandeers sound mixer faders for realtime monitoring
- It is not meant to send OSC during final shows, it instead creates deliverables stored on FOH hardware for the final show(s)


**Relevant Blender Feature Sets:**
---------------------------------------

- Advanced animation tools like Graph Editor, NLA Editor, Dope Sheet, arrays, and constraints 
- Blender’s .blend file management 
- Blender’s highly customizable UI and keymap 
- Asset manager for organizing and sharing file components
- Many other tools within Blender that have been under continuous, iterative, open source evolution for 3 decades
- The Blender community


**Boring Dev Notes:**
------------------------
3/28/2024 — I'm experimenting with the new Blender 4.1 stable build. I'm finding that that the new "Cancel" UI element they added to popup menus does indeed affect ALL popup menus including addon ones (see release video if you haven't already). Will need to expedite adding cancel logic to all those modals now. The button does not appear to be causing runtime errors, fortunately.
