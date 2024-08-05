# Maya-Actions

This plugin enables a user to record, store and replay any set of actions on Maya, similarly to Adobe Photoshop's "Actions" functionallity.

## Usage
Once installed and loaded, a new shelf called "Actions" will appear with 2 buttons:
"Record" and "Stop". All saved actions will appear in this shelf (but can be moved with Maya's Shelf Editor).

The usage is simple:

1. Press the "Record" button to start recording.
2. Perform any actions you wish.
3. Once done, press the "Stop" button. A prompt will appear where you can choose the label for a new button.
4. To replay, press the new button with your label.

NOTE: Selection is an action itslef - to change an object make sure you selected it before recording!

## Features

* Record any set of actions you can do in Maya.
* Store recordings as a new button in Actions shelf.
* Discarding failed recordings (by pressing "Stop" and then "Discard" in prompt).
* Undo/Redo while recording is supported (undo-ed commands will not be executed in the recording).
