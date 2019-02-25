const BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  publicPath: process.env.VUE_APP_PUBLIC_PATH,
  outputDir: "./dist/",
  chainWebpack: config => {
    config.optimization.splitChunks(false);

    config
      .plugin("BundleTracker")
      .use(BundleTracker, [{ filename: "./webpack-stats.json" }]);

    config.resolve.alias.set("__STATIC__", "static");

    config.devServer
      .public(process.env.VUE_APP_PUBLIC_PATH)
      .host("0.0.0.0")
      .port(8080)
      .hotOnly(true)
      .watchOptions({ poll: 1000 })
      .https(false)
      .headers({ "Access-Control-Allow-Origin": ["*"] });
  }
};
