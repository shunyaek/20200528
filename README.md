![GitHub Super Linter](https://github.com/shunyaek/20200528/workflows/GitHub%20Super%20Linter/badge.svg)

# 20200528

To run this project, install the required packages in a Python virtual environment.

To create an environment, use the following command
```bash
python -m venv <environment_name>
```

OPTIONAL: Update `pip`. Use the following commands on Linux and Windows respectively:
```bash
pip install --upgrade pip
```
```powershell
python -m pip install --upgrade pip
```

To activate the environment, use the following commands on Linux and Windows respectively:
```bash
source env/bin/activate
```
```powershell
.\env\Scripts\Activate.ps1
```

To deactivate the environment, use the following command
```bash
deactivate
```

To install the dependencies, use the following command
```bash
pip install -r requirements.txt
```

Finally, to run the project, run `manage.py` in the `src` directory with the `runserver` argument
```bash
python src/manage.py runserver
```
