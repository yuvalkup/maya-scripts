import maya.OpenMaya as om
import maya.OpenMayaMPx as ommpx
import maya.cmds as cmds

import shelf
import config
import plugin_commands
import recorder

import importlib
importlib.reload(config)
importlib.reload(shelf)
importlib.reload(plugin_commands)
importlib.reload(recorder)


# Initialize the plugin
def initializePlugin(mobject):
    mplugin = ommpx.MFnPlugin(mobject)
    try:
        cmd_recorder = recorder.CommandRecorder()

        mplugin.registerCommand(config.RECORD_COMMAND_NAME, lambda: plugin_commands.RecordCommand(cmd_recorder))
        mplugin.registerCommand(config.STOP_COMMAND_NAME, lambda: plugin_commands.StopCommand(cmd_recorder))

        shelf.create_shelf()

    except Exception as e:
        om.MGlobal.displayError("Failed to register command: customShelfCommand - {}".format(e))


# Uninitialize the plugin
def uninitializePlugin(mobject):
    mplugin = ommpx.MFnPlugin(mobject)
    try:
        mplugin.deregisterCommand(config.RECORD_COMMAND_NAME)
        mplugin.deregisterCommand(config.STOP_COMMAND_NAME)

    except Exception as e:
        om.MGlobal.displayError("Failed to deregister command: customShelfCommand - {}".format(e))
