**This is an External Multi-disciplinary Animation Renderer (EMAR)**
======================================================================

Alva Sorcerer is a heavyweight Blender addon consisting currently of about 20,000 lines and several hundred custom UI elements. It extends Blender's functionality far beyond computer graphics into the realm of theatrical show control for live performance venues. Sorcerer leverages the power of Blender to provide technical theatre designers the ability to think and work in completely new ways. This allows creation of truly exotic theatrical experiences. In the realm of professional 3D animation, it is not uncommon for an animator to spend weeks or even months creating and perfecting just 10 seconds of an animation. This speaks volumes to the level of precision that Blender provides. Sorcerer connects theatrical designers to the same precision. 

Contrary to most similar softwares, Sorcerer does not directly control any stage hardware. Instead, Sorcerer remote-controls existing consoles/mixers through OSC during design time and transfers deliverables to the consoles for local execution during final performances. For this reason, Sorcerer is considered an External Multi-discplinary Animation Renderer. 

Currently, most Sorcerer features are for light design, although there is support for 3D audio rendering as well. Much of the Sequencer component of Sorcerer is only compatible with ETC Eos lighting consoles. The other aspects of Sorcerer are expected to be compatible with universal lighting consoles.


---------------------------------------
**Core Feature Sets of Sorcerer:**
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
- It does not output multichannel audio, it instead produces separate audio files for each speaker and also remote controls mixers for realtime monitoring
- It is not meant to be running during final shows, it instead is meant to be used to create deliverables that the console/mixer or Qlab will perform later


---------------------------------------
**Relevant Blender Feature Sets:**
---------------------------------------

- Advanced animation tools like Graph Editor, NLA Editor, Dope Sheet, arrays, and constraints 
- Blender’s .blend file management 
- Blender’s highly customizable UI and keymap 
- Asset manager for organizing and sharing file components
- Many other tools within Blender that have been under continuous, iterative evolution for 3 decades


------------------------
**Boring Dev Notes:**
------------------------
3/28/2024 — I'm experimenting with the new 4.1 stable build. I'm finding that that the new "Cancel" UI element they added to popup menus does indeed affect ALL popup menus including addon ones (see release video if you haven't already). Will need to expedite adding cancel logic to all those modals now. The button does not appear to be causing runtime errors, fortunately.
