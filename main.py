import pandas as pd
import os

inspecoes = {}

for txt in os.listdir("Inspecoes"):
    with open(f"Inspecoes/{txt}", "r", encoding="utf-8") as arquivo:
        inspecoes[txt[:-4]] = arquivo.read()

arquivo = pd.read_excel('RotaInspecao.xlsx')

def unir(frase):
    palavra = ""
    for i in frase:
        palavra += i

    return palavra

def textosensitiva(fonte, arquivo):
    linhas = []

    equipamento = arquivo[3]
    
    referencia = "           " if pd.isna(arquivo[2]) else arquivo[2]
    local = arquivo[0] + " " + arquivo[1]

    linhas.append(f"{local} / {referencia} / {equipamento}")

    if fonte == "BOMBA":
        linhas.append(inspecoes["bomba"])
    elif fonte == "AGITADOR":
        linhas.append(inspecoes["agitador"])
    elif fonte == "VENTILADOR":
        linhas.append(inspecoes["ventilador"])
    elif fonte == "MOTOR":
        linhas.append(inspecoes["motor"])
    elif fonte == "BOMBA DE VÁCUO":
        linhas.append(inspecoes["bombadevacuo"])
    elif fonte == "UNIDADE HIDRÁULICA":
        linhas.append(inspecoes["UnidadeHidraulica"])
    elif fonte == "REDUTOR":
        linhas.append(inspecoes["redutor"])
    elif fonte == "ROLO":
        linhas.append(inspecoes["rolo"])
    else:
        linhas.append("Fora do padrão")

    linhas.append("\n\n")

    return "\n".join(linhas)

with open("rota.txt", "w", encoding="utf-8") as f:

    for data in arquivo.values:
        equipamento = unir(data[3].split())

        if "BOMBADE" in equipamento:
            f.write(textosensitiva("BOMBA DE VÁCUO", data))

        elif "BOMBA" in equipamento:
            f.write(textosensitiva("BOMBA", data))

        elif "AGITADOR" in equipamento:
            f.write(textosensitiva("AGITADOR", data))

        elif "VENTILADOR" in equipamento:
            f.write(textosensitiva("VENTILADOR", data))

        elif "MOTOR" in equipamento:
            f.write(textosensitiva("MOTOR", data))

        elif "UNIDADE" in equipamento:
            f.write(textosensitiva("UNIDADE HIDRÁULICA", data))

        elif "REDUTOR" in equipamento:
            f.write(textosensitiva("REDUTOR", data))

        elif "ROLO" in equipamento:
            f.write(textosensitiva("ROLO", data))

        else:
            f.write(textosensitiva("FORA DE FORMATO", data))