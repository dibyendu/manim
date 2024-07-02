const path = require('path')

module.exports = {
  mode: 'production',
  devtool: 'source-map',
  optimization: {
    usedExports: true
  },
  entry: {
    app: './manim_binder.ts'
  },
  output: {
    filename: 'manim-binder.min.js',
    path: path.resolve(__dirname, 'source', '_static', 'js'),
    publicPath: '/'
  },
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /node_modules/
      },
      {
        test: /\.(css|svg|ttf|eot|woff2|woff)/,
        loader: 'ignore-loader'
      }
    ]
  },
  resolve: {
    extensions: ['.ts', '.js']
  }
}
