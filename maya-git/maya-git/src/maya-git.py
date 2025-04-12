import os
import sys
import subprocess
import maya.cmds as cmds
import maya.mel as mel
from functools import partial

class MayaGitPlugin:
    def __init__(self):
        self.window_name = "mayaGitWindow"
        self.title = "Maya Git"
        self.size = (400, 600)
        
    def create_ui(self):
        if cmds.window(self.window_name, exists=True):
            cmds.deleteUI(self.window_name)
            
        cmds.window(self.window_name, title=self.title, widthHeight=self.size)
        
        main_layout = cmds.columnLayout(adjustableColumn=True)
        
        # Git Status Section
        cmds.frameLayout(label="Git Status", collapsable=True)
        cmds.textScrollList("gitStatusList", numberOfRows=10, allowMultiSelection=True)
        cmds.button(label="Refresh Status", command=self.refresh_status)
        
        # Git Operations Section
        cmds.frameLayout(label="Git Operations", collapsable=True)
        cmds.button(label="Initialize Git Repository", command=self.init_git)
        cmds.button(label="Add Selected Files", command=self.add_files)
        cmds.textFieldGrp("commitMessage", label="Commit Message:", text="")
        cmds.button(label="Commit Changes", command=self.commit_changes)
        
        cmds.showWindow(self.window_name)
        
    def init_git(self, *args):
        project_path = cmds.workspace(q=True, directory=True)
        try:
            subprocess.run(["git", "init"], cwd=project_path, check=True)
            cmds.confirmDialog(title="Success", message="Git repository initialized successfully!")
            self.refresh_status()
        except subprocess.CalledProcessError as e:
            cmds.confirmDialog(title="Error", message=f"Failed to initialize Git repository: {str(e)}")
            
    def add_files(self, *args):
        project_path = cmds.workspace(q=True, directory=True)
        selected_files = cmds.textScrollList("gitStatusList", q=True, selectItem=True)
        if not selected_files:
            cmds.confirmDialog(title="Warning", message="Please select files to add")
            return
            
        try:
            subprocess.run(["git", "add"] + selected_files, cwd=project_path, check=True)
            cmds.confirmDialog(title="Success", message="Files added successfully!")
            self.refresh_status()
        except subprocess.CalledProcessError as e:
            cmds.confirmDialog(title="Error", message=f"Failed to add files: {str(e)}")
            
    def commit_changes(self, *args):
        project_path = cmds.workspace(q=True, directory=True)
        commit_message = cmds.textFieldGrp("commitMessage", q=True, text=True)
        
        if not commit_message:
            cmds.confirmDialog(title="Warning", message="Please enter a commit message")
            return
            
        try:
            subprocess.run(["git", "commit", "-m", commit_message], cwd=project_path, check=True)
            cmds.confirmDialog(title="Success", message="Changes committed successfully!")
            self.refresh_status()
        except subprocess.CalledProcessError as e:
            cmds.confirmDialog(title="Error", message=f"Failed to commit changes: {str(e)}")
            
    def refresh_status(self, *args):
        project_path = cmds.workspace(q=True, directory=True)
        try:
            result = subprocess.run(["git", "status", "--porcelain"], 
                                  cwd=project_path, 
                                  capture_output=True, 
                                  text=True, 
                                  check=True)
            
            status_items = result.stdout.splitlines()
            cmds.textScrollList("gitStatusList", e=True, removeAll=True)
            
            for item in status_items:
                if item.strip():
                    cmds.textScrollList("gitStatusList", e=True, append=item.strip())
                    
        except subprocess.CalledProcessError as e:
            cmds.confirmDialog(title="Error", message=f"Failed to get Git status: {str(e)}")

def initializePlugin(mobject):
    plugin = MayaGitPlugin()
    cmds.evalDeferred(plugin.create_ui)

def uninitializePlugin(mobject):
    if cmds.window("mayaGitWindow", exists=True):
        cmds.deleteUI("mayaGitWindow") 