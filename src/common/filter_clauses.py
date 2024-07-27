from abc import ABC, abstractmethod

class Clause(ABC):
    def __init__(self, column: str, value: list):
        self.column = column
        self.value = value[0]
    
    @abstractmethod
    def generate_sql(self) -> str:
        ...


class EqualClause(Clause):
    def generate_sql(self):
        return f"{self.column} = '{self.value}'"


class NotEqualClause(Clause):
    def generate_sql(self):
        return f"{self.column} != '{self.value}'"


class LikeClause(Clause):
    def __init__(self, column: str, value: list):
        self.column = column
        self.value = value[0].replace("*", "%")

    def generate_sql(self):
        return f"{self.column} LIKE '{self.value}'"


class IsNullClause(Clause):
    def generate_is_null_sql(self):
        return f"{self.column} IS NULL"

    def generate_is_not_null_sql(self):
        return f"{self.column} IS NOT NULL"
    
    def generate_sql(self):
        return self.generate_is_null_sql() if self.value == "true" else self.generate_is_not_null_sql()


class ContainClause(Clause):
    def __init__(self, column: str, value: list):
        self.column = column
        self.value = "{" + ",".join(value) + "}"

    def generate_sql(self):
        return f"{self.column} @> '{self.value}'"
    

type_to_clause_map = {
    "equal": EqualClause,
    "not_equal": NotEqualClause,
    "like": LikeClause,
    "is_null": IsNullClause,
    "contain": ContainClause
}