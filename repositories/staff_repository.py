from db.run_sql import run_sql
from models.staff import Staff


def save(member):
    sql = "INSERT INTO staff (name, start_date, department, performance) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [member.name, member.start_date, member.department, member.performance]
    results = run_sql(sql, values)
    id = results[0]['id']
    member.id = id
    return member

def select_all():
    staff = [] 

    sql = "SELECT * FROM staff"
    results = run_sql(sql)

    for row in results:
        member = Staff(row['name'], row['start_date'], row['department'], row['performance'])
        staff.append(member)
    return staff

def select(id):
    member = None
    sql = "SELECT * FROM staff WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        member = Staff(result['name'], result['start_date'], result['department'], result['performance'])
    return member


def delete_all():
    sql = "DELETE FROM staff"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM staff WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(member):
    sql = "UPDATE staff SET (name, start_date, department, performance) = (%s, %s, %s, %s) WHERE id = %s"
    values = [member.name, member.start_date, member.department, member.performance]
    run_sql(sql, values)


# def tasks(user):

#     tasks = []

#     sql = "SELECT * FROM tasks WHERE user_id = %s"
#     values = [user.id]
#     results = run_sql(sql, values)

#     for row in results:
#         task = Task(row['description'], user, row['duration'], row['completed'], row['id'])
#         tasks.append(task)

#         return tasks