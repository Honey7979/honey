from jira import JIRA 

jt= {'server': "https://honey13.atlassian.net/"}
jira = JIRA(options = jt, basic_auth = ("honey22@navgurukul.org","2hIFgdy5RHYaUTJnWK6Z172D"))

# we display only three things in 1 loop at once

for issue in jira.search_issues(jql_str='project = HoneyComb'):
    print('{}: {}:{}'.format(issue.key,issue.fields.summary,     
                         issue.fields.reporter.displayName))

for p in jira.search_issues(jql_str='project = HoneyComb'):
    print('{}: {}:{}'.format(p.fields.description,p.fields.duedate,
                             p.fields.status))   
                        
# for v in jira.search_issues(jql_str='project = HoneyComb'):
#     print('{}: {}:{}'.format(v.fields.Number,     
#                          v.fields.reporter.displayName))