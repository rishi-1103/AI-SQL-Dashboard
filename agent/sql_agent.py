from sqlalchemy import text
from database.db_connection import engine
from agent.llm import llm
from agent.prompts import SQL_PROMPT
import time


def generate_sql(user_question):
    prompt = f"""
{SQL_PROMPT}

User Question:
{user_question}
"""

    for attempt in range(5):
        try:
            response = llm.invoke(prompt)

            if isinstance(response.content, list):
                sql_query = response.content[0]["text"].strip()
            else:
                sql_query = response.content.strip()

            sql_query = (
                sql_query.replace("```sql", "")
                .replace("```", "")
                .strip()
            )

            return sql_query

        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(5)

    raise Exception("Failed after 5 retries.")


def execute_sql(sql_query):
    try:
        with engine.connect() as conn:
            result = conn.execute(text(sql_query))

            if result.returns_rows:
                columns = result.keys()
                rows = result.fetchall()
                return columns, rows

            return None, "Query executed successfully."

    except Exception as e:
        return None, str(e)