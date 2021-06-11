import Vue from "vue";
import App from "./App.vue";
import store from "./store";
import router from "./router";
import vuetify from "./plugins/vuetify";

import path from "path";
var __dirname = path.resolve();

import AOS from "aos";
import "aos/dist/aos.css";
import VueTyperPlugin from "vue-typer";
Vue.use(VueTyperPlugin);

// Components
import "./components";

Vue.config.productionTip = false;

// import fetch, { Response, RequestInit } from "node-fetch";
// import fs from "fs";
// import { promisify } from "util";

// const readFile = promisify(fs.readFile());

// // 앞에 붙는 ://를 지운다.
// const removeProtocol = url => url.replace(/(^\w+:|^)\/\//, "");

// // 파일을 읽고 fetch의 Response 형식으로 반환함
// const fetchFile = async url => {
//   const path = removeProtocol(url);
//   const file = await readFile(path);
//   const contentType = url.indexOf(".json") !== -1 ? "application/json" : "application/octet-stream";
//   const headers = { "content-type": contentType };
//   return new Response(file, { headers });
// };

// // @ts-ignore
// // 이제 fetch 시 file 프로토콜도 지원함
// global.globalThis.fetch = async (url, init) => (url.startsWith("file://") ? fetchFile(url) : fetch(url, init));

new Vue({
  store,
  router,
  vuetify,
  created() {
    AOS.init();
  },
  render: h => h(App)
}).$mount("#app");
