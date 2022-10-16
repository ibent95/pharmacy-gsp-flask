import os

from json import dump
from operator import and_
from pprint import pp, pprint

from app import app, request, platform, flask, render_template, jsonify
from werkzeug.routing import BaseConverter, ValidationError
from enumerations.common import GSPCalculationTypeEnum


class Common:

	def __init__(self):
		message = "Initiate Common service."

	def setLogger(type, message, data):

		messageObject = message + ' | data: %s |'

		match type:

			case "info":
				app.logger.info(messageObject, data)

			case "warning":
				app.logger.warn(messageObject, data)

			case "error":
				app.logger.error(messageObject, data)

			case "exception":
				app.logger.exception(messageObject, data)

			case default:
				app.logger.info(messageObject, data)

	def setPrint(message, data):
		print(message, data)

	def setPPrint(message, data):
		pp([message, data])

	def listOfDictHelper(objlist):
		result = [item.setObjectToDict() for item in objlist]
		return result

	def page_range(page, last, span=5):

		"""Return a range of page numbers around page, containing span pages
		(if possible). Page numbers run from 1 to last.

		>>> list(page_range(2, 10))
		[1, 2, 3, 4, 5]
		>>> list(page_range(4, 10))
		[2, 3, 4, 5, 6]
		>>> list(page_range(9, 10))
		[6, 7, 8, 9, 10]

		"""
		return range(
			max(
				min(page - (span - 1) // 2, last - span + 1),
				1
			),
			min(
				max(page + span // 2, span), last
			) + 1
		)

	def getDataPerPage(data, offset=0, per_page=10):
		return data[offset:offset + per_page]

class RequestTypeConverter(BaseConverter):

	def to_python(self, value):
		try:
			request_type = GSPCalculationTypeEnum(value)
			return request_type
		except ValueError as err:
			raise ValidationError()

	def to_url(self, object):
		return object
