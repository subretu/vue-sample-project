def get_date_summary(cur):
    cur.execute(
        """
        with a1 as(
            select
                opstime::date as opsdate
                ,sum(value) as sum_value
            from
                sample_date_summary
            group by
                opstime::date
        )
        select
            right(opsdate::text,1) as id
            ,opsdate
            ,sum_value
        from
            a1
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


def delete_user(cur):
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
