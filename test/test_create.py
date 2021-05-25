def test_add_project(app):
    app.testplan.selectTestplan()
    app.testplan.selectCases()
    app.testplan.savePlan()

