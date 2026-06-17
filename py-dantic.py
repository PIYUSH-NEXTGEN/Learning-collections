from pydantic import  BaseModel, EmailStr, AnyUrl, Field, field_validator, computed_field
from typing import List, Dict, Optional, Annotated

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip_code: str

class Patient(BaseModel):
    # name: str = Field(max_length=50 )
    name : Annotated[str, Field(max_length=50,title="Name of patient",
                                description="Give name of the patient in less than 50 char",
                                examples = [' Nitesh', 'John Doe'])]
    age: int
    weight: float = Field(gt=0)
    height: float = Field(gt=0)
    married: bool
    address: Optional[Address] = None
    allergies: Optional[List[str]] = None
    contact_info: Dict[str, str]
    email:EmailStr
    social: Optional[AnyUrl] = None

    @computed_field()
    @property
    def calc_bmi(self) -> float:
        bmi = round(self.weight / (self.height**2),2)
        return bmi

    @field_validator('email')
    @classmethod

    def email_validator(cls, value):
        valid_domains = ['hdfc.com','sbi.com']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError(f"Email domain must be one of {valid_domains}")
        return value

    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()

    @field_validator('age',mode='after')
    @classmethod
    def validate_age(cls, value):
        if 0< value < 120:
            return value
        else:
            raise ValueError("Age must be between 0 and 120")

def patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_info)
    print(patient.email)
    print(patient.social)
    print(patient.calc_bmi)
    print(patient.address)

patient_info = {'name': 'John Doe', 'age': 30, 'weight':50,'height':1.75,
                'married':True,'allergies':['pollen','dust'],
                'contact_info':{'email':'john.doe@example.com','phone':'1234'},
                'email': 'john.doe@hdfc.com',
                'social': 'https://twitter.com/johndoe',
                'address': {'street': '123 Main St', 'city': 'Anytown', 'state': 'CA', 'zip_code': '12345'}}
patient1 = Patient(**patient_info)
patient_data(patient1)