def test_add_project(app):
    #app.session.login("ekaterina.lisovets", "Lisovets1")
    app.testplan.selectTestplan()
    app.testplan.selectCases()
    app.testplan.savePlan()

