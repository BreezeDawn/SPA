from flask import jsonify

from SPA_back.src.py.services.DataService import data_blue
from SPA_back.src.py.utils.GetLogger.logger import setup_log
from SPA_back.src.py.response_code import RET, error_map

logger = setup_log(__name__)


@data_blue.route('/', methods=['GET'])
def data_test():
    result = dict(code=RET.OK, message=error_map[RET.OK])

    logger.info(result)

    return jsonify(result)
