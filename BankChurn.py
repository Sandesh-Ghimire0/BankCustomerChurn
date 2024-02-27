from pydantic import BaseModel

class BankChurn(BaseModel):
    credit_score:str
    geography:str
    gender:str
    age:int
    tenure:int
    balance:int
    num_of_products:int
    has_cr_card:int
    is_active_member:int
    estimated_salary:int
    complain:int
    satisfaction_score:int
    card_type:int
    point_earned:int