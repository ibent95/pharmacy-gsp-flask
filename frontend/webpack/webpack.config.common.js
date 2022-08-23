const path = require('path');

const sourcePath = 'frontend/src/';
const outputPath = '../../static';

module.exports = {
	entry: [
		'./' + sourcePath + '/ts/app.ts',
		//path.resolve(__dirname, sourcePath + '/js')
	],
	output: {
		path: path.resolve(__dirname, outputPath),
		filename: 'js/app.js',
	},
	resolve: {
		// Add `.ts` and `.tsx` as a resolvable extension.
		extensions: ['.js', '.jsx', '.ts', '.tsx']
	},
	module: {
		rules: [
			{
				test: /\.s[ac]ss$/i, // /\.css$/i
				use: ['style-loader', 'css-loader', 'postcss-loader'],
				include: [
					path.resolve(__dirname, sourcePath + '/css'),
				],
			},
			{
				test: /\.js$/,
				loader: 'esbuild-loader',
				exclude: /node_modules/,
				include: [
					path.resolve(__dirname, sourcePath + '/ts'),
					path.resolve(__dirname, sourcePath + '/tsx'),
				],
				options: {
					target: ['es2015']
				}
			},
			//{
			//	test: /\.tsx?$/, // .ts or .tsx
			//	use: ['ts-loader'],
			//	exclude: /node_modules/,
			//	include: [
			//		path.resolve(__dirname, sourcePath + '/ts'),
			//		path.resolve(__dirname, sourcePath + '/tsx'),
			//	],
			//},
		],
	},
};