from termgraph import Data, Args, BarChart
def show_test_result(files,analysis):
    labels = ["Files","Functions","Classes","Variables","Imports","Calls"]
    values = [len(files),len(analysis["functions"]),len(analysis["classes"]),len(analysis["variables"]),len(analysis["imports"]),len(analysis["calls"])]
    data = Data(values, labels)

    chart = BarChart(data)

    chart.draw()

def show_result(passed, failed):

    labels = ["Passed", "Failed"]

    values = [passed, failed]

    data = Data(values, labels)

    chart = BarChart(data)

    chart.draw()