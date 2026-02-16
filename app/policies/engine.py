from typing import List, Optional
from app.models.policy import Policy
from app.models.workflow import Exception as WorkflowException # avoid keyword clash
from .rules import Evaluator, PolicyRule

class PolicyEngine:
    def __init__(self):
        pass

    def evaluate(self, policies: List[Policy], context: dict) -> List[dict]:
        """
        Evaluates a list of policies against a given context.
        Returns a list of triggered policy actions.
        """
        triggered_actions = []
        
        for policy in policies:
            if not policy.is_active:
                continue
                
            # Parse rules from JSONB
            # Assuming policy.rules is a dict with a list of rules
            # e.g. {"rules": [{"field": "status", "operator": "EQUALS", "value": "IN_PROGRESS"}]}
            
            rules_data = policy.rules.get("rules", [])
            match = True
            
            for rule_def in rules_data:
                rule = PolicyRule(**rule_def)
                if not Evaluator.evaluate(rule, context):
                    match = False
                    break
            
            if match:
                triggered_actions.append({
                    "policy_id": policy.id,
                    "policy_name": policy.name,
                    "actions": policy.actions
                })
                
        return triggered_actions
