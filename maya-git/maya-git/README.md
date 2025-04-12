# Maya Git Plugin

A Maya plugin that provides Git version control integration directly within Maya.

## Features

- Initialize Git repositories
- View Git status of files
- Add files to staging
- Commit changes with messages
- Simple and intuitive UI

## Installation

### Easy Installation (Recommended)
1. Simply drag the `install.mel` file into your Maya viewport
2. Follow the on-screen instructions

### Manual Installation
1. Copy the `src` directory to your Maya scripts directory:
   - Windows: `C:\Users\<username>\Documents\maya\scripts`
   - Mac: `~/Library/Preferences/Autodesk/maya/scripts`
   - Linux: `~/maya/scripts`

2. In Maya, open the Script Editor and run:
   ```python
   import maya.cmds as cmds
   cmds.loadPlugin('maya-git.py')
   ```

## Usage

1. Open the plugin window through the Maya menu or by running:
   ```python
   import maya.cmds as cmds
   cmds.loadPlugin('maya-git.py')
   ```

2. The plugin window will appear with the following sections:
   - Git Status: Shows the current status of files in your project
   - Git Operations: Contains buttons for common Git operations

3. Basic workflow:
   - Click "Initialize Git Repository" to start version control
   - Use "Refresh Status" to see changed files
   - Select files and click "Add Selected Files" to stage them
   - Enter a commit message and click "Commit Changes"

## Requirements

- Maya 2018 or later
- Git installed on your system
- Python 2.7 or later

## Notes

- The plugin uses the current Maya project directory as the Git repository root
- Make sure Git is properly installed and accessible from the command line
- The plugin requires proper file permissions to execute Git commands 