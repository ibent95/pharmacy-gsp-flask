const path = require('path');
const { merge } = require('webpack-merge');

const commonWebpackSettings = require('./webpack.config.common.js');

module.exports = merge(commonWebpackSettings, {
	mode: 'production',
});