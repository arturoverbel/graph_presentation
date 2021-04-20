import sys
from module.export_lab_real import ExportLabReal
from module.calculate_lab_real import CalculateLabReal


def export(filename: str):
    lab = ExportLabReal(testing=True)
    lab.export_lab_real(filename)


def calculate(filename=""):
    lab_calc = CalculateLabReal(filename, testing=True)
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
    filename = ""
    if len(sys.argv) >= 3:
        filename = sys.argv[2]
    else:
        print("Falta argumento filename")

    calculate(filename)
    exit()

print("Don't recognize the command argv: ", exec_command)


