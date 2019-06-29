from SPA_back.src.py import db
from SPA_back.src.py.services.DataService import models
from SPA_back.src.py.utils.GetLogger.logger import setup_log

logger = setup_log(__name__)


class DataSql:
    def __init__(self):
        self.db = db

    def add_array_to_db_one(self, array):
        try:
            for item in array:
                self.add_item_to_db_one(item)
        except BaseException as e:
            logger.exception(e)
            return False

        return True

    def add_item_to_db_one(self, item):
        # noinspection PyBroadException
        try:
            data_obj = models.DataOne(data=item)

            self.db.session.add(data_obj)

        except Exception as e:

            self.db.session.rollback()

            logger.warning(e)

    def add_array_to_db_two(self, array):
        try:
            for item in array:
                self.add_item_to_db_two(item)
        except BaseException as e:
            logger.exception(e)
            return False

        return True

    def add_item_to_db_two(self, item):
        # noinspection PyBroadException
        try:
            data_obj = models.DataTwo(data=item)

            self.db.session.add(data_obj)

        except Exception as e:

            self.db.session.rollback()

            logger.warning(e)
