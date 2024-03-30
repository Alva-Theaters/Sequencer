**3D Animation in Real Life, for Theatre, with Blender**
======================================================================

Alva Sorcerer is a heavyweight Blender addon that uses OSC to remote-control ETC Eos family theatrical lighting consoles, Qlab, live sound mixers, and other professional lighting consoles. Blender is the free and open source 3D animation suite supporting modeling, rigging, animation, simulation, rendering, compositing, motion tracking and video editing. Alva Sorcerer connects that power to FOH show control to create 3D animations in real life in theatre.

Alva Sequencer is the limited version of Sorcerer not behind a paywall.

**What Sorcerer IS:**
---------------------------------------

- Node-based light design (Sorcerer only)
- Sequence-based light design
- Animation-based light design
- Dynamic spatial selections (Sorcerer only)
- Motion capture for light design
- 3D audio panner integrated directly into stage lighting control
- Pop-up ML editor within 3D view (Sorcerer only)
- Automation tools that rapidly produce deliverables
- ADHD friendly


**What Sorcerer Does NOT Do:**
---------------------------------------

- It is not DMX software, it instead remote-controls professional consoles and produces deliverables
- It is not visualization software
- It does not output multichannel audio, it instead outputs separate tracks for each speaker to Qlab and commandeers sound mixer faders for realtime monitoring
- It is not meant to send OSC during final shows, it instead creates deliverables stored on FOH hardware for the final show(s)


**Use Cases:**
------------------

- Use a simple node layouts to provide students or volunteers the simplest conceivable way to control lights
- Output short, extremely sophisticated and precise lighting animations as deliverables to play as effects
- Animate moving lights to track 3D audio objects
- Use the video editor to make timecoding on Eos absurdly intuitive
- Use node layouts to build lighting cues the way a painter would, not how a computer programmer would
- Create exotic lighting effects by animating 3D objects that influence the lights they move over


**Relevant Blender Feature Sets:**
---------------------------------------

- Advanced animation tools like Graph Editor, NLA Editor, Dope Sheet, arrays, and constraints 
- Blender’s .blend file management 
- Blender’s highly customizable UI and keymap 
- Asset manager for organizing and sharing file components
- Many other tools within Blender that have been under continuous, iterative, open source evolution for 3 decades
- The Blender community


**Compatibility:**
---------------------------------------

- Alva Sequencer was initially developed in Blender 2.79, but has since been adapted to Blender 4.0
- Alva Sorcerer was developed on Blender 4.0
- Basic Sorcerer/Sequencer functionality has been tested on Blender 4.1 and Blender 3.5 without any sign of problems, although 4.1 introduces a Cancel button on all popups, but this does not do anything yet for most Sorcerer/Sequencer popups
- Alva Sequencer was designed primarily for ETC Eos, but some features like animation and trigger strips should work on other consoles
- Excluding the patch feature, Alva Sorcerer-only features were designed with universal lighting console compatibility in mind, but it has not been tested on consoles other than Eos
- 3D audio file playback is compatible with any software capable of playing numerous tracks at once to numerous sound card outputs (Qlab, for example)
- 3D audio realtime monitoring should be compatible with most sound mixers that support OSC input


**Boring Dev Notes:**
------------------------
3/28/2024 — I'm experimenting with the new Blender 4.1 stable build. I'm finding that that the new "Cancel" UI element they added to popup menus does indeed affect ALL popup menus including addon ones (see release video if you haven't already). Will need to expedite adding cancel logic to all those modals now. The button does not appear to be causing runtime errors, fortunately.
