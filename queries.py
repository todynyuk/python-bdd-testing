from utils.database_methods import get_data_from_database_by_query
from utils import string_utils


def get_login_by_id(user_id):
    query = f"""SELECT login FROM users WHERE id = {user_id};"""
    return string_utils.del_brackets_and_quotes_from_str(get_data_from_database_by_query(query))


def get_password_by_login(user_login):
    query = f"""SELECT password FROM users WHERE login = '{user_login}'"""
    return string_utils.del_brackets_and_quotes_from_str(get_data_from_database_by_query(query))


def get_first_name_by_login(login):
    query = f"""SELECT first_name FROM users WHERE login = '{login}';"""
    return string_utils.del_brackets_and_quotes_from_str(get_data_from_database_by_query(query))


def get_last_name_by_login(login):
    query = f"""SELECT last_name FROM users WHERE login = '{login}';"""
    return string_utils.del_brackets_and_quotes_from_str(get_data_from_database_by_query(query))


def get_zip_code_by_login(login):
    query = f"""SELECT zip_code FROM users WHERE login = '{login}';"""
    return string_utils.del_brackets_and_quotes_from_str(get_data_from_database_by_query(query))


def get_item_name_by_user_id(user_id):
    query = f"""SELECT product_name FROM public.users_orders WHERE user_id = {user_id}"""
    return string_utils.del_brackets_and_quotes_from_str(get_data_from_database_by_query(query))
