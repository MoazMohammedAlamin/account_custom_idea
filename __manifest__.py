
{
    "name": "Idea Customize Accounting ",
    "version": "13.0.1.0.0",
    "category": "Human Resources",
    "website": "",
    "author": "(IDEA)",
    "license": "AGPL-3",
    "installable": True,
    "application": False,
    "summary": "VIEW CUSTOMIZE WORK",
    "depends": ["account"],
    "external_dependencies": {"python": ["dateutil"]},
    "data": [
        "security/ir.model.access.csv",
        "views/hr_employee.xml",
    ],
}
