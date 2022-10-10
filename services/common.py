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


class RequestTypeConverter(BaseConverter):

	def to_python(self, value):
		try:
			request_type = GSPCalculationTypeEnum(value)
			return request_type
		except ValueError as err:
			raise ValidationError()

	def to_url(self, object):
		return object
