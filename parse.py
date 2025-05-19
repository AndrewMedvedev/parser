from typing import cast

from bs4 import BeautifulSoup, ResultSet, Tag

from constants import ORGS, UNIVERSITY_AND_DIRECTIONS
from rest import get_html
from schemas import Applicant


async def send_data():
    count = -1
    data = []
    for institute in UNIVERSITY_AND_DIRECTIONS:
        count += 1
        data_directions = {institute: []}
        data.append(data_directions)
        for direction in UNIVERSITY_AND_DIRECTIONS[institute]:
            columns = await get_table_data(
                direction=direction, org=ORGS[count], institute=institute
            )
            data_directions[institute] = {direction: columns}


def valid_data(cells: ResultSet[Tag], institute: str, direction: str) -> dict:
    applicant_id = cells[1].get_text(strip=True)
    rating = int(cells[0].get_text(strip=True))
    original = cells[1].get_text(strip=True) != "Да"
    priority = (
        int(cells[11].get_text(strip=True))
        if cells[11].get_text(strip=True)
        not in {"Нет", "дети участников СВО", "Дети-сироты и оставшиеся без попечения родителей"}
        else 0
    )
    points = (
        int(cells[5].get_text(strip=True)) if cells[5].get_text(strip=True) not in {"—", ""} else 0
    )
    bonus_points = (
        int(cells[6].get_text(strip=True)) if cells[6].get_text(strip=True) != "—" else 0
    )
    result = Applicant(
        applicant_id=applicant_id,
        rating=rating,
        institute=institute,
        direction=direction,
        priority=priority,
        points=points,
        bonus_points=bonus_points,
        original=original,
    )
    return result.model_dump()


async def get_table_data(direction: str, org: int, institute: str):
    data = await get_html(direction=direction, org=org)
    soup = BeautifulSoup(data, "html.parser")
    rows = soup.find_all("tr")
    data = []
    for row in rows[2:]:
        cells = cast(Tag, row).find_all("td")
        result = valid_data(
            cells=cast(ResultSet[Tag], cells), institute=institute, direction=direction
        )
        data.append(result)
    return data
