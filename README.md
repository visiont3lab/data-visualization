# Data Visualization course

## [Course Overview](overview.md)

## Setup Editor (Vscode) and Get Data Visualization course folder

1. [Install Vsocde](https://code.visualstudio.com/download)
   - [Add Python Plugins](https://code.visualstudio.com/docs/languages/python), Add extension Python, Jupyter, Kite Python Autocomplete, Edit csv
2. [Install Kite Python Autocomplete](https://kite.com/download/)
3. [Install Git Bash](https://www.stanleyulili.com/git/how-to-install-git-bash-on-windows/), inside vscode select bash terminal
4. [Install Python 3.6 and Pip](https://www.python.org/downloads/)
    - [Lettura Utile](https://gist.github.com/ricpol/2ca0ae46f02bfddf08036fa85519aa97)
    Notate che Python verrà installato in C:/Program Files/Python37 se lo installate "for all user"; se lo installate solo per voi stessi, finirà invece in C:/Users/<VOSTRO_NOME>/AppData/Local/Programs/Python/Python37.)
5. [Clone Data Visualization repository](https://github.com/visiont3lab/data-visualization)
6. Create Virtual Environment

    ```
    pip install virtualenv
    virtualenv --python=python3.6 env
    source env/bin/activate
    cd data-visualization
    pip install -r requirements
    ```

7. [Setup Debugger Pyhton Vscode](https://code.visualstudio.com/docs/python/debugging)
8. Test Installation

    ```
    bokeh, dash app
    ```

