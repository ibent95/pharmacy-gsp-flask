from json import dump
from operator import and_
from pprint import pp, pprint
import os

from app import app, request, platform, flask, render_template, jsonify


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
		result = [item.obj_to_dict() for item in objlist]
		return result