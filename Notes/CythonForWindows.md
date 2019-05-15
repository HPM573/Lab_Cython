
# Install Cython on Windows


Confirm that Python is installed and 
the system variable name is set up correctly. Open a "Windows PowerShell" 
(click on the Windows icon and type 'Windows PowerShell", 
then click on the Windows PowerShell icon). Once the command windows is open, type `python` and hit Enter. 

If Python is installed correctly, you should see output similar to what is shown below:  
    
    Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
    Type "help", "copyright", "credits" or "license" for more information.
    
If you receive a message such as:

    The term 'python' is not recognized...` 
    
python is either not installed or the system variable path is not set up correctly.

The easiest way to proceed is to 
[reinstall Python](https://www.python.org/downloads/) and 
to make sure that 'Add Python 3.7 to PATH' is checked, and 
under Customize installation 'pip' is checked to be installed.      

If the above approach failed, follow the instruction [here](https://datatofish.com/add-python-to-windows-path/) 
to add python to Windows Path. 

Type `pip -V` in the command window and hit Enter. If you see a message like

    pip 19.0.3 from c:\users\ry87\appdata\local\programs\python\python37-32\lib\site-packages\pip (python 3.7)

it means that `pip` is installed correctly on your computer. 
Otherwise, follow the instruction [here](https://www.liquidweb.com/kb/install-pip-windows/) to install `pip`. 

To install `Cython`, 
type `pip install Cython` in the command windows and hit enter.


