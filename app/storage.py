import json
from models import db, EuromillionsResult

def get_result_by_date(date):
    return EuromillionsResult.query.get(date)

def save_result(date, numbers, stars, prizes=None):
    result = EuromillionsResult(
        date=date,
        numbers=','.join(map(str, numbers)),
        stars=','.join(map(str, stars)),
        prizes=json.dumps(prizes) if prizes else None
    )
    db.session.merge(result)
    db.session.commit()