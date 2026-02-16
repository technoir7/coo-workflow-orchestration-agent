from typing import Any, List, Optional
from enum import Enum
from pydantic import BaseModel
from datetime import datetime, timedelta

class Operator(str, Enum):
    EQUALS = "EQUALS"
    NOT_EQUALS = "NOT_EQUALS"
    GREATER_THAN = "GREATER_THAN"
    LESS_THAN = "LESS_THAN"
    CONTAINS = "CONTAINS"
    DAYS_SINCE = "DAYS_SINCE"

class PolicyRule(BaseModel):
    field: str
    operator: Operator
    value: Any

class Evaluator:
    @staticmethod
    def evaluate(rule: PolicyRule, context: dict) -> bool:
        """
        Deterministic evaluation of a single rule against a context dict.
        """
        actual_value = context.get(rule.field)
        
        if rule.operator == Operator.EQUALS:
            return actual_value == rule.value
        
        elif rule.operator == Operator.NOT_EQUALS:
            return actual_value != rule.value
            
        elif rule.operator == Operator.GREATER_THAN:
            if actual_value is None: return False
            return actual_value > rule.value
            
        elif rule.operator == Operator.LESS_THAN:
            if actual_value is None: return False
            return actual_value < rule.value
            
        elif rule.operator == Operator.CONTAINS:
            if actual_value is None: return False
            return rule.value in actual_value
            
        elif rule.operator == Operator.DAYS_SINCE:
             # Value is allowed days as int
             if not isinstance(actual_value, datetime):
                 return False
             delta = datetime.now() - actual_value
             return delta.days > rule.value
             
        return False
