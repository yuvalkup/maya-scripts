import maya.OpenMaya as om
import maya.OpenMayaMPx as ommpx

import shelf
import prompt


class RecordCommand(ommpx.MPxCommand):
    def __init__(self, recorder):
        ommpx.MPxCommand.__init__(self)
        self._rec = recorder

    def doIt(self, args):
        self._rec.start()
        om.MGlobal.displayInfo('Recording now!')


class StopCommand(ommpx.MPxCommand):
    def __init__(self, recorder):
        ommpx.MPxCommand.__init__(self)
        self._rec = recorder

    def doIt(self, args):
        commands = self._rec.stop()
        if commands is None:
            om.MGlobal.displayWarning('Was not recording...')
            return

        label = self._prompt_for_label()
        if label is None:
            om.MGlobal.displayInfo('Recording discarded')
            return

        shelf.create_button(label, ';'.join(commands))

    def _prompt_for_label(self):
        dialog = prompt.LabelPromptDialog()
        return dialog.get_text()
