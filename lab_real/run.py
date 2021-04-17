import sys
from module.export_lab_real import ExportLabReal
from module.calculate_lab_real import CalculateLabReal


def export(filename=""):
    lab = ExportLabReal(testing=True)
    lab.export_lab_real(filename)


def calculate():
    lab_calc = CalculateLabReal(testing=True)
    lab_calc.calculate()


"""
Start Run
"""
exec_command = "export"
if len(sys.argv) >= 2:
    exec_command = sys.argv[1]

if exec_command == "export":
    filename = ""
    if len(sys.argv) >= 3:
        filename = sys.argv[2]

    export(filename)
    exit()

if exec_command == "calculate":
    calculate()
    exit()

print("Don't recognize the command argv: ", exec_command)


