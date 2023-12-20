from typing import List

from sqlalchemy import text

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Hotel


class HotelDao(GeneralDAO):

    _domain_type = Hotel

    def find_by_city(self, city: str) -> List[object]:
        return self._session.query(Hotel).filter(Hotel.city == city).order_by(Hotel.city).all()
    
    def get_price_value(self, filter: str):
        try:
            query = text("CALL CallGetPriceStat(:stat_type)")
            result = self._session.execute(query, {"stat_type": filter})

            # Fetch all rows from the result set
            results = result.fetchall()

            # Commit the transaction
            self._session.commit()

            # Return the fetched results
            return results

        except Exception as e:
            # Rollback the transaction in case of an error
            self._session.rollback()
            raise e
        