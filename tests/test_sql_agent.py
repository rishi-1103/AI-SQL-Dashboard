from agent.sql_agent import generate_sql, execute_sql

question = "What is the total revenue?"

print("Question:", question)

sql = generate_sql(question)
print("\nGenerated SQL:")
print(sql)

columns, rows = execute_sql(sql)

print("\nResults:")

if columns:
    print(columns)
    for row in rows:
        print(row)
else:
    print(rows)