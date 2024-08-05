import maya.api.OpenMaya as om
import maya.mel as mel

import config
import commands_stack


class CommandRecorder:
    def __init__(self):
        self._records = commands_stack.CommandsStack()
        self._cb_id = None

    def start(self):
        if self._cb_id:
            om.MGlobal.displayWarning('Already recording...')
            return

        self._records.clear()

        def callback(message, messageType, clientData):
            if messageType == om.MCommandMessage.kInfo:
                if message.startswith('Undo'):
                    self._records.undo()
                if message.startswith('Redo'):
                    self._records.redo()

            if messageType in [om.MCommandMessage.kMELProc, om.MCommandMessage.kMELCommand]:
                self._records.push(message)

        self._cb_id = om.MCommandMessage.addCommandOutputCallback(callback)

    def stop(self):
        if not self._cb_id:
            return

        om.MMessage.removeCallback(self._cb_id)
        self._cb_id = None

        filtered = [i for i in self._records.list if not i.startswith(config.COMMANDS_PREFIX)]
        return filtered
