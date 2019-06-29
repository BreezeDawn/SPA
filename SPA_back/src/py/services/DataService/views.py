import numpy as np
from flask import jsonify

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

        data_sql.add_array_to_db_one(data_one)

    except BaseException as e:
        logger.exception(e)

        result = dict(code=RET.SERVERERR, message=error_map[RET.SERVERERR], data=data_one)

        logger.info(result)

        return jsonify(result)

    result = dict(code=RET.OK, message=error_map[RET.OK], data=data_one)

    logger.info(result)

    return jsonify(result)
