from enum import Enum, unique

@unique
class GSPCalculationTypeEnum(str, Enum):
	TRAINING = 'training'
	TESTING = 'testing'