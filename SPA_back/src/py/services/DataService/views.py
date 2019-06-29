import numpy as np
from flask import jsonify, request

from SPA_back.src.py.services.DataService import data_blue
from SPA_back.src.py.services.DataService.utils.DataSql import DataSql
from SPA_back.src.py.utils.GetLogger.logger import setup_log
from SPA_back.src.py.response_code import RET, error_map

logger = setup_log(__name__)

data_sql = DataSql()


@data_blue.route('/', methods=['GET'])
def data_test():
    result = dict(code=RET.OK, message=error_map[RET.OK])

    logger.info(result)

    return jsonify(result)


@data_blue.route('/data/get_array', methods=['GET'])
def get_array():
    data_one = None

    try:
        data_one = np.random.randint(0, 100, 10).tolist()

        flag = data_sql.add_array_to_db_one(data_one)

        assert flag, "error to db one"

    except BaseException as e:
        logger.exception(e)

        result = dict(code=RET.SERVERERR, message=error_map[RET.SERVERERR], data=data_one)

        logger.info(result)

        return jsonify(result)

    result = dict(code=RET.OK, message=error_map[RET.OK], data=data_one)

    logger.info(result)

    return jsonify(result)


@data_blue.route('/data/post_array', methods=['POST'])
def post_array():
    array = None

    try:
        array = request.json.get("array", None)

        if not array or not isinstance(array, str):
            raise TypeError("invalid input, array is None or isn't str type")

        array = eval(array)

        flag = data_sql.add_array_to_db_two(array)

        assert flag, "error to db two"

    except Exception as e:

        exc = dict(code=RET.SERVERERR, message=error_map[RET.SERVERERR], array=array, e=str(e))

        logger.exception(exc)

        return jsonify(exc)

    result = dict(code=RET.OK, message=error_map[RET.OK], array=array)

    logger.info(result)

    return jsonify(result)
