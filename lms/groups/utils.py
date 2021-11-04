def format_records(records):
    if not records:
        return "(Empty recordset)"
    return "<br>".join(
        f'<a href="/groups/update_groups/{rec.id}/">EDIT</a>{rec}' for rec in records
    )
