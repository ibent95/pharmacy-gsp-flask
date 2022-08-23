const glob = require("glob");
const Path = require("path");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const CopyWebpackPlugin = require("copy-webpack-plugin");
const WebpackAssetsManifest = require("webpack-assets-manifest");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");

const srcPath = "frontend/src";
const outputPath = "../../static";

module.exports = {
  entry: {
    app: [
      "./" + srcPath + "/ts/app.ts",
      "./" + srcPath + "/js/app.js",
    ]
  },
  output: {
    filename: "js/[name].js",
    path: Path.resolve(__dirname, outputPath),
    //path: Path.join(__dirname, ),
    //publicPath: "/static/",
    //assetModuleFilename: "[path][name][ext]",
  },
  optimization: {
    mergeDuplicateChunks: false,
    runtimeChunk: { name: 'manifest' },
    splitChunks: {
      // removed name and chunks from here
      chunks: 'all',
      name: 'vendor',
    },
  },
  plugins: [
    new CleanWebpackPlugin(),
    new CopyWebpackPlugin({
      patterns: [
        { from: Path.resolve(__dirname, "../src/images"), to: "images" },
        { from: Path.resolve(__dirname, "../src/assets"), to: "assets" },
      ],
    }),
    new WebpackAssetsManifest({
      entrypoints: true,
      output: "manifest.json",
      writeToDisk: true,
      //publicPath: true,
    }),
    new MiniCssExtractPlugin({
      filename: './css/[name].css',
    }),
  ],
  resolve: {
    alias: {
      "~": Path.resolve(__dirname, "../src"),
    },
    extensions: ['.ts', '.js', '.tsx', '.jsx'],
  },
  module: {
    rules: [
      {
        test: /\.sass$|\.scss$/,
        use: [MiniCssExtractPlugin.loader, 'css-loader', 'sass-loader'],
      },
      {
        test: /\.css$/i,
        use: ['style-loader', 'css-loader'],
      },
      {
        test: /\.tsx?$/,
        use: "ts-loader",
        exclude: /node_modules/,
      },
      {
        test: /\.js$/,
        include: /node_modules/,
        type: "javascript/auto",
      },
      {
        test: /\.(ico|jpg|jpeg|png|gif|eot|otf|webp|svg|ttf|woff|woff2)(\?.*)?$/,
        type: "asset/inline",
      },
    ],
  },
};
