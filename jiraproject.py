from jira import JIRA 
import mysql.connector as connector


jt= {'server': "https://honey13.atlassian.net/"}
jira = JIRA(options = jt, basic_auth = ("honey22@navgurukul.org","2hIFgdy5RHYaUTJnWK6Z172D"))

# we display only three things in 1 loop at once

# for issue in jira.search_issues(jql_str='project = HoneyComb'):
#     print('{}: {}:{}'.format(issue.key,issue.fields.summary,     
#                          issue.fields.reporter.displayName))

# for p in jira.search_issues(jql_str='project = HoneyComb'):
#     print('{}: {}:{}'.format(p.fields.description,p.fields.duedate,
#                              p.fields.status))   
                    

# import mysql.connector as connector
c=connector.connect(host = "localhost",
                    user = "root",
                    password = "Honey@105",
                    database = "final_jira")

for issue in jira.search_issues(jql_str = 'project=jira_striver'):
    name = issue.fields.summary
    number = issue.key
    description = issue.fields.description
    reporter = issue.fields.reporter.displayName
    status = issue.fields.status
    due_date = issue.fields.duedate
    issue_type = issue.fields.issuetype
    assignee = issue.fields.assignee
    query = "insert into jira13 values('{}','{}','{}','{}','{}','{}','{}','{}')".format(name,number,description,reporter,status,due_date,issue_type,assignee)
    
    # A cursor is an object which helps to execute the query and fetch the records from the database.
    honey = c.cursor()

    honey.execute(query)
    
    #  It basically provides the database confirmation regarding the changes made by a user or an application in the database.
    c.commit()
    
    print("data inserted successfully")
    