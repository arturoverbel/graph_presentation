import sys
from module.export_lab_real import ExportLabReal
from module.calculate_lab_real import CalculateLabReal


def export(filename: str, stuff_to_export="dist"):
    lab = ExportLabReal(testing=True)
    lab.export_lab_real(filename, stuff_to_export=stuff_to_export)


def calculate(filename="", attempt=2):
    lab_calc = CalculateLabReal(filename, testing=True)
    lab_calc.calculate(attempt)


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

    stuff_to_export = "dist"
    if len(sys.argv) >= 4:
        stuff_to_export = sys.argv[3]

    export(filename, stuff_to_export)
    exit()

if exec_command == "calculate":
    filename = ""
    attempt = 2

    if len(sys.argv) < 3:
        print("Falta argumento filename")
        exit()

    if len(sys.argv) >= 3:
        filename = sys.argv[2]

    if len(sys.argv) < 4:
        print("Falta argumento attemp")
        exit()

    if len(sys.argv) >= 4:
        attempt = int(sys.argv[3])

    calculate(filename, attempt)
    exit()

print("Don't recognize the command argv: ", exec_command)


