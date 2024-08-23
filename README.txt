1. Download and Install SourceTree(https://www.sourcetreeapp.com/)
    1a. Select Bitbucket Option >> Click Next
    1b. Click Skip >> Next
    1c. Fill Name and Email
    1d. Click "No" button

2. Download and Install Visual Studio Code(https://code.visualstudio.com/Download)
    2a. Open your workspace Folder 
    NOTE: Do not forget to tick "TRUST THE AUTHORS OF ALL FILES...." checkbox
    2b. Click "Yes, I trust the authors...." button
 
3. Download and Install Python(latest version - https://www.python.org/downloads/)
    # windows
    3a. When installing Python dont forget to tick "Add python.exe to Playwright" check box
    3b. Once successfully installed, Open CMD and enter:
        - python -V
        - where python
        - python
    3c. Check if added on the Environment variables(User variable) >> double click "Path" Variable
        - C:\Users\<userfolder> Tech\AppData\Local\Programs\Python\Python<version>\
        - C:\Users\<userfolder> Tech\AppData\Local\Programs\Python\Python<version>\Scripts\
        Note: Add manually if missing (Use "where python" to check correct folder path)
    3d. Add on Environment variable(User variable) >> Click "New..." button
        - PYTHONPATH = C:\Users\<userfolder>

    # mac      
    3a. Download and install Python
    3b. Once successfully installed, Open CMD and enter:
        - python -V
        - which python
    3c. Add on Environment variable(User variable) >> Click "New..." button
        - Open terminal
            - Enter 'touch .bash_profile'
            - Enter 'open .bash_profile'
                - Copy and paste in the .bash_profile terminal:
                    export PATH="/usr/local/bin:$PATH" 
                    export PATH="/Users/<userName>/demoWWEB/vmWEB/bin/playwright:$PATH" (or you can type 'which playwright' to see the directory)
            - Enter 'source .bash_profile
     
4. Download and Add to PATH Allure(https://github.com/allure-framework/allure2/releases)
    4a. Extract downloaded folder in your C:\Program Files
    4b. Add on the Environment variables(System variable) >> double click "Path" Variable >> "New" button
        - C:\Program Files\allure-<version>\bin

5. How to create Python Virtual Machine
    Open terminal(Ctrl + `) and enter:
    # windows
    5.1. Create your VM path directory: 
        # windows
        - py -m venv <VMname> (py -m venv vmWEB)
    5.2. Activate you VM:
        # windows
        - .\vmWEB\Scripts\activate (If error encountered - Perform Issue Encountered 1)
        Note: To deactivate - deactivate
    5.3. Install requirements.txt
        5.3a. to Install, enter (vmWEB should be activated)
            - pip install -r requirements.txt
            - python.exe -m pip install --upgrade pip (if need to update)
            Note: To generate a new requirement.txt file - pip freeze > requirements.txt

    # mac
    5.1. Create your VM path directory: 
        - python3 -m venv vmWEB
    5.2. Activate you VM:
        - source vmWEB/bin/activate
        Note: To deactivate - deactivate
    5.3. Install requirements.txt
        5.3a. to Install, enter (vmWEB should be activated)
            - pip install -r requirements.txt
            - python.exe -m pip install --upgrade pip (if need to update)
            Note: To generate a new requirement.txt file - pip freeze > requirements.txt

(OPTIONAL)
6. Follow Python Playwright Installation Guide - https://playwright.dev/python/docs/intro
    6a. Open terminal(Ctrl + `) and enter:
        - pip install pytest-playwright
        - pip install --upgrade pip
        - playwright install
ç 
    6b. Python
        Python Extension Pack
        python snippets 
        