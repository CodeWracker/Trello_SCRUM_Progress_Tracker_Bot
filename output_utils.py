from datetime import datetime
from heapq import merge
import plotly.graph_objects as go
import xlsxwriter


def generate_difficulty_chart(all_cards_difficulty_acc, done_difficulty_acc):

    # Generate the difficulty chart using plotly and save it as a png file
    # The chart is a line chart with two lines, one for the accumulated difficulty of all cards and the other for the accumulated difficulty of done cards

    # Convert the timestamps to dates
    all_cards_dates = []
    done_dates = []
    for acc in all_cards_difficulty_acc:
        dt = datetime.fromtimestamp(acc[0])
        all_cards_dates.append(dt)
    for acc in done_difficulty_acc:
        dt = datetime.fromtimestamp(acc[0])
        done_dates.append(dt)

    # Create the chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=all_cards_dates, y=[
                  acc[1] for acc in all_cards_difficulty_acc], name="Todas as Tarefas"))
    fig.add_trace(go.Scatter(x=done_dates, y=[
                  acc[1] for acc in done_difficulty_acc], name="Feito"))
    fig.update_layout(
        title="Acompanhamento do Progresso",
        xaxis_title="Data",
        yaxis_title="Dificuldade Acumulada",
        legend_title="Legenda",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple"
        )
    )

    # Save the chart as a png file with todays date
    today = datetime.today()
    str_today = today.strftime("%Y-%m-%d")
    # change fig size
    fig.update_layout(
        autosize=False,
        width=1000,
        height=500,


    )

    fig.write_image(f"output/{str_today}-difficulty_chart.png")


def generate_crit_activity_relationship(crit_activity):
    # generate a xlsx file with the relationship between the criteria and the cards that are related to them
    # the file is saved in the output folder

    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('output/crit_activity_relationship.xlsx')
    worksheet = workbook.add_worksheet()

    # Start from the first cell. Rows and columns are zero indexed.

    worksheet.write(0, 0, "Critérios")
    worksheet.write(0,  1, "Atividades")
    row = 1
    col = 0

    crits = []
    for crit in crit_activity:
        crits.append(crit)
    # sort crits
    crits.sort()

    # Iterate over the data and write it out row by row.
    for crit in crits:
        worksheet.write(row, col, crit)
        row_ini = row
        row_end = row
        for activity in crit_activity[crit]:
            worksheet.write(row, col, crit)
            worksheet.write(row, col + 1, activity)
            row_end = row
            row += 1
        # merge cells that are the same
        if (row_ini != row_end):
            worksheet.merge_range(row_ini, col, row_end, col, crit)

    workbook.close()

    return
