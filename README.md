# Judotraining Übungskatalog
---
Dies ist ein kleines Programm, das ich geschrieben habe, um eine schnelle Übersicht über alle Übungen bekommen zu können, die meine Frau Anna und ich und für unser Eltern-Kind-Judo überlegthaben. Es dient also zum einen als Datenbank. Zum anderen kann man sich schnell und einfach eine Trainingseinheit zusammenstellen. Jedes Mal, wenn man sich die Details einer Übungsform anschaut, hat man die Möglichkeit, sie dem aktuellen Trainingsplan hinzuzufügen. Wenn man sich den aktuellen Trainingsplan anschaut, hat man die Möglichkeit, ihn als Excel-File zu exportieren.

Um das Programm zu starten, gib führe bitte zunächst, die unten aufgeführten Befehle durch, um die entsprechende virtuelle Umgebung einzurichten.
Danach startest du das Programm mit folgendem Befehl in der command line:
``` bash
python judotechnique_katalogue.py
```


## Set up your Environment

Die notwendigen Packages sind in requirements.txt abgespeichert.

### **`macOS`** type the following commands : 


- Install the virtual environment and the required packages by following commands:

    ```BASH
    pyenv local 3.11.3
    python -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
### **`WindowsOS`** type the following commands :

- Install the virtual environment and the required packages by following commands.

   For `PowerShell` CLI :

    ```PowerShell
    pyenv local 3.11.3
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

    For `Git-Bash` CLI :

  ```BASH
    pyenv local 3.11.3
    python -m venv .venv
    source .venv/Scripts/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```


