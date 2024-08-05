import maya.OpenMayaMPx as ommpx
import maya.cmds as cmds

import config


def create_button(label, command, image='commandButton.png'):
    if cmds.shelfLayout(config.SHELF_NAME, exists=True):
        cmds.shelfButton(label=label, annotation=label, sourceType='mel', command=command, image1=image, imageOverlayLabel=label, parent=config.SHELF_NAME)


def remove_button(label):
    if cmds.shelfLayout(config.SHELF_NAME, exists=True) and cmds.shelfButton(label, exists=True):
        cmds.deleteUI(label)


def create_shelf():
    if cmds.shelfLayout(config.SHELF_NAME, exists=True):
        return

    cmds.shelfLayout(config.SHELF_NAME, parent='ShelfLayout')
    create_button('Record', config.RECORD_COMMAND_NAME)
    create_button('Stop', config.STOP_COMMAND_NAME)


def remove_shelf():
    if cmds.shelfLayout(config.SHELF_NAME, exists=True):
        cmds.deleteUI(config.SHELF_NAME, layout=True)
