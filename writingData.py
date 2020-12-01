from analysingData import analyse_data, salidas_lista, further_info
import pandas as pd 
import datetime as dt

from openpyxl.formatting.rule import IconSetRule
from openpyxl.formatting.rule import Rule
from openpyxl.styles import PatternFill, Color
from openpyxl.styles.differential import DifferentialStyle


FILENAME = "C:/Users/javie/OneDrive/Documentos Javier/Personal/análisis/analisisArtistas.xlsx"

def write_further_info(sheet):
	salidas = salidas_lista(FILENAME)

	info = further_info(FILENAME)

	initial_row = 79

	sheet[f"G{initial_row}"] = f"Salidas: {len(salidas)}"
	sheet[f"H{initial_row}"] = "Previous pos"
	sheet[f"I{initial_row}"] = "Previous playcount"

	for salida in salidas:
		initial_row += 1
		sheet[f"G{initial_row}"] = salida[0]
		sheet[f"H{initial_row}"] = salida[1]
		sheet[f"I{initial_row}"] = salida[2]

	initial_row = 79

	sheet[f"L{initial_row}"] = "Subida más fuerte"
	sheet[f"L{initial_row + 1}"] = "Bajada más fuerte"
	sheet[f"L{initial_row + 2}"] = "Entrada más fuerte"
	sheet[f"N{initial_row - 1}"] = "Playcount"
	sheet[f"O{initial_row -1}"] = "Diff pos"
	sheet[f"P{initial_row - 1}"] = "Diff rep"


	for idx, artist in enumerate(info):
		sheet[f"M{initial_row + idx}"] = artist[0]
		sheet[f"N{initial_row + idx}"] = artist[1]
		sheet[f"O{initial_row  + idx}"] = artist[2]
		sheet[f"P{initial_row + idx}"] = artist[3]







def format_data(writer, current_date):
	workbook = writer.book
	sheet = workbook[current_date]
	#sheet = workbook.active

	#Fill ("NEW") rule
	blue_bg = PatternFill(bgColor = Color(indexed = 27))
	diff_style = DifferentialStyle(fill = blue_bg)
	rule = Rule(type = "expression", dxf = diff_style)
	rule.formula = ['$D2 = "NEW"']
	sheet.conditional_formatting.add("D2:E201", rule)
	
	#Arrow rule
	rule_arrow = IconSetRule('3Arrows','num',[-200,0,1])
	sheet.conditional_formatting.add("D2:E201",rule_arrow)

	write_further_info(sheet)

	workbook.save(FILENAME)






def write_data(filename):
	columns = ("name", "playcount", "Dif pos", "Dif rep")
	data = analyse_data(FILENAME)
	df = pd.DataFrame(data, columns = columns, index = range(1, len(data) + 1)) 
	current_date = (dt.date.today() - dt.timedelta(days = 1)).strftime("%Y-%m")
	with pd.ExcelWriter(filename, engine = "openpyxl", mode = 'a') as writer:
		df.to_excel(writer, sheet_name = current_date)
		workbook = writer.book
		format_data(writer, current_date)

write_data(FILENAME)

