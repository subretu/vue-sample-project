def get_date_summary(cur):
    cur.execute(
        """
        select
            id
            ,opsdate
            ,sum_value
        from
            sample_date_summary2
        order by
            opsdate
        ;
        """
    )
    rows = cur.fetchall()
    return rows


def get_time_summary(cur):
    cur.execute(
        """
        select
            opstime
            ,value
        from
            sample_date_summary
        order by
            opstime
        ;
        """
    )
    rows = cur.fetchall()
    return rows


def get_date_stack_summary(cur):
    cur.execute(
        """
        select
            opstime::date as opsdate
            ,sum(value) as sum_value1
            ,(sum(value)*1.1)::integer as sum_value2
            ,(sum(value)*0.6)::integer as sum_value3
        from
            sample_date_summary
        group by
            opstime::date
        order by
            opsdate
        ;
        """
    )
    rows = cur.fetchall()
    return rows


def delete_id(conn, cur, id):
    cur.execute(f"delete from sample_date_summary2 where id = '{id}' ;")
    conn.commit()


def insert_data(conn, cur, input_id, input_opsdate, input_value):
    cur.execute(
        f"insert into sample_date_summary2 (id, opsdate, sum_value) values({input_id}, '{input_opsdate}', {input_value});"
    )
    conn.commit()


def get_json_data(cur):
    cur.execute(
        """
        select
            json_data
        from
            sample_date_summary2
        limit 1
        ;
        """
    )
    rows = cur.fetchall()
    return rows


def get_member_name(conn, cur, id):
    cur.execute(f"select name from members where member_id = '{id}';")
    rows = cur.fetchall()
    return rows
