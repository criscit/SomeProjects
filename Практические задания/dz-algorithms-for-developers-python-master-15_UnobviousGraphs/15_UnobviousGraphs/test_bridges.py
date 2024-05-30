from unittest import TestCase
from typing import Dict, List


from bridges import is_project_success


class BridgesTest(TestCase):

    @staticmethod
    def read(project_code: str) -> Dict[str, List[str]]:
        islands: List[str] = project_code.strip().split("\n")
        project: Dict[str, List[str]] = {}
        for island in islands:
            row = island.split(":")
            project[row[0].strip()] = row[1].strip().split(",")
        return project

    def test_valid_project(self):
        """Path to princess-frog."""
        cases = [
            ("A:B,C \n B:A,C \n C:A,B", True),
            ("A:B,C \n B:A,C,D \n C:A,B \n D:B", True),
            ("A:C \n B:D \n C:A \n D:B", False),
            ("A: B,C \n B: A,C,C,D \n C: A,B,B \n D:B,E \n E:D", True),
            ("A: B,C,D \n B:A,D \n C:A,D \n D:A,B,C", False),
            ("A: D \n B:D \n C:D \n D:A,B,C", False),
            ("Kotlin: Java \n JS:Java \n C#:Java \n Java:Kotlin,JS,C#", False),
            ("1: 2,5 \n 2:1,5 \n 3:4,5,6 \n 4:3,6 \n 5:1,2,3,6 \n 6:3,4,5", True),
            ("1: 2,5 \n 2:1,5 \n 3:4,5,6 \n 4:3 \n 5:1,2,3,6 \n 6:3,4,5", False),
            ("1: 2,5 \n 2:1,5 \n 3:4,4,5,6 \n 4:3,3,6 \n 5:1,2,3,6 \n 6:3,4,5", True),
            ("1: 2,5,7 \n 2:1,3,4,5,6,6,7 \n 3:2,4 \n 4:2,3 \n 5:1,2 \n 6:2,2 \n 7:1,2", True)
        ]

        for project_code, expected_result in cases:
            with self.subTest(project_code=project_code):
                project = self.read(project_code)
                self.assertEqual(is_project_success(project), expected_result)
