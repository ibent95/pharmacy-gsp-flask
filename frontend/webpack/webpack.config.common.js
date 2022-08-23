const path = require('path');

const outputPath = '../../static';

module.exports = {
	entry: './frontend/src/ts/app.ts',
	output: {
		path: path.resolve(__dirname, outputPath),
		filename: 'js/app.js',
	},
};