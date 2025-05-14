from .staff_sql_data import create_table, fetch_staff, insert_staff, delete_staff, update_staff
from .ramp_insp_sql_data import create_ramp_table

__all__ = [
    'create_table', 'fetch_staff', 'insert_staff', 'delete_staff', 'update_staff',
    'create_ramp_table'
]