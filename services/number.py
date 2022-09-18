class Number:

	def normalizeNumber(rawNumber):
		result = None

		if (isinstance(rawNumber, list)):
			result = [float(i) / max(rawNumber) for i in rawNumber]

		elif (isinstance(rawNumber, float)):
			result = float(rawNumber) / 1

		return result

	def percentToFloat(rawNumber):
		result = None

		if (isinstance(rawNumber, str)) :
			result = float(rawNumber.strip('%')) / 100

		elif (isinstance(rawNumber, float) or isinstance(rawNumber, int)):
			result = rawNumber / 100


		return result