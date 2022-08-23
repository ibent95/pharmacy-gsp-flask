const path = require('path');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

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
	plugins: [
		new MiniCssExtractPlugin(),
		//["postcss-short", { prefix: "x" }],
		//"postcss-preset-env",
	],
	module: {
		rules: [
			{
				test: /\.js$/,
				loader: 'esbuild-loader',
				exclude: /node_modules/,
				include: [
					path.resolve(__dirname, sourcePath + '/js'),
					path.resolve(__dirname, sourcePath + '/ts'),
					path.resolve(__dirname, sourcePath + '/jsx'),
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
			{ // css, scss, sass
				test: /\.s[ac]ss$/i, // /\.s(a|c)ss$/, /\.(sass|scss|less|css)$/, /\.css$/i , /\.s[ac]ss$/i, /\.s?css/i
				use: ['style-loader', 'css-loader', 'sass-loader'],

				//include: [
				//	path.resolve(__dirname, sourcePath + '/css'),
				//	path.resolve(__dirname, sourcePath + '/scss'),
				//	//path.resolve(__dirname, sourcePath + '/vendor/**'),
				//],
			},
			{ // Fonts
				test: /\.(woff(2)?|ttf|eot|svg)(\?v=\d+\.\d+\.\d+)?$/,
				use: [
					{
						loader: 'file-loader',
						options: {
							name: '[name].[ext]',
							//outputPath: path.resolve(__dirname, outputPath + '/font'),
							outputPath: 'font',
						}
					}
				]
			},
			{ // Images
				test: /\.(ico|jpg|jpeg|png|gif|otf|webp)(\?.*)?$/,
				use: [
					{
						loader: 'file-loader',
						options: {
							name: '[name].[ext]',
							//outputPath: path.resolve(__dirname, outputPath + '/images'),
							outputPath: 'images',
						}
					}
				]
			},
		],
	},
};