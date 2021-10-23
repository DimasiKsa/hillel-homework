def format_records(records):
    if not records:
        return '(Empty recordset)'
    return '<br>'.join(f'<p></p> {rec}' for rec in records)
