import mysql.connector as connector
c=connector.connect(host="localhost",
                    user="root",
                    password="Honey@105",
                    database="jira_project")

cursor=c.cursor()
while True:
    s_no=int(input())
    number=input()
    name=input()
    description=input()
    reporter=input()
    status=input()
    due_d=input()
    assignee=input()

    query="insert into jira values({},'{}','{}','{}','{}','{}','{}','{}')".format(s_no,number,name,description,reporter,status,due_d,assignee)
    cursor.execute(query)
    c.commit()
    print("data inserted successfully")
   